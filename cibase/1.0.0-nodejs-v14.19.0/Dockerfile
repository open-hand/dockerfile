FROM choerodon/cibase:1.0.0-base

ENV TYPESCRIPT_VERSION="3.6.3"
# install base packages
RUN set -eux; \
    ARCHITECTURE="$(uname -m)"; \
    ARCH="$(dpkg --print-architecture)"; \
    # install nodejs skopeo
    curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -; \
    echo 'deb https://deb.nodesource.com/node_14.x buster main' > /etc/apt/sources.list.d/nodesource.list; \
    apt-get update; \
    apt-get upgrade -y; \
    apt-get install -y \
        nodejs; \
	rm -rf /var/lib/apt/lists/*; \
    # install yarn
    npm install -g yarn; \
    # install typescript
    npm install -g typescript@${TYPESCRIPT_VERSION};