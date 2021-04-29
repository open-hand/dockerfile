FROM nginxinc/nginx-unprivileged:1.19

USER 0

# Modify timezone
ENV TZ=Asia/Shanghai

RUN apt-get update; \
    apt-get install -y \
        vim \
        curl \
        ca-certificates; \
    apt-get upgrade -y; \
    rm -rf /var/lib/apt/lists/*;

# Nginx conf
ADD default.conf /etc/nginx/conf.d/default.conf

# aliyun mirror
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak; \
    sed -i 's http://.*.debian.org http://mirrors.aliyun.com g' /etc/apt/sources.list

RUN echo 'root:changeit' | chpasswd
