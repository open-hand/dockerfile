FROM choerodon/cibase:1.0.0-base

# install cgo-related dependencies
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        g++ \
        gcc \
        libc6-dev \
        make \
        pkg-config \
    ; \
    rm -rf /var/lib/apt/lists/*

ENV PATH /usr/local/go/bin:$PATH

ENV GOLANG_VERSION 1.17.6

RUN set -eux; \
    arch="$(dpkg --print-architecture)"; arch="${arch##*-}"; \
    url=; \
    case "$arch" in \
        'amd64') \
            url='https://dl.google.com/go/go1.17.6.linux-amd64.tar.gz'; \
            sha256='231654bbf2dab3d86c1619ce799e77b03d96f9b50770297c8f4dff8836fc8ca2'; \
            ;; \
        'armel') \
            export GOARCH='arm' GOARM='5' GOOS='linux'; \
            ;; \
        'armhf') \
            url='https://dl.google.com/go/go1.17.6.linux-armv6l.tar.gz'; \
            sha256='9ac723e6b41cb7c3651099a09332a8a778b69aa63a5e6baaa47caf0d818e2d6d'; \
            ;; \
        'arm64') \
            url='https://dl.google.com/go/go1.17.6.linux-arm64.tar.gz'; \
            sha256='82c1a033cce9bc1b47073fd6285233133040f0378439f3c4659fe77cc534622a'; \
            ;; \
        'i386') \
            url='https://dl.google.com/go/go1.17.6.linux-386.tar.gz'; \
            sha256='06c50fb0d44bb03dd4ea8795f9448379c5825d2765307b51f66905084c3ba541'; \
            ;; \
        'mips64el') \
            export GOARCH='mips64le' GOOS='linux'; \
            ;; \
        'ppc64el') \
            url='https://dl.google.com/go/go1.17.6.linux-ppc64le.tar.gz'; \
            sha256='adc35c920b8c0253d4dd001f8979e0db4c6111a60cd5e0785a8bee95dba1fcaa'; \
            ;; \
        's390x') \
            url='https://dl.google.com/go/go1.17.6.linux-s390x.tar.gz'; \
            sha256='ccb2d4509db846be7055d1105b28154e72cd43162c4ef79c38a936a3e6f26e1d'; \
            ;; \
        *) echo >&2 "error: unsupported architecture '$arch' (likely packaging update needed)"; exit 1 ;; \
    esac; \
    build=; \
    if [ -z "$url" ]; then \
# https://github.com/golang/go/issues/38536#issuecomment-616897960
        build=1; \
        url='https://dl.google.com/go/go1.17.6.src.tar.gz'; \
        sha256='4dc1bbf3ff61f0c1ff2b19355e6d88151a70126268a47c761477686ef94748c8'; \
        echo >&2; \
        echo >&2 "warning: current architecture ($arch) does not have a compatible Go binary release; will be building from source"; \
        echo >&2; \
    fi; \
    \
    wget -O go.tgz.asc "$url.asc"; \
    wget -O go.tgz "$url" --progress=dot:giga; \
    echo "$sha256 *go.tgz" | sha256sum -c -; \
    \
# https://github.com/golang/go/issues/14739#issuecomment-324767697
    GNUPGHOME="$(mktemp -d)"; export GNUPGHOME; \
    rm -rf "$GNUPGHOME" go.tgz.asc; \
    \
    tar -C /usr/local -xzf go.tgz; \
    rm go.tgz; \
    \
    go version

ENV GOPATH /go
ENV PATH $GOPATH/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH

RUN go get -u github.com/jstemmer/go-junit-report