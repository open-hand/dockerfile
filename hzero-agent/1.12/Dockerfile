FROM docker.xuanyuan.me/library/busybox:1.32 AS build
ENV HZERO_AGENT_VERSION="1.12"
ADD --chown=www-data:www-data \
    https://files.saas.hand-china.com/choerodon/hzero-agent-${HZERO_AGENT_VERSION}.tgz \
    /hzero-agent-${HZERO_AGENT_VERSION}.tgz

RUN tar zxf /hzero-agent-${HZERO_AGENT_VERSION}.tgz;

FROM docker.xuanyuan.me/library/busybox:1.32
ENV HZERO_AGENT_VERSION="1.12"


COPY --from=build --chown=www-data:www-data /hzero-agent /hzero/agent

COPY --chown=www-data:www-data opentelemetry-java-instrumentation-propagator-ext-0.1.0-all.jar /hzero/agent
COPY --chown=www-data:www-data opentelemetry-javaagent.jar /hzero/agent
COPY --chown=www-data:www-data opentelemetry-samplers.jar /hzero/agent

USER 33
