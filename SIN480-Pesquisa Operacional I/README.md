# SIN480 — Pesquisa Operacional I

> **Obrigatória · 6º período** · 60 h (4 h teóricas + 0 h práticas por semana) · 4 créditos · Semestres: II

| | |
|---|---|
| **Pré-requisitos** | [SIN 111](../SIN111-Fundamentos%20de%20Programa%C3%A7%C3%A3o) |
| **É pré-requisito de** | [SIN 481](../SIN481-Pesquisa%20Operacional%20II) |
| **Obrigatória também em** | Engenharia de Produção (4º) |
| **Programa analítico** | [Catálogo de Graduação UFV 2026 (PDF)](https://catalogo.ufv.br/pdf.php?campus=crp&disciplina=SIN%20480&ano=2026) |

## Ementa

Modelagem matemática de problemas gerenciais. Introdução à programação linear. Implementação do Método Simplex. Problemas de transporte. Problemas de alocação ou designação. Minimização em redes. Caminho mínimo. Fluxo máximo. Programação não-linear.

## Objetivos

Apresentar os conceitos básicos de Pesquisa Operacional: programação linear, inteira e modelos de rede. Proporcionando ao aluno condições de entendimento e desenvolvimento, por meio de raciocínio lógico, de modelos matemáticos que podem ser aplicados na resolução de problemas de várias áreas do conhecimento. Além disso, o aluno será capaz de associar métodos de resolução a problemas de otimização de acordo com suas características, e fazer uso de software de otimização na resolução de problemas.

## Conteúdo programático

1. **Modelagem matemática de problemas gerenciais** (2 h)
   - O modelo no Processo de decisão
   - Introdução a Pesquisa Operacional
   - O que são variáveis de decisão
   - Etapas do P.O
   - Modelagem do problema
   - Tipos de Modelo
2. **Introdução à programação linear** (8 h)
   - Modelando problemas utilizando PL
   - Interpretação Geométrica
   - Operações elementares
   - Métodos para a solução de desigualdades
3. **Implementação do Método Simplex** (12 h)
   - Escolha da variável que entra na Base
   - Escolha da variável que sai da Base
   - Como fazer o pivoteamento
   - Como saber se a solução é ótima
   - O problema da solução ilimitada
   - O problema das soluções múltiplas
   - Problemas de minimização
     - Implementação do método simplex de duas fases
   - Simplex revisado
   - Dualidade
     - Introdução
     - Método dual simplex
4. **Problemas de transporte** (6 h)
   - Método de Vogel
   - Casos Especiais
5. **Problemas de alocação ou designação** (6 h)
   - Método Húngaro
   - Casos Especiais
6. **Minimização em redes** (6 h)
   - Algoritmos Kruskal e Prim
7. **Caminho mínimo** (6 h)
   - Dijkstra
   - Algoritmo de Ford, Bellman e Moore
   - Caminho mais confiável
   - Algoritmo de Floyd
   - Algoritmo de Dantzig
8. **Fluxo máximo** (8 h)
   - Algoritmos de aumento de fluxo
   - Rede residual
   - Algoritmo de Ford/Fulkerson
   - Algoritmo de Dinic
9. **Programação não-linear** (6 h)
   - Aplicações
   - Solução gráfica
   - Método de lagrange

## Bibliografia

### Básica

- ANDRADE, E.L. Introdução à Pesquisa Operacional. Rio de Janeiro: LTC, 1998.
- CAIXETA FILHO, José Vicente. Pesquisa Operacional. São Paulo: Atlas, 2001.
- FITZSIMMONS, A.J. e FITZSIMMONS, M.J. Administração de serviços. 2ª ed. Porto Alegre: Bookman, 2000.

### Complementar

- BREGALDA, P.F.; OLIVEIRA, A.A.F. e BORNSTEIN, C.T. Introdução à programação linear. 3.ed. Rio de Janeiro: Campus, 1988.
- BRONSON, Richard. Pesquisa Operacional. Editora McGraw-Hill. 1994.
- HILLIER, F.S. e LIEBERMAN, G.J. Introdução à pesquisa operacional. Rio de Janeiro: Campus, 1988.
- SHAMBLIN, James E. Pesquisa Operacional. São Paulo: Atlas, 1989.
- WAGNER, Harvey M. Pesquisa operacional. 2ª ed. Rio de Janeiro: Prentice-Hall do Brasil, 1986. 851p.
- MACULAN, N. and Fampa, M.H.C. Otimização Linear. Editora EdUnb, 2006

## Referências úteis

- [Google OR-Tools](https://developers.google.com/optimization) — programação linear, inteira e roteamento; em inglês
- [PuLP](https://coin-or.github.io/pulp/) — modelagem de programação linear em Python; em inglês
- [MIT 15.053 — Optimization Methods in Management Science](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/) — MIT OpenCourseWare; em inglês
- [GLPK — GNU Linear Programming Kit](https://www.gnu.org/software/glpk/) — solver livre

---

<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV; referências úteis em `dados/referencias.json`. Tem material ou indicação desta disciplina? [Contribua](../README.md#como-contribuir). Gerado por `scripts/catalogo.py`; edite o script ou os dados, não este arquivo.</sub>
