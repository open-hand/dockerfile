FROM mirrors.saas.hand-china.com/choerodon/adoptopenjdk:jdk8u282-b08 AS jdk8
FROM mirrors.saas.hand-china.com/library/eclipse-temurin:17-jdk-jammy AS jdk17
FROM mirrors.saas.hand-china.com/library/eclipse-temurin:21-jdk-jammy AS jdk21

FROM mirrors.saas.hand-china.com/choerodon/sonar-scanner:4.6-jdk-11.0.11_9
COPY --from=jdk8  /opt/java/openjdk /opt/java/openjdk8
COPY --from=jdk17 /opt/java/openjdk /opt/java/openjdk17
COPY --from=jdk21 /opt/java/openjdk /opt/java/openjdk21

# install base packages
RUN set -eux; \
    curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -; \
    echo "deb https://deb.nodesource.com/node_20.x "$(. /etc/os-release && echo "$VERSION_CODENAME")" main" > /etc/apt/sources.list.d/nodesource.list; \
    apt-get update; \
    apt-get install -y \
        nodejs; \
	rm -rf /var/lib/apt/lists/*;