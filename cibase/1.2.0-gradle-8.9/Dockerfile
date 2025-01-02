FROM eclipse-temurin:8-jdk-jammy AS jdk8
FROM eclipse-temurin:11-jdk-jammy AS jdk11

FROM choerodon/cibase:1.2.0-jdk17

ENV ANDROID_SDK_CLI_VERSION="11076708_latest" \
    GRADLE_VERSION="8.9-bin" \
    PATH="/opt/gradle/bin:/opt/android-sdk-cli/bin:$PATH" \
    ANDROID_HOME="/root/android-sdk" \
    JAVA_8_HOME="/opt/java/openjdk8" \
    JAVA_11_HOME="/opt/java/openjdk11" \
    JAVA_17_HOME="/opt/java/openjdk"

COPY --from=jdk8  /opt/java/openjdk /opt/java/openjdk8
COPY --from=jdk11 /opt/java/openjdk  /opt/java/openjdk11

RUN wget -qO "/tmp/commandlinetools-linux-${ANDROID_SDK_CLI_VERSION}.zip" \
    https://googledownloads.cn/android/repository/commandlinetools-linux-${ANDROID_SDK_CLI_VERSION}.zip; \
    unzip /tmp/commandlinetools-linux-${ANDROID_SDK_CLI_VERSION}.zip -d /tmp; \
    mv /tmp/cmdline-tools /opt/android-sdk-cli; \
    yes | sdkmanager "platform-tools" "build-tools;34.0.0" "platforms;android-34" --sdk_root="/root/android-sdk"; \
    wget -qO "/tmp/gradle-${GRADLE_VERSION}.zip" \
    https://mirrors.aliyun.com/macports/distfiles/gradle/gradle-${GRADLE_VERSION}.zip; \
    unzip /tmp/gradle-${GRADLE_VERSION}.zip -d /tmp; \
    mv /tmp/gradle-8.9 /opt/gradle; \
    rm -r /tmp/*; \
    mv /opt/java/openjdk /opt/java/openjdk11; \
    ln -snf /opt/java/openjdk11 /opt/java/openjdk; \
    echo 'alias jdk8="ln -snf $JAVA_8_HOME /opt/java/openjdk"' > ~/.bashrc; \
    echo 'alias jdk11="ln -snf $JAVA_11_HOME /opt/java/openjdk"' > ~/.bashrc; \
    echo 'alias jdk17="ln -snf $JAVA_17_HOME /opt/java/openjdk"' > ~/.bashrc;