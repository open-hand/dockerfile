FROM busybox:1.32

ENV TOOL_LIQUIBASE_VERSION="3.0-SNAPSHOT"

ADD --chown=www-data:www-data \
    https://nexus.choerodon.com.cn/repository/choerodon-snapshot/com/zknow/starter/zknow-tool-liquibase/3.0-SNAPSHOT/zknow-tool-liquibase-3.0-20250924.102728-3.jar \
    /var/choerodon/liquibase.jar
WORKDIR /var/choerodon
RUN ln -s liquibase.jar choerodon-tool-liquibase.jar

USER 33