# SIN252 — Arquitetura de Computadores

> **Obrigatória · 4º período** · 60 h (4 h teóricas + 0 h práticas por semana) · 4 créditos · Semestres: II

| | |
|---|---|
| **Pré-requisitos** | [SIN 251](../SIN251-Organiza%C3%A7%C3%A3o%20de%20Computadores) |
| **Programa analítico** | [Catálogo de Graduação UFV 2026 (PDF)](https://catalogo.ufv.br/pdf.php?campus=crp&disciplina=SIN%20252&ano=2026) |

## Ementa

Conceito de arquitetura de computadores. Conjunto de instruções e programação em Assembly. Avaliação de desempenho. O caminho de dados. Pipelining. Hierarquia de memórias. Sistemas de E/S. Tópicos em arquitetura de computadores.

## Objetivos

Compreender como os programas escritos em uma linguagem de alto nível, como C ou Java, são traduzidos para a linguagem de máquina e como o hardware executa os programas resultantes. Entender o que é a interface entre o hardware e o software, o como o software instrui o hardware a realizar as funções necessárias. Compreender o que determina o desempenho de um programa e como um programador pode melhorar o desempenho. Conhecer quais técnicas podem ser utilizadas pelos projetistas de hardware para melhorar o desempenho

## Conteúdo programático

1. **Conceito de arquitetura de computadores** (4 h)
   - Abstração em um Sistema de Computação
   - Hardware / software
   - Risc vs. Cisc
2. **Conjunto de instruções e programação em Assembly** (16 h)
   - Arquitetura do Conjunto de Instruções
   - Conjunto de Instruções e assembly do MIPS 32
   - Instruções lógicas e aritméticas
   - Instruções de movimentação de dados
   - Instruções de desvios
   - Assembly do MIPS 32
   - Funções em Assembly do MIPS
     - Conjunto de Instruções e linguagem assembly de arq. x86
3. **Avaliação de desempenho** (8 h)
   - Definindo desempenho
   - Vazão VS. Tempo de resposta
   - Medidas de desempenho considerando o clock
   - Ciclos de clock por instrução (CPI)
   - Equação do desempenho
   - Fatores que influenciam no desempenho
   - Otimização do desempenho
     - Comparação de desempenho
4. **O caminho de dados** (8 h)
   - Conceitos de caminho de dados e controle (CPU)
   - Caminho de dados e Controle do MIPS Monociclo
   - Caminho de dados e Controle do MIPS Multiciclo
   - Exemplo de um caminho de dados e controle x86
5. **Pipelining** (8 h)
   - Aumentando o desempenho com pipelining
   - Hazards
   - Hazards estruturais e soluções
   - Hazards de Dados; Stalls e encaminhamento
   - Hazards de Controle; Previsão de desvios (estático e dinâmico)
   - Avaliação de desempenho em arquiteturas pipelining
   - Superescalar
     - Pipelining em arq. X86
6. **Hierarquia de memórias** (6 h)
   - Hierarquia de memórias
   - Memória cachê
   - Mapeamento direto
   - Mapeamento associativo
   - Tratando falhas
   - Memória virtual
   - Segmentação
     - Tabela de páginas
     - TLB
   - Tratamento de falhas
7. **Sistemas de E/S** (6 h)
   - Barramentos
   - DMA
   - Tecnologias de armazenamento
8. **Tópicos em arquitetura de computadores** (4 h)
   - Máquinas paralelas: Multiprocessadores e vetoriais
   - Redes de interconexão
   - Arquiteturas reconfiguráveis (FPGAs)

## Bibliografia

### Básica

- HENNESSY, J.L.; PATTERSON, D.A. Arquitetura de computadores: uma abordagem quantitativa. 4. ed. Rio de Janeiro: Elsevier, 2008.
- PATTERSON, D.A.; HENNESSY, J.L. Organização e Arquitetura de computadores: a interface hardware/software. 3. ed. Rio de Janeiro: Elsevier, 2005.
- STALLINGS, W. Arquitetura e organização de computadores: projeto para o desempenho. 5. ed. São Paulo: Prentice Hall, 2002.

### Complementar

- DÁMORE, R. VHDL - Descrição e Síntese de Circuitos Digitais. LTC, 2005.
- HEURING, V.P.; MURDOCCA, M.J. Introdução a Arquitetura de Computadores. 1.ed. Campus, 2001.
- MANO, M.M.; KIME, C.R. Logic and computer design fundamentals. 4. ed. Prentice Hall, 2007.
- MONTEIRO, M.A. Introdução à organização de computadores. 5. ed. Rio de Janeiro: LTC, 2007.
- TANENBAUM, A.S. Organização estruturada de computadores. 5. ed. São Paulo: Prentice Hall, 2007.
- TOCCI, R.; WIDMER, N.S.; MOSS, G. Sistemas digitais: princípios e aplicações. 10. ed. Prentice Hall, 2007.
- WEBER, R.F. Fundamentos De Arquitetura de Computadores. 3. ed. Bookman, 2008.

## Materiais neste repositório

Ainda não há materiais nesta pasta. Veja [como contribuir](../README.md#como-contribuir).

---

<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV. Gerado por `scripts/catalogo.py`; edite o script, não este arquivo.</sub>
