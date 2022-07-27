FROM debian:buster

ENV TINI_VERSION=v0.19.0 \
    KUBECTL_VERSION=v1.21.14

RUN apt-get update && \
    apt-get install -y \
        git \
        curl \
        ncat \
        tzdata \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*  && \
    mkdir -p /ssh-keys && \
    curl -sSL -o /usr/bin/kubectl \
       "http://mirror.azure.cn/kubernetes/kubectl/${KUBECTL_VERSION}/bin/linux/amd64/kubectl" && \
    chmod a+x /usr/bin/kubectl && \
    curl -sSL -o /usr/bin/tini \
        "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" && \
    chmod a+x /usr/bin/tini && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
    sed -i 's http://.*.debian.org http://mirrors.aliyun.com g' /etc/apt/sources.list

RUN echo 'root:changeit' | chpasswd
USER 33

ENTRYPOINT ["tini", "--"]