FROM choerodon/adoptopenjdk:jdk8u282-b08 as jdk8
FROM eclipse-temurin:17-jdk-jammy as jdk17

FROM choerodon/sonar-scanner:4.6-jdk-11.0.11_9
COPY --from=jdk8  /opt/java/openjdk /opt/java/openjdk8
COPY --from=jdk17 /opt/java/openjdk /opt/java/openjdk17

# install base packages
RUN set -eux; \
    curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -; \
    echo "deb https://deb.nodesource.com/node_14.x "$(. /etc/os-release && echo "$VERSION_CODENAME")" main" > /etc/apt/sources.list.d/nodesource.list; \
    apt-get update; \
    apt-get install -y \
        nodejs; \
	rm -rf /var/lib/apt/lists/*;