FROM aquasec/trivy:0.44.1 AS builder
RUN trivy image --download-db-only; \
    trivy image --download-java-db-only; \
    tar -czf /tmp/trivy-db.tgz /root/.cache/trivy/db /root/.cache/trivy/java-db

FROM busybox:1.32
COPY --from=builder /tmp/trivy-db.tgz /opt/trivy-db.tgz
