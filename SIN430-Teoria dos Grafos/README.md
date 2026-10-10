# SIN430 — Teoria dos Grafos

> **Optativa** · 60 h (4 h teóricas + 0 h práticas por semana) · 4 créditos · Semestres: I

| | |
|---|---|
| **Pré-requisitos** | [SIN 216](../SIN216-Programa%C3%A7%C3%A3o%20e%20Estruturas%20de%20Dados%20II) |
| **Obrigatória também em** | Ciência de Dados e Inteligência Artificial (7º) |
| **Programa analítico** | [Catálogo de Graduação UFV 2026 (PDF)](https://catalogo.ufv.br/pdf.php?campus=crp&disciplina=SIN%20430&ano=2026) |

## Ementa

Introdução à Teoria dos Grafos. Conceitos Básicos. Representação de Grafos. Caminhos e Circuitos. Dígrafos. Grafos Valorados. Conectividade, Planaridade e Coloração. Árvores. Busca em Grafos. Fluxos em Redes.

## Objetivos

Proporcionar conhecimentos básicos, teóricos e práticos envolvendo Teoria dos Grafos, suas representações e aplicações. Tornando o aluno apto a resolver problemas básicos envolvendo grafos, compreendendo sua grande importância da área para a Ciência da Computação.

## Conteúdo programático

1. **Introdução à Teoria dos Grafos** (2 h)
   - Motivação
   - Exemplos de aplicação
2. **Conceitos Básicos** (4 h)
   - Definição e notação
   - Subgrafos
   - Grafos completos e bipartidos
   - Isomorfismo de grafos
   - Complemento de um grafo
   - Grafos rotulados e grafos planares
   - Cliques
     - Conjunto Independente de Vértices
     - Cobertura de Vértice
3. **Representação de Grafos** (4 h)
   - Na Matriz de adjacências
   - Listas
4. **Caminhos e Circuitos** (4 h)
   - Caminhos, percurso, trajetos e ciclos de grafos
   - Caminhos e ciclos Hamiltonianos e Eulerianos
   - Grafos conexos e desconexos
   - Distância entre vértices
   - Exclusão e inclusão de arestas
5. **Dígrafos** (4 h)
   - Dígrados fortemente e fracamente conexos
   - Alcançabilidade de vértices
   - Dígrafo acíclico
   - Aplicações
6. **Grafos Valorados** (10 h)
   - Grafos valorados
   - Menor caminho
   - Algoritmo de Djikstra
   - Algoritmo de Bellman-Ford
   - Algoritmo de Floyd-Warshall
7. **Conectividade, Planaridade e Coloração** (6 h)
   - Conectividade de: corte, grafos k-conexos
   - Planaridade de: grafos, planares, fórmulas de Euler
   - Coloração: grafos k-coloríveis, o problema das 4 cores
8. **Árvores** (16 h)
   - Árvore e floresta
   - Árvore geradora
   - Raiz de uma árvore, nível de um vértice, árvores m-ária
   - Árvore geradora de custo mínimo
   - Algoritmos de Prim e Kruskal
9. **Busca em Grafos** (4 h)
   - Algoritmo básico
   - Busca em profundidade e amplitude
10. **Fluxos em Redes** (6 h)
   - Fluxos em redes
   - Cortes
   - Teorema do fluxo máximo

## Bibliografia

### Básica

- DROZEK, A. Estruturas de Dados e Algoritmos em C . São Paulo: Pioneira Thomson Learning, 2002. 579 p.
- GERSTING, J.L. Fundamentos Matemáticos para a Ciência da Computação. 5ª ed. Rio de Janeiro: LTC, 2004. 616 p.
- NETTO, P.O.B. Grafos: Teoria, Modelos e Algoritmos. 4ª ed. São Paulo: Edgard Blücher, 2006. 313 p.

### Complementar

- BONDY, J.A.; MURTY, U.S.R. Graph Theory with Applications. The Macmillan Press LTD, 1977.
- NETTO, P.O.B.; JURKIEWICZ, S. Grafos: Introdução e Prática. 1ª ed. São Paulo: Edgard Blücher, 2009. 176 p.
- SZWARCFITER, J.L. Grafos e algoritmos computacionais. Rio de Janeiro: Campus, 1988. pp. 43-45.
- TENENBAUM, A.M. et al. Estruturas de dados usando C. Makron Books, 1995. 884 p.
- ZIVIANI, N. Projeto de algoritmos: com implementações em Pascal e C. 2ª ed. São Paulo: Pioneira Thomson Learning, 2004. 522 p.

## Referências úteis

- [Algoritmos para Grafos em C (Paulo Feofiloff, IME-USP)](https://www.ime.usp.br/~pf/algoritmos_para_grafos/) — notas de aula em português
- [NetworkX](https://networkx.org/documentation/stable/) — biblioteca Python para grafos; em inglês
- [CP-Algorithms — Graphs](https://cp-algorithms.com/) — algoritmos de grafos com implementação; em inglês
- [VisuAlgo — grafos](https://visualgo.net/en/dfsbfs) — animações de BFS e DFS

---

<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV; referências úteis em `dados/referencias.json`. Tem material ou indicação desta disciplina? [Contribua](../README.md#como-contribuir). Gerado por `scripts/catalogo.py`; edite o script ou os dados, não este arquivo.</sub>
