# SIN351 — Sistemas Operacionais

> **Obrigatória · 5º período** · 60 h (4 h teóricas + 0 h práticas por semana) · 4 créditos · Semestres: I

| | |
|---|---|
| **Pré-requisitos** | [SIN 216](../SIN216-Programa%C3%A7%C3%A3o%20e%20Estruturas%20de%20Dados%20II) |
| **É pré-requisito de** | [SIN 352](../SIN352-Redes%20de%20Computadores), [SIN 142](../SIN142-Sistemas%20Distribu%C3%ADdos), [SIN 440](../SIN440-Avalia%C3%A7%C3%A3o%20de%20Desempenho%20de%20Sistemas%20Computacionais) |
| **Programa analítico** | [Catálogo de Graduação UFV 2026 (PDF)](https://catalogo.ufv.br/pdf.php?campus=crp&disciplina=SIN%20351&ano=2026) |

## Ementa

Princípios básicos de sistemas operacionais. Gerenciamento de processos. Gerência de memória. Sistemas de arquivos. Entrada/Saída.

## Objetivos

Aprender a parte estrutural e comportamental de um sistema operacional. Estruturalmente um sistema operacional é dividido em módulos que podem ser compostos por software e hardware. No que diz respeito ao comportamento, os sistema operacional executa tarefas que visam otimizar, melhorar e facilitar a interação do usuário com o a máquina.

## Conteúdo programático

1. **Princípios básicos de sistemas operacionais** (10 h)
   - Ativação e desativação de procedimentos utilizando pilhas
   - Alocação dinâmica de memória
   - Passagem de parâmetros por valor, referência e nome
   - Estabelecimento de novo ambiente
   - Mecanismo de endereçamento para processamento de parâmetros (técnicas de "displays" e endereço relativo na pilha)
   - Implementação de referências não locais
   - Programas reentrantes
2. **Gerenciamento de processos** (15 h)
   - Processos assincrônicos
   - Utilização de interrupções de máquinas para ativar procedimentos
   - Palavra-de-status de processos e mudança automática de contexto
   - Semáforos
   - Lista de prontos (Ready list). Implementação de um escalonador (Schedule) simples
   - Exemplos clássicos de controle de processos, tais como: deadlook, produtor/consumidor, escritor/leitor, etc
3. **Gerência de memória** (15 h)
   - Características de hierarquia de memórias
   - Memória virtual, paginação, segmentação
   - Mecanismos para eficiência de operação de mapeamento e utilização de memória
   - Proteção de memória
   - Multiprogramação
   - Problemas relacionados com memórias secundárias
4. **Sistemas de arquivos** (10 h)
   - Arquivos e diretórios
   - Implementação do sistema de arquivos
   - Otimização
   - Exemplos de sistemas de arquivos
5. **Entrada/Saída** (10 h)
   - Princípios de hardware de E/S
   - Princípios do software de E/S
   - Camadas do software de E/S
   - Discos
   - Relógios

## Bibliografia

### Básica

- DEITEL, H. M.; CHOFFNES, P. J. Sistemas Operacionais. Editora Pearson Brasil, 1a. edição, 2005.
- SILBERSCHATZ, A. GALVIN, P.B., GAGNE, G.; Sistemas Operacionais com Java. Editora Campus, 1a. edição, 2005.
- TANENBAUM, A. S.; Sistemas Operacionais Modernos. Editora Pearson Brasil, 2a. edição, 2003.

### Complementar

- GALVIN, Silberschatz. Operating system conceps. 4th. ed. Addison-Wesley, Reading, Mass., 1994.
- GUIMARÃES, C. C. Princípios de sistemas operacionais. 3.ed. Rio de Janeiro, Campus, 1983.
- MACHADO, F.B., MAIA, L. P.; Arquitetura de Sistemas Operacionais. Editora LTC, 3ª Edição, 2002.
- OLIVEIRA, R.; TOSCANI, S.; CARISSIMI, A.S.; Sistemas Operacionais. Livro 11 da Série Livros Didáticos do Instituto de Informática da UFRG, 2a. Ed., Editora Sagra Luzzato, 2001.
- SHAW, A. C. The logical design of operating systems. Prentice-Hall, Englewood Cliffs, 1974.
- TANENBAUM, A.S.; WOODHULL, A.S. Sistemas operacionais: projeto e implementação. 2.ed. Bookman, 1999.

## Materiais neste repositório

Ainda não há materiais nesta pasta. Veja [como contribuir](../README.md#como-contribuir).

---

<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV. Gerado por `scripts/catalogo.py`; edite o script, não este arquivo.</sub>
