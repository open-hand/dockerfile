FROM aquasec/trivy:0.44.1 AS builder
RUN trivy image --download-db-only; \
    trivy image --download-java-db-only; \
    cd /root/.cache/trivy; \
    tar -czf /tmp/trivy-db.tgz db java-db

FROM busybox:1.32
COPY --from=builder /tmp/trivy-db.tgz /opt/trivy-db.tgz
