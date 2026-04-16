FROM mikefarah/yq:4.45.1 AS yq
FROM docker:27.5.1-cli AS docker
FROM gcr.io/kaniko-project/executor:v1.23.2 AS kaniko

FROM maven:3.9.9-eclipse-temurin-23
# disable 'maven-default-http-blocker'
RUN sed -i '160,166d' /usr/share/maven/conf/settings.xml

ENV TZ="Asia/Shanghai" \
    ROOT_PASSWORD="changeit" \
    SKOPEO_VERSION="v1.22.2" \
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

ADD --chmod=644 https://raw.githubusercontent.com/containers/skopeo/refs/heads/main/default-policy.json /etc/containers/policy.json

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
        xmlstarlet \
        openssh-server \
        mariadb-client \
        ca-certificates; \
	rm -rf /var/lib/apt/lists/*; \
    ARCH="$(dpkg --print-architecture)"; \
    wget -qO "skopeo-linux-${ARCH}" \
       "https://github.com/lework/skopeo-binary/releases/download/${SKOPEO_VERSION}/skopeo-linux-${ARCH}"; \
    mv "skopeo-linux-${ARCH}" /usr/bin/skopeo; \
    chmod a+rx /usr/bin/skopeo; \
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
RUN sed -i 's http://.*.ubuntu.com http://mirrors.aliyun.com g' /etc/apt/sources.list.d/ubuntu.sources

EXPOSE 22

CMD [ "/bin/sh","-c","/usr/sbin/sshd -D" ]
