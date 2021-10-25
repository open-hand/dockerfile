FROM dockerhub.k8s.saas.hand-china.com/library/debian:stretch


RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
    sed -i 's http://.*.debian.org http://mirrors.aliyun.com g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y \
        git \
        curl \
        tzdata \
        connect-proxy \
        ca-certificates && \
    mkdir -p /ssh-keys && \
    curl -sSL -o /usr/bin/kubectl \
       "http://mirror.azure.cn/kubernetes/kubectl/$(curl -sSL http://mirror.azure.cn/kubernetes/kubectl/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod a+x /usr/bin/kubectl && \
    curl -sSL -o /usr/bin/tini \
        "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" && \
    chmod a+x /usr/bin/tini && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone
