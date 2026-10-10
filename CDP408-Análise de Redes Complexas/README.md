# CDP408 — Análise de Redes Complexas

> **Optativa** · 60 h (4 h teóricas + 0 h práticas por semana) · 4 créditos · Semestres: I e II

| | |
|---|---|
| **Pré-requisitos** | [MAP 298](../MAP298-Geometria%20Anal%C3%ADtica%20e%20%C3%81lgebra%20Linear) ou [MAP 112](../MAP112-%C3%81lgebra%20Linear) |
| **Programa analítico** | [Catálogo de Graduação UFV 2026 (PDF)](https://catalogo.ufv.br/pdf.php?campus=crp&disciplina=CDP%20408&ano=2026) |

## Ementa

Fundamentos de teoria de grafos e redes complexas. Métricas e medidas de centralidade em redes. Estruturas e propriedades de redes: grau, caminhos, conectividade. Redes livres de escala e mundo pequeno. Modelos de geração de redes: Erdos–Rényi, Barabási–Albert, Watts–Strogatz. Comunidades e detecção de clusters em redes. Redes dinâmicas e evolutivas. Redes sociais, biológicas, tecnológicas e de informação. Análise de redes com Python: NetworkX, igraph. Aplicações em ciência de dados: recomendação, influência, propagação.

## Objetivos

Compreender os fundamentos teóricos de redes complexas Aplicar métricas e medidas de centralidade em redes Implementar algoritmos de detecção de comunidades Analisar propriedades estruturais de redes reais Modelar e simular redes usando modelos teóricos Desenvolver habilidades com ferramentas de análise de redes Aplicar análise de redes em problemas reais de ciência de dados

## Conteúdo programático

1. **Fundamentos de Teoria de Grafos** (8 h)
   - Conceitos básicos: vértices, arestas, grafos direcionados e não direcionados
   - Representações matriciais: matriz de adjacência e incidência
   - Grafos ponderados e bipartidos
   - Caminhos, ciclos e conectividade • Componentes conectados
   - Introdução ao NetworkX
2. **Métricas e Centralidade em Redes** (10 h)
   - Grau e distribuição de grau
   - Distâncias e diâmetro
   - Coeficiente de agrupamento
   - Centralidade: grau, intermediação, proximidade, autovetor
   - PageRank e centralidade de Katz
   - Análise de redes ego-centered
3. **Estruturas e Propriedades de Redes** (10 h)
   - Redes livres de escala
   - Efeito mundo pequeno
   - Rede aleatória Erdos–Rényi
   - Assortatividade e homofilia
   - Redes core-periferia
   - Motivos e subgrafos
   - Análise de resiliência e vulnerabilidade
4. **Modelos de Redes Complexas** (10 h)
   - Modelo Barabási–Albert (preferencial attachment)
   - Modelo Watts–Strogatz (mundo pequeno)
   - Modelos baseados em configuração
   - Redes hierárquicas
   - Modelos de redes sociais
   - Validação de modelos
5. **Detecção de Comunidades** (12 h)
   - Algoritmos de detecção de comunidades
   - Modularidade e qualidade de particionamento
   - Louvain method
   - Girvan-Newman
   - Label propagation
   - Comunidades sobrepostas
   - Avaliação de comunidades detectadas
6. **Aplicações e Projeto Final** (10 h)
   - Redes sociais online
   - Redes de citações científicas
   - Redes biológicas e metabólicas
   - Redes de transporte e infraestrutura
   - Sistemas de recomendação baseados em rede
   - Projeto aplicado completo

## Bibliografia

### Básica

- BARABÁSI, Albert-László. Network Science. Cambridge: Cambridge University Press, 2016.
- LATORA, Vito; NICOSIA, Vincenzo; RUSSO, Giovanni. Complex Networks: Principles, Methods and Applications. Cambridge: Cambridge University Press, 2017.
- ZINOVIEV, Dmitry. Complex Network Analysis in Python: Recognize – Construct – Visualize – Analyze – Interpret. 1. ed. Raleigh: Pragmatic Bookshelf, 2018.
- EASLEY, D.; KLEINBERG, J. Networks, Crowds, and Markets: Reasoning About a Highly Connected World. Cambridge: Cambridge University Press, 2010.
- NICOLETTI, Maria do Carmo; HRUSCHKA JÚNIOR, Estevam R. Fundamentos da Teoria dos Grafos para Computação. 3. ed. Rio de Janeiro: LTC, 2017.
- NETTO, Paulo Oswaldo Boaventura; JURKIEWICZ, Samuel. Grafos: Introdução e Prática. 2. ed. São Paulo: Blucher, 2017.

### Complementar

- ANGELIS, Andre F. de. Redes Complexas como Infraestrutura de Processamento Distribuído: Modelos e Simulações. Saarbrücken: Novas Edições Acadêmicas, 2020.
- KEJRIWAL, Mayank; KNOBLOCK, Craig A.; SZEKELY, Pedro. Knowledge Graphs: Fundamentals, Techniques, and Applications. Cambridge: MIT Press, 2021.

## Referências úteis

- [Network Science (Albert-László Barabási)](https://networksciencebook.com/) — livro aberto e interativo; em inglês
- [NetworkX](https://networkx.org/documentation/stable/) — análise de redes em Python; em inglês
- [Gephi](https://gephi.org/) — visualização e análise de redes

---

<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV; referências úteis em `dados/referencias.json`. Tem material ou indicação desta disciplina? [Contribua](../README.md#como-contribuir). Gerado por `scripts/catalogo.py`; edite o script ou os dados, não este arquivo.</sub>
