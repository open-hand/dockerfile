FROM choerodon/cibase:1.2.0-base

# install base packages
RUN set -eux; \
    curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -; \
    echo "deb https://deb.nodesource.com/node_16.x "$(. /etc/os-release && echo "$VERSION_CODENAME")" main" > /etc/apt/sources.list.d/nodesource.list; \
    apt-get update; \
    apt-get install -y \
        nodejs; \
	rm -rf /var/lib/apt/lists/*; \
    # install yarn typescript npm-cli-login
    npm install -g yarn; \
    npm install -g typescript; \
    npm install -g npm-cli-login
