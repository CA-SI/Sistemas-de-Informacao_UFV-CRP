# SIN352 — Redes de Computadores

> **Obrigatória · 6º período** · 90 h (4 h teóricas + 2 h práticas por semana) · 6 créditos · Semestres: II

| | |
|---|---|
| **Pré-requisitos** | [SIN 351](../SIN351-Sistemas%20Operacionais) |
| **É pré-requisito de** | [SIN 214](../SIN214-Administra%C3%A7%C3%A3o%20a%20Gerenciamento%20de%20Redes), [SIN 452](../SIN452-Redes%20de%20Alto%20Desempenho), [SIN 453](../SIN453-Laborat%C3%B3rio%20de%20Redes) |
| **Programa analítico** | [Catálogo de Graduação UFV 2026 (PDF)](https://catalogo.ufv.br/pdf.php?campus=crp&disciplina=SIN%20352&ano=2026) |

## Ementa

Visão geral de redes de computadores e sistemas distribuídos. Camada física. Camada de enlace de dados. Camada de acesso ao meio. Camada de rede. Camada de transporte. Camada de aplicação. Programação em redes usando Sockets.

## Objetivos

Entende como funciona um rede de computadores tanto física, como virtualmente. A disciplina apresenta a composição em software das camadas de comunicação de protocolos, juntamente com aulas práticas de simulação de rede de computadores.

## Conteúdo programático

1. **Visão geral de redes de computadores e sistemas distribuídos** (4 h)
   - Utilização de redes de computadores. Hardware de rede, software de rede, Modelos de referência OSI e TCP/IP (internet)
2. **Camada física** (4 h)
   - Tipos de meios de transmissão, modulação de sinal, transmissão sem fio, rádio celular, rede pública de telefonia, noções de Redes digitais de serviços integrados de faixa estreita e de faixa larga e de redes ATM (Asynchronous Transfer Mode)
3. **Camada de enlace de dados** (8 h)
   - Formato de quadros, detecção e correção de erros, controle de fluxo, protocolo para-e-espera, protocolos de janela deslizante, correção de erro usando "go-back-n" e retransmissão seletiva, protocolos de enlace usados na Internet
4. **Camada de acesso ao meio** (10 h)
   - Alocação de canais compartilhados, histórico, alocação em redes com topologia de barramento e anel, protocolo para redes sem fio, padrões IEEE para redes locais (Ethernet e Token Ring), pontes, redes de alta velocidade: DQDB (Distributed Queue Dual Bus), FDDI (Fiber Distributed DAta Interface), Fast Ethernet, Gigabit Ethernet e ATM
5. **Camada de rede** (10 h)
   - Protocolos de roteamento: inundação, vetor de distância e baseado no estado do link; noções sobre algoritmos de controle de congestionamento; interconexão de redes; ATM
6. **Camada de transporte** (8 h)
   - Serviço de transporte, estabelecimento e liberação de conexão
   - Controle de fluxo e gerência de buffers, exemplo de um protocolo de transporte simples usando máquina de estado (ou Redes de Petri), protocolo de transporte na internet: TCP (Transmission control protocol) e UDP (User Datagram Protocol)
7. **Camada de aplicação** (10 h)
   - Correio eletrônico, segurança em redes (criptografia), serviço de nomes (DNS Domain Name System), gerência de redes usando SNMP (Simple Network Management Protocol), WWW (World Wide Web), aplicações multimídia e comunicação de grupo
8. **Programação em redes usando Sockets** (6 h)
   - Conceito de sockets, implementação em sistemas Unix, programação usando socket; exemplo de um serviço simples usando o paradigma cliente servidor, serviço usando conexão; serviço sem conexão (datagrama), servidor multi processos
9. **Introdução às redes de computadores** (4 h)
   - Revisão dos modelos OSI e TCP/IP
   - Equipamentos de Redes
   - Encaminhamento IP
   - Introdução ao encaminhamento IP
   - Classes de Endereço
   - Endereços Públicos e Privados
   - Sub-Redes
10. **Camada física** (2 h)
   - Meios de transmissão analógica e digital
   - Chaveamento
11. **A subcamada de acesso ao meio** (4 h)
   - Protocolos de redes locais
   - Redes de Fibra Óptica
12. **WANs e roteadores** (5 h)
   - Introdução às WANs e aos roteadores
   - Configuração de roteadores Cisco
   - Repetidores
   - Pontes e roteadores
13. **Encaminhamento IP** (5 h)
   - Introdução ao Encaminhamento
   - Encaminhamento Estático
   - Encaminhamento Dinâmico com RIP, IGRP, EIGRP e OSPF
14. **Switching** (5 h)
   - Introdução ao Switching
   - Redes Estruturadas com Switches
   - Configuração de Switches Cisco
15. **Redes virtuais - VLANs** (5 h)
   - Introdução às VLANs
   - Configuração de VLANs
   - Encaminhamento entre VLANs

## Bibliografia

### Básica

- COMER, D.E. Computer Networks and internets, Prentice-Hall, 3a edição, 2006.
- KUROSE, J.F.; ROSS, K.W. Redes de Computadores e a Internet. 3ed. Addison-Wesley, 2006.
- TANENBAUM, A.S. Redes de computadores. 3ed., Campus, Rio de Janeiro, 1997.

### Complementar

- COMER, D.E. Interligação em rede com TCP/IP, v.1, Ed. Campus, Rio de Janeiro, 1998
- COMER, D.E. Redes de computadores e internet. Bookman. Ed. 2000.
- DERSLER, F.J. Guia de Conectividade, Editora Campos, 1993.
- DERSLER, F.J. Guia para Interligação de Redes Locais, Editora Campos, 1993.
- SOARES, L.F. et al. Redes de computadores: das Lans, Mans e Wans às redes ATM, Campus, Rio de Janeiro, 1997.

## Materiais neste repositório

- [3929](https://github.com/MatheusRV/Computer-Networks-Course) (submódulo git)

---

<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV. Gerado por `scripts/catalogo.py`; edite o script, não este arquivo.</sub>
