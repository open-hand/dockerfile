FROM debian:stretch

ENV TINI_VERSION=v0.19.0 \
    KUBECTL_VERSION=v1.21.14

RUN apt-get update; \
    apt-get install -y \
        git \
        curl \
        wget \
        nmap \
        tzdata \
        ca-certificates; \
    rm -rf /var/lib/apt/lists/*; \
    mkdir -p /ssh-keys; \
    ARCH="$(dpkg --print-architecture)"; \
    wget -qO "tini-static-${ARCH}" \
       "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static-${ARCH}"; \
    wget -qO "tini-static-${ARCH}.sha256sum" \
       "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static-${ARCH}.sha256sum"; \
    sha256sum --strict --check <"tini-static-${ARCH}.sha256sum"; \
    rm -r "tini-static-${ARCH}.sha256sum"; \
    mv "tini-static-${ARCH}" /usr/bin/tini; \
    chmod +x /usr/bin/tini; \
    tini --version; \
    wget -qO "kubernetes-client-linux-${ARCH}.tar.gz" \
        "https://dl.k8s.io/${KUBECTL_VERSION}/kubernetes-client-linux-${ARCH}.tar.gz"; \
    tar zxvf kubernetes-client-linux-${ARCH}.tar.gz; \
    mv kubernetes/client/bin/kubectl /usr/bin/kubectl; \
    chmod +x /usr/bin/kubectl; \
    kubectl --version; \
    rm -rf kubernetes

# Add mirror source
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak; \
    sed -i 's http://.*.debian.org http://mirrors.aliyun.com g' /etc/apt/sources.list

RUN echo 'root:changeit' | chpasswd

ENTRYPOINT ["tini", "--"]
