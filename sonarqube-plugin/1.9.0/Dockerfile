FROM busybox:1.32

ENV PLUGIN_VERSION=1.9.0
WORKDIR /sonarqube/plugin
USER 33
ADD --chown=www-data:www-data https://file.choerodon.com.cn/choerodon-install/sonarqube/sonar-auth-choerodonoauth-plugin-${PLUGIN_VERSION}.RELEASE.jar /sonarqube/plugin