FROM busybox:1.32 AS build
ENV SKYWALKING_VERSION="8.10.0"
ADD --chown=www-data:www-data \
    https://dlcdn.apache.org/skywalking/java-agent/${SKYWALKING_VERSION}/apache-skywalking-java-agent-${SKYWALKING_VERSION}.tgz \
    /apache-skywalking-java-agent-${SKYWALKING_VERSION}.tgz
RUN tar zxf /apache-skywalking-java-agent-${SKYWALKING_VERSION}.tgz; \
    mv /skywalking-agent/optional-plugins/apm-trace-ignore-plugin-${SKYWALKING_VERSION}.jar \
    /skywalking-agent/plugins;

FROM busybox:1.32
ENV SKYWALKING_VERSION="8.10.0"
COPY --from=build --chown=www-data:www-data /skywalking-agent /skywalking/agent
USER 33