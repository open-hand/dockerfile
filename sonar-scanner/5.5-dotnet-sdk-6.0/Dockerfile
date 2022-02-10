FROM mcr.microsoft.com/dotnet/sdk:6.0

RUN apt-get update && \
    apt-get install -y \
      openjdk-11-jre \
  && rm -rf /var/lib/apt/lists/*

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

RUN dotnet tool install --global dotnet-sonarscanner --version 5.5.1

ENV PATH="${HOME}/.dotnet/tools:${PATH}"