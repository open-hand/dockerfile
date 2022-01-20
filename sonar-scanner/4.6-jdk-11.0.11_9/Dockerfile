FROM choerodon/maven:3.8.4-jdk-11.0.11_9

ENV SONAR_SCANNER_HOME="/opt/sonar-scanner" \
    SONAR_SCANNER_VERSION="4.6.2.2472"
ENV PATH="${SONAR_SCANNER_HOME}/bin:${PATH}"

# copy sonar-scanner-cli
COPY sonar-scanner/bin /opt/sonar-scanner/bin
COPY sonar-scanner/conf /opt/sonar-scanner/conf
COPY sonar-scanner/lib /opt/sonar-scanner/lib