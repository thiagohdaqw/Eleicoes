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

# Referências
- Dataset
    - Stopwords: https://github.com/stopwords-iso/stopwords-pt/blob/master/stopwords-pt.txt
    - Palavras Positivas: 
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