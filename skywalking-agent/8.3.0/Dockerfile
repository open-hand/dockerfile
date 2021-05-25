FROM busybox:1.32 AS build
ENV SKYWALKING_VERSION="8.3.0"
ADD --chown=www-data:www-data \
    https://archive.apache.org/dist/skywalking/${SKYWALKING_VERSION}/apache-skywalking-apm-${SKYWALKING_VERSION}.tar.gz \
    /apache-skywalking-apm-${SKYWALKING_VERSION}.tar.gz
RUN tar zxf /apache-skywalking-apm-${SKYWALKING_VERSION}.tar.gz; \
    mv /apache-skywalking-apm-bin/agent/optional-plugins/apm-trace-ignore-plugin-${SKYWALKING_VERSION}.jar \
    /apache-skywalking-apm-bin/agent/plugins;

FROM busybox:1.32
ENV SKYWALKING_VERSION="8.3.0"
COPY --from=build --chown=www-data:www-data /apache-skywalking-apm-bin/agent /skywalking/agent
USER 33