FROM mikefarah/yq:4.47.1 AS yq
FROM docker:26.1.4-cli AS docker
FROM martizih/kaniko:v1.25.3-debug AS kaniko
FROM aquasec/trivy:0.66.0 AS trivy

FROM buildpack-deps:bookworm

RUN groupadd --gid 1000 node \
  && useradd --uid 1000 --gid node --shell /bin/bash --create-home node

# gpg keys listed at https://github.com/nodejs/node#release-team
RUN set -ex \
  && for key in \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    56730D5401028683275BD23C23EFEFE93C4CFFFE \
    77984A986EBC2AA786BC0F66B01FBB92821C587A \
    8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 \
  ; do \
    gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
    gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
    gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
  done

ENV NODE_VERSION 10.10.0

RUN buildDeps='xz-utils' \
    && ARCH= && dpkgArch="$(dpkg --print-architecture)" \
    && case "${dpkgArch##*-}" in \
      amd64) ARCH='x64';; \
      ppc64el) ARCH='ppc64le';; \
      s390x) ARCH='s390x';; \
      arm64) ARCH='arm64';; \
      armhf) ARCH='armv7l';; \
      i386) ARCH='x86';; \
      *) echo "unsupported architecture"; exit 1 ;; \
    esac \
    && set -x \
    && apt-get update && apt-get install -y ca-certificates curl wget $buildDeps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
    && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
    && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
    && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
    && apt-get purge -y --auto-remove $buildDeps \
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs

ENV YARN_VERSION 1.9.4

RUN set -ex \
  && for key in \
    6A010C5166006599AA17F08146C2130DFD2497F5 \
  ; do \
    gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
    gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
    gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
  done \
  && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
  && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \
  && gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
  && mkdir -p /opt \
  && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \
  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \
  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \
  && rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz


ENV TZ="Asia/Shanghai" \
    ROOT_PASSWORD="changeit" \
    HELM_VERSION="v3.18.6" \
    PATH="/kaniko:${PATH}"

# install yq
COPY --from=yq /usr/bin/yq /usr/bin/yq

# install kaniko
COPY --from=kaniko /kaniko /kaniko
COPY --from=kaniko /etc/nsswitch.conf /etc/nsswitch.conf

# install docker-client-cli
COPY --from=docker /usr/local/bin/docker /usr/local/bin/docker
COPY --from=docker /usr/local/libexec/docker/cli-plugins/docker-buildx /usr/local/libexec/docker/cli-plugins/docker-buildx

# install trivy
COPY --from=trivy /usr/local/bin/trivy /usr/local/bin/trivy
COPY --from=trivy /contrib/ /contrib/

# install typescript npm-cli-login
RUN npm install -g typescript; \
    npm install -g npm-cli-login --unsafe-perm

# install base packages
RUN set -eux; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
        jq \
        vim \
        git \
        tar \
        curl \
        wget \
        unzip \
        pylint \
        gnupg2 \
        skopeo \
        xmlstarlet \
        openssh-server \
        mariadb-client \
        ca-certificates \
        build-essential; \
	rm -rf /var/lib/apt/lists/*; \
    ARCH="$(dpkg --print-architecture)"; \
    # install helm
    wget -qO "/tmp/helm-${HELM_VERSION}-linux-${ARCH}.tar.gz" \
        "https://get.helm.sh/helm-${HELM_VERSION}-linux-${ARCH}.tar.gz"; \
    tar xzf "/tmp/helm-${HELM_VERSION}-linux-${ARCH}.tar.gz" -C /tmp; \
    mv /tmp/linux-${ARCH}/helm /usr/bin/helm; \
    # post install
    helm plugin install https://github.com/chartmuseum/helm-push; \
    ln -s /kaniko/executor /kaniko/kaniko; \
    ln -s /usr/bin/xmlstarlet /usr/bin/xml; \
    docker-credential-gcr config --token-source=env; \
    # Modify `sshd_config`
    sed -ri 's/^#PermitEmptyPasswords no/PermitEmptyPasswords yes/' /etc/ssh/sshd_config; \
    sed -ri 's/^#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config; \
    sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config; \
    # Delete root password (set as empty)
    passwd -d root; \
    mkdir -p /run/sshd; \
    rm -r /tmp/*;

# Add mirror source
RUN sed -i "s@http://.*deb.debian.org@http://repo.huaweicloud.com@g" /etc/apt/sources.list.d/debian.sources

EXPOSE 22

CMD [ "/bin/sh","-c","/usr/sbin/sshd -D" ]