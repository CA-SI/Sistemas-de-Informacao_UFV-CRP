# CDP200 — Big Data I

> **Optativa** · 60 h (4 h teóricas + 0 h práticas por semana) · 4 créditos · Semestres: I e II

| | |
|---|---|
| **Pré-requisitos** | [SIN 216](../SIN216-Programa%C3%A7%C3%A3o%20e%20Estruturas%20de%20Dados%20II) |
| **Programa analítico** | [Catálogo de Graduação UFV 2026 (PDF)](https://catalogo.ufv.br/pdf.php?campus=crp&disciplina=CDP%20200&ano=2026) |

## Ementa

Fundamentos de Big Data. Arquiteturas e ecossistema Hadoop. Sistema de arquivos HDFS. Modelo de programação MapReduce. Processamento distribuído com Apache Spark. Spark RDD e DataFrames. Otimização de consultas em grandes volumes de dados. Conceitos de data lakes e data warehouses. NoSQL: bancos de dados chave-valor, documentais, colunares e de grafos. Técnicas de ingestão e processamento de dados em streaming. Introdução a ferramentas de orquestração de pipelines.

## Objetivos

Compreender os fundamentos de Big Data e seus desafios Dominar o ecossistema Hadoop e suas componentes Implementar algoritmos usando o modelo MapReduce Desenvolver aplicações com Apache Spark Conhecer e aplicar bancos de dados NoSQL Projetar pipelines de ingestão e processamento de dados Desenvolver habilidades para processamento distribuído

## Conteúdo programático

1. **Introdução a Big Data** (8 h)
   - Conceitos fundamentais: Volume, Velocidade, Variedade, Veracidade
   - Arquiteturas de Big Data
   - Casos de uso e aplicações
   - Desafios tecnológicos
   - Ecossistema Hadoop
   - Computação distribuída vs paralela
2. **Hadoop e HDFS** (10 h)
   - Arquitetura Hadoop
   - Hadoop Distributed File System (HDFS)
   - NameNode e DataNodes
   - Replicação e tolerância a falhas
   - Comandos HDFS
   - YARN e gerenciamento de recursos
   - Monitoramento do cluster
3. **Modelo MapReduce** (10 h)
   - Fundamentos do MapReduce
   - Mappers e Reducers
   - Shuffle e Sort
   - Otimização de jobs MapReduce
   - Implementação de algoritmos clássicos
   - MapReduce vs alternativas modernas
4. **Apache Spark** (12 h)
   - Arquitetura do Spark
   - Resilient Distributed Datasets (RDDs)
   - Transformações e ações
   - Spark DataFrames e Datasets
   - Spark SQL
   - Otimização com Catalyst Optimizer
5. **Bancos de Dados NoSQL** (10 h)
   - Teorema CAP
   - Modelos de dados: chave-valor, documento, colunar, grafos
   - Cassandra e HBase
   - MongoDB
   - Redis
   - Neo4j
   - Casos de aplicação
6. **Ingestão e Processamento Básico** (10 h)
   - Ferramentas de ingestão: Sqoop, Flume
   - Conceitos de Data Lakes
   - Introdução ao processamento streaming
   - Projeto prático integrador
   - Apresentação de resultados

## Bibliografia

### Básica

- WHITE, Tom. Hadoop: The Definitive Guide. 4. ed. Sebastopol: O'Reilly Media, 2015.
- AMARAL, Fernando. Introdução à Ciência de Dados. 1. ed. Rio de Janeiro: Alta Books, 2016. 320 p. ISBN 978-8576089346.
- ACHARYA, S., CHELLAPPAN, S., "Big Data Analytics" Wiley 2015.

### Complementar

- HAN, Jiawei; KAMBER, Micheline; PEI, Jian. Data Mining: Concepts and Techniques. 3. ed. Waltham: Morgan Kaufmann, 2012.
- SADALAGE, Pramod J.; FOWLER, Martin. NoSQL Essencial: Um Guia Conciso para o Mundo Emergente da Persistência Poliglota. São Paulo: Novatec Editora, 2013. 216 p. ISBN 978-85-7522-338-3.
- DAMJI, Jules S.; WENIG, Brooke; DAS, Tathagata; LEE, Denny. Learning Spark: Lightning-Fast Data Analytics. 2. ed. Sebastopol: O’Reilly Media, 2020. 397 p. ISBN 978-1492050049.
- INMON, W. H. Building the Data Warehouse. 4. ed. Hoboken: Wiley, 2005.
- NETTO, Amílcar; MACIEL, Francisco. Python para Data Science: e Machine Learning Descomplicado. 1. ed. Rio de Janeiro: Alta Books, 2021.

## Materiais neste repositório

Ainda não há materiais nesta pasta. Veja [como contribuir](../README.md#como-contribuir).

---

<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV. Gerado por `scripts/catalogo.py`; edite o script, não este arquivo.</sub>
