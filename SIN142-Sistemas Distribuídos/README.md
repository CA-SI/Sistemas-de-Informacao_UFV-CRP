# SIN142 — Sistemas Distribuídos

> **Obrigatória · 7º período** · 60 h (4 h teóricas + 0 h práticas por semana) · 4 créditos · Semestres: I

| | |
|---|---|
| **Pré-requisitos** | [SIN 351](../SIN351-Sistemas%20Operacionais) |
| **É pré-requisito de** | [SIN 441](../SIN441-T%C3%B3picos%20em%20Sistemas%20Distribu%C3%ADdos) |
| **Programa analítico** | [Catálogo de Graduação UFV 2026 (PDF)](https://catalogo.ufv.br/pdf.php?campus=crp&disciplina=SIN%20142&ano=2026) |

## Ementa

Conceitos fundamentais de sistemas distribuídos. Comunicação. Sincronização. Consistência e replicação. Tolerância a falhas. Segurança. Sistemas de arquivos distribuídos e sistemas de nomes. Memória compartilhada e distribuída. Transações e controle de concorrência.

## Objetivos

Apresentar aos alunos os conceitos relacionados a Sistemas Distribuídos.

## Conteúdo programático

1. **Conceitos fundamentais de sistemas distribuídos** (4 h)
2. **Comunicação entre processos** (8 h)
   - Chamada de procedimento remoto
   - Comunicação orientada a mensagem
   - Comunicação orientada a fluxo
3. **Sincronização** (8 h)
   - Sincronização de relógios
   - Relógios lógicos
   - Exclusão mútua
   - Algoritmos de eleição
4. **Consistência e replicação** (8 h)
   - Modelos de consistência em dados e no cliente
   - Gerenciamento de réplicas
   - Protocolos de consistência
5. **Tolerância a falhas** (8 h)
6. **Segurança** (4 h)
7. **Sistemas de arquivos distribuídos e sistemas de nomes** (6 h)
   - Estudo de casos
8. **Memória compartilhada distribuída** (8 h)
9. **Transações e controle de concorrência** (6 h)

## Bibliografia

### Básica

- COULOURIS, G.; DOLLIMORE, J.; KINBERG, Tim. Sistemas Distribuídos: Conceitos e Projetos. 4a. edição. Bookmann, 2007
- TANENBAUM, Andrew; STEEN, M. Van. Sistemas Distribuídos: Princípios e Paradigmas. 2a edição, Prentice-Hall, 2008.
- KUROSE, James F. ; ROSS, Keith W. Redes de computadores e a Internet : uma abordagem top- down.São Paulo : Pearson Addison Wesley, 2010.

### Complementar

- SOARES, Luiz Fernando G. Redes de computadores: das LANs, MANs e WANs as redes ATM. Rio de Janeiro: Campus, 1995.
- COMER, Douglas E. Interligacao em rede com TCP/IP, volume 1 : principios, protocolos e arquitetura. Rio de Janeiro: Campus, 1998.
- COMER, Douglas E. Interligacao em rede com TCP/IP, volume 2 : projeto, implementação e detalhes internos. Rio de Janeiro: Campus, 1999.
- PETERSON, Larry L. Redes de computadores: uma abordagem de sistemas. Rio de Janeiro, Campus, Elsevier, 2004.
- TANENBAUM, Andrew S. Redes de computadores. Rio de Janeiro, Elsevier, Campus, 2003.

## Referências úteis

- [Distributed Systems, 4ª ed. (van Steen & Tanenbaum)](https://www.distributed-systems.net/index.php/books/ds4/) — livro gratuito para download pessoal; em inglês
- [MIT 6.5840 — Distributed Systems](https://pdos.csail.mit.edu/6.824/) — aulas, artigos e laboratórios em Go; em inglês
- [Raft Consensus Algorithm](https://raft.github.io/) — artigo e visualização do algoritmo de consenso
- [gRPC](https://grpc.io/docs/) — chamadas de procedimento remoto; em inglês

---

<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV; referências úteis em `dados/referencias.json`. Tem material ou indicação desta disciplina? [Contribua](../README.md#como-contribuir). Gerado por `scripts/catalogo.py`; edite o script ou os dados, não este arquivo.</sub>
