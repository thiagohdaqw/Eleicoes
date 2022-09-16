# Instalação
## Kafka ElasticSearch Connector
- copie as libs de `kafka-libs` para `$KAFKA_HOME/libs`
```
$ cp kafka-libs/* $KAFKA_HOME/libs
```

- copie os arquivos de configuracao para o Kafka
```
$ cp config/kafka/* $KAFKA_HOME/config/
```

- Desative a autenticação do elasticsearch setando para `false` as chaves `xpack.security.enabled` e `xpack.security.enrollment.enabled` em `$ELASTICSEARCH_HOME/config/elastisearch.yml`
