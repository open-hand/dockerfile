FROM choerodon/adoptopenjdk:jdk8u282-b08 as jdk

FROM choerodon/sonar-scanner:4.6-jdk-11.0.11_9
COPY --from=jdk /opt/java/openjdk /opt/java/openjdk8