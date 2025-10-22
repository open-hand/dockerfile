FROM busybox:1.32

ARG USERNAME \
    PASSWORD

ENV TOOL_LIQUIBASE_VERSION="3.0-RELEASE"

ADD --chown=www-data:www-data \
    https://${USERNAME}:${PASSWORD}@nexus.choerodon.com.cn/repository/choerodon-release/io/choerodon/choerodon-tool-liquibase/3.0.RELEASE/choerodon-tool-liquibase-3.0.RELEASE.jar \
    /var/choerodon/liquibase.jar
WORKDIR /var/choerodon
RUN ln -s liquibase.jar choerodon-tool-liquibase.jar

USER 33