FROM nginxinc/nginx-unprivileged:1.29

USER 0

# Modify timezone
ENV TZ=Asia/Shanghai

RUN apt-get update; \
    apt-get install -y --no-install-recommends \
        vim \
        curl \
        ca-certificates; \
    apt-get upgrade -y --no-install-recommends; \
    rm -rf /var/lib/apt/lists/*;

# Nginx conf
ADD default.conf /etc/nginx/conf.d/default.conf

# aliyun mirror
RUN sed -i 's http://.*.debian.org http://mirrors.aliyun.com g' /etc/apt/sources.list.d/debian.sources

RUN echo 'root:changeit' | chpasswd
