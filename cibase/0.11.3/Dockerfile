FROM gcr.io/kaniko-project/executor:v1.5.1 AS kaniko
FROM choerodon/adoptopenjdk:jdk8u275-b01

# Ref: https://github.com/carlossg/docker-maven/blob/26ba49149787c85b9c51222b47c00879b2a0afde/openjdk-8/Dockerfile
# Install Maven Start
ARG MAVEN_VERSION=3.6.3
ARG USER_HOME_DIR="/root"
ARG SHA=c35a1803a6e70a126e80b2b3ae33eed961f83ed74d18fcd16909b2d44d7dada3203f1ffe726c17ef8dcca2dcaa9fca676987befeadc9b9f759967a8cb77181c0
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries

RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
  && echo "${SHA}  /tmp/apache-maven.tar.gz" | sha512sum -c - \
  && tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"
# Install Maven End

ENV SONAR_SCANNER_HOME="/opt/sonar-scanner" \
    SONAR_SCANNER_VERSION="4.5.0.2216"

ENV TZ="Asia/Shanghai" \
    YQ_VERSION="v4.6.1" \
    HELM_VERSION="v3.5.2" \
    DOCKER_VERSION="19.03.13" \
    HELM_PUSH_VERSION="v0.9.0" \
    TYPESCRIPT_VERSION="3.6.3" \
    PATH="${SONAR_SCANNER_HOME}/bin:/kaniko:${PATH}"

# copy kaniko
COPY --from=kaniko /kaniko /kaniko
COPY --from=kaniko /etc/nsswitch.conf /etc/nsswitch.conf
# copy sonar-scanner-cli
COPY sonar-scanner/bin /opt/sonar-scanner/bin
COPY sonar-scanner/conf /opt/sonar-scanner/conf
COPY sonar-scanner/lib /opt/sonar-scanner/lib

# install base packages
RUN set -eux; \
    apt-get update; \
    apt-get install -y \
        jq \
        vim \
        git \
        tar \
        wget \
        unzip \
        pylint \
        gnupg2 \
        xmlstarlet \
        mariadb-client \
        ca-certificates \
        apt-transport-https; \
    ARCHITECTURE="$(uname -m)"; \
    ARCH="$(dpkg --print-architecture)"; \
    # install nodejs
    curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -; \
    echo 'deb https://deb.nodesource.com/node_14.x buster main' > /etc/apt/sources.list.d/nodesource.list; \
    echo 'deb-src https://deb.nodesource.com/node_14.x buster main' >> /etc/apt/sources.list.d/nodesource.list; \
    apt-get update; \
    apt-get install -y \
        nodejs; \
	rm -rf /var/lib/apt/lists/*; \
    # install yarn
    npm install -g yarn; \
    # install typescript
    npm install -g typescript@${TYPESCRIPT_VERSION}; \
    # install docker client
    wget -qO "/tmp/docker-${DOCKER_VERSION}-ce.tgz" \
        "https://download.docker.com/linux/static/stable/${ARCHITECTURE}/docker-${DOCKER_VERSION}.tgz"; \
    tar zxf "/tmp/docker-${DOCKER_VERSION}-ce.tgz" -C /tmp; \
    mv /tmp/docker/docker /usr/bin; \
    # install yq
    wget -qO /usr/bin/yq \
        "https://github.com/mikefarah/yq/releases/download/${YQ_VERSION}/yq_linux_${ARCH}"; \
    chmod a+x /usr/bin/yq; \
    # install helm
    wget -qO "/tmp/helm-${HELM_VERSION}-linux-${ARCH}.tar.gz" \
        "https://get.helm.sh/helm-${HELM_VERSION}-linux-${ARCH}.tar.gz"; \
    tar xzf "/tmp/helm-${HELM_VERSION}-linux-${ARCH}.tar.gz" -C /tmp; \
    mv /tmp/linux-${ARCH}/helm /usr/bin/helm; \
    # post install
    helm plugin install --version ${HELM_PUSH_VERSION} https://github.com/chartmuseum/helm-push; \
    # Don't use embedded jre
    sed -i '/use_embedded_jre=true/d' /opt/sonar-scanner/bin/sonar-scanner; \
    ln -s /usr/bin/xmlstarlet /usr/bin/xml; \
    ln -s /kaniko/executor /kaniko/kaniko; \
    docker-credential-gcr config --token-source=env; \
    rm -r /tmp/*;

# Add trivy
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin v0.16.0; \
    trivy image --download-db-only;

# Add mirror source
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak; \
    sed -i 's deb.debian.org mirrors.aliyun.com g' /etc/apt/sources.list