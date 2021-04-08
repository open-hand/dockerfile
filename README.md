# Choerodon Dockerfile

- `adoptopenjdk` - 基于 debian 镜像构建，免费的、完全无品牌的 OpenJDK 版本，基于 GPL 开源协议（+Classpath Extension），以免费软件的形式提供社区版的 OpenJDK 二进制包。
- `cibase` - 基于 adoptopenjdk 镜像构建，增加 maven、docker client、kaniko、sonar-scanner、node、yarn、helm 等软件包。
- `dbtools` - 基于 busybox 镜像构建，仅存储初始化数据库所使用到的 jar 工具包。
- `frontbase` - 基于 nginx 镜像构建，增加自定义 nginx 配置。
- `javabase` - 基于 adoptopenjdk 镜像构建，增加 tini、tar、netcat 等软件包。
- `ruamel-yaml` - 基于 busybox 镜像构建，将 ruamel.yaml 进行打包，提供给 devops-service 进行调用。
- `skywalking-agent` - 基于 busybox 镜像构建，仅存储 skywalking-agent。

## 镜像地址

- Github Action 构建后镜像推送至 Dockerhub，镜像地址规则为 `choerodon`/`一级目录名`:`二级目录名`。

- 每一小时会自动同步至阿里云容器镜像服务，镜像地址规则为 `registry.cn-shanghai.aliyuncs.com/c7n`/`一级目录名`:`二级目录名`。

- 示例如下：
    ```
    .
    ├── adoptopenjdk
    │   ├── jdk8u275-b01
    │   │   └── Dockerfile   # Dockerhub: choerodon/adoptopenjdk:jdk8u275-b01
                             # 阿里云容器镜像服务: registry.cn-shanghai.aliyuncs.com/c7n/adoptopenjdk:jdk8u275-b01
    ```