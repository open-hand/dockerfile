FROM hengyunabc/arthas:3.5.1-no-jdk AS arthas
FROM choerodon/adoptopenjdk:jdk8u282-b08
ENV TZ="Asia/Shanghai" \
    TINI_VERSION="v0.19.0" \
    JAVA_OPTS="-XX:MaxRAMPercentage=90.0"

COPY --from=arthas /opt/arthas /opt/arthas
# Install base packages
RUN apt-get update; \
    apt-get install -y --no-install-recommends \
        vim \
        tar \
        wget \
        unzip \
        netcat \
        gnupg2 \
        procps \
        net-tools \
        openssh-client \
        ca-certificates; \
    apt-get upgrade -y --no-install-recommends; \
    rm -rf /var/lib/apt/lists/*; \
    ARCH="$(dpkg --print-architecture)"; \
    wget -qO "tini-static-${ARCH}" \
       "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static-${ARCH}"; \
    wget -qO "tini-static-${ARCH}.sha256sum" \
       "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static-${ARCH}.sha256sum"; \
    sha256sum --strict --check <"tini-static-${ARCH}.sha256sum"; \
    rm -r "tini-static-${ARCH}.sha256sum"; \
    mv "tini-static-${ARCH}" /usr/bin/tini; \
    chmod +x /usr/bin/tini; \
    tini --version

# install skopeo
RUN echo 'deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/Debian_10/ /' > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list; \
    curl -L https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/Debian_10/Release.key | apt-key add -; \
    apt-get update; \
    apt-get -y install skopeo; \
    rm -rf /var/lib/apt/lists/*

# Add mirror source
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak; \
    sed -i 's http://.*.debian.org http://mirrors.aliyun.com g' /etc/apt/sources.list

RUN echo 'root:changeit' | chpasswd

ENTRYPOINT ["tini", "--"]