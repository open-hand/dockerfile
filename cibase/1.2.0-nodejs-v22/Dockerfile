FROM choerodon/cibase:1.2.0-base

# install base packages
RUN set -eux; \
    curl -fsSL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh; \
    bash nodesource_setup.sh; \
    apt-get update; \
    apt-get install -y \
        nodejs; \
	rm -rf /var/lib/apt/lists/*; \
    # install yarn typescript npm-cli-login
    npm install -g yarn; \
    npm install -g typescript; \
    npm install -g npm-cli-login
