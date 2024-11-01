FROM docker.elastic.co/elasticsearch/elasticsearch:7.16.2

ARG ELASTICSEARCH_VERSION=7.16.2

COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

RUN curl -sSLo "/tmp/elasticsearch-analysis-ik-${ELASTICSEARCH_VERSION}.zip" \
        "https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v${ELASTICSEARCH_VERSION}/elasticsearch-analysis-ik-${ELASTICSEARCH_VERSION}.zip"; \
    bin/elasticsearch-plugin install --batch file:///tmp/elasticsearch-analysis-ik-${ELASTICSEARCH_VERSION}.zip; \
    rm -rf /tmp/*;

USER 1000