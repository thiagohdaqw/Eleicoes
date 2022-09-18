# Pre-requisitos
- [Apache Spark](https://spark.apache.org/downloads.html)
- [Apache Kafka](https://kafka.apache.org/downloads)
- [Elasticsearch](https://www.elastic.co/pt/downloads/elasticsearch)
- [Kibana](https://www.elastic.co/pt/downloads/kibana)
- [Python](https://www.python.org/downloads/)

# Screenshots
- ...

# Instalação
## 1. Instale as dependencias
```
$ pip install -r requirements.txt
```
## 2. Kafka ElasticSearch Connector
- copie as libs de `kafka-libs` para `$KAFKA_HOME/libs`
```
$ mkdir $KAFKA_HOME/libs
$ cp kafka-libs/* $KAFKA_HOME/libs
```

- copie os arquivos de configuracao para o Kafka
```
$ cp config/kafka/* $KAFKA_HOME/config/
```
## 3. Configurações de Ambiente
- Configure o token de autenticação do twitter na variavel de ambiente `TWITTER_BEARER_TOKEN`
- Insira as credenciais do Elasticsearch em `$KAFKA_HOME/config/elasticsearch-connect.properties` nas chaves `connection.username` e `connection.password` ou desative a autenticação do elasticsearch setando para `false` as chaves `xpack.security.enabled` e `xpack.security.enrollment.enabled` em `$ELASTICSEARCH_HOME/config/elastisearch.yml`
- Configure a url do Spark master na varivel `SPARK_MASTER` e do Kafka na variavel `KAFKA_SERVER` como variaveis de ambiente, o `.env.example` mostra exemplos.
- É recomendado limitar a quantidade máxima de memoria ram do elasticsearch, é possivel realizar isso no arquivo `$ELASTICSEARCH_HOME/config/jvm.options` nas chaves `-Xms` e `-Xmx`.

# Uso
## 1. Inicie o ambiente
```
# KAFKA
$ $KAFKA_HOME/bin/zookeeper-server-start.sh -daemon config/zookeeper.properties          
$ $KAFKA_HOME/bin/kafka-server-start.sh -daemon config/server.properties

# SPARK
$ $SPARK_HOME/sbin/start-all.sh

# Elasticsearch e Kibana
$ $ELASTISEARCH_HOME/bin/elasticsearch
$ $KIBANA_HOME/bin/kibana
```

## 2. Kibana
- Importe o `base_dados.ndjson` na pagina de `Saved Objects`do Kibana.
- Va para a seção de visualização e visualize o dashboard.

## 3. Predição e Contagem de Palavras
- Inicie os Jupyter Notebooks `predict.ipynb` e `wordCount.ipynb` até a seção de `Sink`.

# Referências
- Spark Streaming: https://spark.apache.org/docs/latest/streaming-programming-guide.html
- MLlib: https://spark.apache.org/mllib/
- Tweepy: https://docs.tweepy.org/en/stable/
- Dataset
    - Stopwords: https://github.com/stopwords-iso/stopwords-pt/blob/master/stopwords-pt.txt
    - Palavras Positivas:
        - https://www.dicio.com.br/palavras-positivas/
        - https://www.42frases.com.br/frases-positivas-curtas/
        - https://www.pensador.com/frases_positivas/
        - https://www.educlub.com.br/lista-de-palavras-positivas-para-aumentar-a-autoestima/
    - Palavras Negativas:
        - https://aprenderpalavras.com/lista-de-palavroes-xingamentos-e-girias/
        - https://kiwiask.com/ola-alguem-pode-me-dar-uma-lista-com-50-palavras-negativas-e-50-palavras-positivas-preciso-para-hoje/
        - https://share-danielfeau.com/pt/a-lista-%C3%BAtil-do-escritor-de-111-adjetivos-negativos-para-descrever-uma-pessoa/
        - https://br.guiainfantil.com/materias/educacao/comportamentofrases-negativas-que-desmotivam-as-criancas/
        - https://segredosdomundo.r7.com/xingamentos-brasil/
        - https://pt.lambdageeks.com/negative-sentence-examples/