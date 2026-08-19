FROM ghcr.io/pixil98/bitnami-postgres-pgvecto-rs:16.6.0-debian-12-r2

# 切 root 装依赖
USER root
RUN apt update && apt install -y --no-install-recommends \
    git build-essential postgresql-server-dev-16 \
    && rm -rf /var/lib/apt/lists/*

# 编译安装 pgvector
RUN cd /tmp \
    && git clone --branch v0.8.2 https://github.com/pgvector/pgvector.git \
    && cd pgvector \
    && make \
    && make install \
    && cd /tmp && rm -rf pgvector

# 切回 postgres 用户
USER 1001