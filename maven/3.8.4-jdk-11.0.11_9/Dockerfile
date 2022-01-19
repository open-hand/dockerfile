FROM choerodon/adoptopenjdk:jdk-11.0.11_9

# Ref: https://raw.githubusercontent.com/carlossg/docker-maven/59bdaf8b1ec69a787d7857cd1025f1f3efd7b216/openjdk-11-slim/Dockerfile
# Install Maven Start
ARG MAVEN_VERSION=3.8.4
ARG USER_HOME_DIR="/root"
ARG SHA=a9b2d825eacf2e771ed5d6b0e01398589ac1bfa4171f36154d1b5787879605507802f699da6f7cfc80732a5282fd31b28e4cd6052338cbef0fa1358b48a5e3c8
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries

RUN apt-get update && \
    apt-get install -y \
      curl \
      procps \
      jq \
      vim \
      git \
      tar \
      wget \
      unzip \
      pylint \
      gnupg2 \
      xmlstarlet \
      openssh-server \
      mariadb-client \
      ca-certificates \
      build-essential \
      apt-transport-https \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
  && echo "${SHA}  /tmp/apache-maven.tar.gz" | sha512sum -c - \
  && tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

COPY settings-docker.xml /usr/share/maven/ref/
# Install Maven End