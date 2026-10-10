# 001 — Matriz curricular 2026

## Contexto

O repositório organiza materiais por disciplina, mas as pastas refletiam matrizes antigas
(SIN110, SIN211, SIN498/499, SIN496, CRP199 etc.), tinham nomes errados (SIN390 duplicada,
SIN393 com o nome de SIN392, SIN460 como "Mineração de Dados") e nenhuma pasta tinha README.

A matriz vigente do curso SIP (Campus Rio Paranaíba) está no Catálogo de Graduação UFV 2026:
<https://catalogo.ufv.br/matriz.php?campus=crp&complemento=*&curso=SIP&ano=2026>.

## Requisitos

1. Existe uma pasta `CÓDIGO-Nome oficial` na raiz para cada disciplina obrigatória e optativa da
   matriz 2026.
2. Pastas cujo código ou nome mudou são renomeadas com `git mv`, preservando arquivos e submódulos.
3. Disciplinas que saíram da matriz vão para `Z-Matrizes Anteriores/`, com indicação da disciplina
   correspondente na matriz 2026 quando houver.
4. Toda pasta de disciplina tem um `README.md` com: tipo (obrigatória/optativa/matriz anterior),
   período, carga horária, pré-requisitos, ementa, objetivos, conteúdo programático, bibliografia
   básica e complementar, link para o programa analítico oficial e lista dos materiais da pasta.
5. O conteúdo vem do programa analítico oficial da UFV (sem texto inventado).
6. O README da raiz traz o fluxograma da matriz 2026 com pré-requisitos, o índice por período, as
   optativas e a tabela das disciplinas de matrizes anteriores.
7. A geração é reproduzível por script, para atualizar quando sair um novo catálogo.

## Critérios de aceite

- `python3 scripts/catalogo.py baixar` gera `dados/catalogo-2026.json` a partir do site da UFV.
- `python3 scripts/catalogo.py gerar` (re)gera todos os READMEs sem alterar os materiais.
- Todos os links do README da raiz apontam para pastas existentes.
- Nenhum arquivo de material é perdido (somente `git mv`).

## Fora de escopo

- Curadoria de materiais externos (vídeos, listas, apostilas) por disciplina.
- Equivalências oficiais para aproveitamento de estudos (definidas pela coordenação).
