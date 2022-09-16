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

- copie os arquivos de configuração para o elasticsearch, isso irá desativar a autenticação
```
$ cp config/elasticsearch/* $ELASTICSEARCH_HOME/config
```
