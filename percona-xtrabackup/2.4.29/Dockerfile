FROM alpine AS wget
ARG TARGETARCH
ENV OS_ARCH="${TARGETARCH:-amd64}"
RUN wget -O /usr/bin/mc https://dl.min.io/client/mc/release/linux-${OS_ARCH}/mc

FROM bitnami/percona-xtrabackup:2.4.29
COPY --from=wget --chmod=0755 /usr/bin/mc /usr/bin/mc