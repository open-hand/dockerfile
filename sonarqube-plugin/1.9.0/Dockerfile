FROM alpine:3

ENV PLUGIN_VERSION=1.9.0
USER 1001
WORKDIR /sonarqube/plugin
ADD --chown=1001:1001 https://file.choerodon.com.cn/choerodon-install/sonarqube/sonar-auth-choerodonoauth-plugin-${PLUGIN_VERSION}.RELEASE.jar /sonarqube/plugin