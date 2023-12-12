FROM hengyunabc/arthas:3.7.1-no-jdk AS arthas
FROM eclipse-temurin:8u392-b08-jdk-jammy
ENV TZ="Asia/Shanghai" \
    TINI_VERSION="v0.19.0" \
    JAVA_OPTS="-XX:InitialRAMPercentage=70.0 -XX:MaxRAMPercentage=70.0 -XX:+HeapDumpOnOutOfMemoryError"

COPY --from=arthas /opt/arthas /opt/arthas
COPY jvmdump.sh /usr/bin/jvmdump

# Install base packages
RUN apt-get update; \
    apt-get install -y --no-install-recommends \
        vim \
        tar \
        wget \
        unzip \
        skopeo \
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
    chmod a+x /usr/bin/tini; \
    chmod a+x /usr/bin/jvmdump; \
    tini --version; \
    skopeo --version; \
    case "${ARCH}" in \
       amd64|x86_64) \
         curl -fsSL https://tier1app.com/dist/ycrash/yc-agent-latest.zip -o yc-agent-latest.zip; \
         unzip yc-agent-latest.zip; \
         mv linux/yc /usr/bin/yc; \
         chmod a+x /usr/bin/yc; \
         rm -r yc-agent-latest.zip linux mac windows; \
         yc --version; \
         ;; \
       *) \
         echo "Unsupported arch: ${ARCH}"; \
         ;; \
    esac

# Add mirror source
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak; \
    sed -i 's http://.*.ubuntu.com http://mirrors.aliyun.com g' /etc/apt/sources.list

RUN echo 'root:changeit' | chpasswd

ENTRYPOINT ["tini", "--"]