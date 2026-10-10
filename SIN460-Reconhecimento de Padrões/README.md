# SIN460 — Reconhecimento de Padrões

> **Optativa** · 60 h (4 h teóricas + 0 h práticas por semana) · 4 créditos · Semestres: I e II

| | |
|---|---|
| **Pré-requisitos** | [SIN 215](../SIN215-Programa%C3%A7%C3%A3o%20e%20Estruturas%20de%20Dados%20I) e ([ESP 105](../ESP105-Inicia%C3%A7%C3%A3o%20%C3%A0%20Estat%C3%ADstica) ou ESP 224) |
| **Obrigatória também em** | Ciência de Dados e Inteligência Artificial (7º) |
| **Programa analítico** | [Catálogo de Graduação UFV 2026 (PDF)](https://catalogo.ufv.br/pdf.php?campus=crp&disciplina=SIN%20460&ano=2026) |

## Ementa

Introdução. Dados. Explorando os dados. Introdução do problema de classificação. Algoritmos de classificação. Análise de grupos.

## Objetivos

Apresentar aos alunos todos os conceitos e técnicas de reconhecimento de padrões.

## Conteúdo programático

1. **Introdução** (4 h)
   - O que é Reconhecimento de Padrões?
   - Desafios
   - Tarefas de Reconhecimento de Padrões
2. **Dados** (8 h)
   - Tipos de dados
   - Qualidade dos dados
   - Pré-processamento de dados
   - Agregação e amostragem
   - Seleção de atributos e redução da dimensionalidade
   - Medidas de semelhança e diferença
3. **Introdução do problema de classificação** (18 h)
   - Noções preliminares
   - Abordagem Geral
   - Árvores de decisão
   - Como uma árvore de decisão funciona
   - Construção da árvore de decisão
   - Aprimoramento
   - Algoritmo de indução de árvore de decisão
     - Overfitting
     - Problemas com ruídos
   - Falta de amostras
     - Comparação múltipla
     - Lidando com Overfitting
     - Avaliando o desempenho
   - Houldout
   - Sub-amostragem aleatória
   - Validação cruzada
   - Bootstrap
   - Métodos para comparar classificadores
4. **Algoritmos de classificação** (18 h)
   - Classificador do vizinho mais próximo
   - Algoritmo
   - Principais características
   - Classificadores Bayesianos
   - Teorema de Bayes
   - Usando o Teorema de Bayes para classificação
   - Classificador de Bayes simples
     - Redes Neurais Artificiais (ANN)
     - Perceptron
   - Treinamento
     - Aprendizado
     - ANN multicamadas (MLP)
     - Características de ANN
5. **Análise de grupos** (12 h)
   - Visão geral
   - O que é análise de grupos?
   - Diferentes tipos de grupos
   - Diferentes tipos de agrupamentos
   - K-médias
   - O algoritmo k-médias básico
   - Dividindo k-médias
     - Pontos fortes e fracos
     - K-médias como problema de otimização
   - Determinando o número de grupos
     - Agrupamento hierárquico
     - Principais conceitos
     - Algoritmo hierárquico aglomerativo
   - Medidas de similaridade entre grupos
   - Questões chave no agrupamento hierárquico
   - Pontos fortes e fracos

## Bibliografia

### Básica

- PINHEIRO, C.A.R. Inteligência Analítica - Mineração de Dados e Descoberta de Conhecimento. 1ª ed. Ciência Moderna, 2008.
- SILVA, I.N., SPATTI, D.H. e FLAUZINO, R. A. Neurais Artificiais para engenharia e ciências aplicadas: curso prático. Edição 1. Artliber, 2010.
- STEINBACH, M.; KUMAR, V.; TAN, P. Introdução ao Data Mining (Mineração de Dados). Edição 1. Ciência Moderna, 2009.

### Complementar

- AGUIAR, O.J.H. Inteligência Computacional Aplicada à Administração, Economia e Engenharia em Matlab. Edição 1. Thomson, 2007.
- Duda, R.O.; Hart, P.E. and Stork, D.G. Pattern Classification. Edição 2. Wiley-Interscience, 2000.
- LINDEN, R. Algoritmos Genéticos. Edição 2. Brasport, 2008.
- MITCHELL, T. Machine Learning, Edição 1. McGraw Hill, 1997.
- Theodoridis, S.; Koutroumbas, K. Pattern Recognition. Edição 1. Elsevier, 2008.

## Referências úteis

- [An Introduction to Statistical Learning](https://www.statlearning.com/) — livro aberto com versões em R e Python; em inglês
- [Pattern Recognition and Machine Learning (Bishop)](https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/) — livro disponível gratuitamente em PDF; em inglês
- [Guia do usuário do scikit-learn](https://scikit-learn.org/stable/user_guide.html) — em inglês
- [Kaggle Learn](https://www.kaggle.com/learn) — microcursos práticos e bases de dados; em inglês

---

<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV; referências úteis em `dados/referencias.json`. Tem material ou indicação desta disciplina? [Contribua](../README.md#como-contribuir). Gerado por `scripts/catalogo.py`; edite o script ou os dados, não este arquivo.</sub>
