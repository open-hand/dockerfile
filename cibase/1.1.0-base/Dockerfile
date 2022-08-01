FROM gcr.io/kaniko-project/executor:v1.8.1 AS kaniko
FROM debian:bullseye

ENV TZ="Asia/Shanghai" \
    ROOT_PASSWORD="changeit" \
    YQ_VERSION="v4.26.1" \
    HELM_VERSION="v3.9.2" \
    DOCKER_VERSION="20.10.17" \
    PATH="/kaniko:${PATH}"

# copy kaniko
COPY --from=kaniko /kaniko /kaniko
COPY --from=kaniko /etc/nsswitch.conf /etc/nsswitch.conf

# install base packages
RUN set -eux; \
    apt-get update; \
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
        ca-certificates \
        build-essential \
        apt-transport-https; \
    ARCHITECTURE="$(uname -m)"; \
    ARCH="$(dpkg --print-architecture)"; \
    # install nodejs skopeo
    curl -sSL https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/Debian_11/Release.key | apt-key add -; \
    echo 'deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/Debian_11/ /' > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list; \
    apt-get update; \
    apt-get install -y \
        skopeo; \
    apt-get upgrade -y; \
	rm -rf /var/lib/apt/lists/*; \
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
    helm plugin install https://github.com/chartmuseum/helm-push; \
    ln -s /usr/bin/xmlstarlet /usr/bin/xml; \
    ln -s /kaniko/executor /kaniko/kaniko; \
    docker-credential-gcr config --token-source=env; \
    # Modify `sshd_config`
    sed -ri 's/^#PermitEmptyPasswords no/PermitEmptyPasswords yes/' /etc/ssh/sshd_config; \
    sed -ri 's/^#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config; \
    sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config; \
    # Delete root password (set as empty)
    passwd -d root; \
    mkdir -p /run/sshd; \
    rm -r /tmp/*;

# Add trivy
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin v0.16.0; \
    trivy image --download-db-only;

# Add mirror source
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak; \
    sed -i 's deb.debian.org mirrors.aliyun.com g' /etc/apt/sources.list

EXPOSE 22

CMD [ "/bin/sh","-c","/usr/sbin/sshd -D" ]