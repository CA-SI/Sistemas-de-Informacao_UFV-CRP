# 002 — Guias do curso

## Contexto

As pastas das disciplinas respondem "o que se estuda em cada disciplina". Faltam orientações transversais: como a
matriz funciona, como é o TCC, o que conta como extensão e atividade complementar, como escolher optativas e o que
muda para quem veio de uma matriz anterior. O Guia CASI tem o mesmo formato de guia (Markdown com fontes), e o site
[disciplinas.casi.org.br](https://github.com/CA-SI/disciplinas.casi.org.br) publica este repositório.

## Requisitos

1. Cada guia é um arquivo `guias/<slug>.md` (slug em minúsculas, com hífens), com frontmatter YAML e corpo Markdown.
2. Frontmatter (contrato abaixo) com fontes obrigatórias: todo fato citado vem de uma fonte listada.
3. Links para disciplinas apontam para a pasta da disciplina (`../SIN488-Trabalho de Conclusão de Curso I/`), entre
   `<` e `>` por causa dos espaços. Assim funcionam no GitHub e o site os converte em páginas de disciplina.
4. `guias/README.md` lista os guias.
5. Só informação verificável. Equivalências e regras que dependem da coordenação são indicadas como tal.

## Contrato do frontmatter

Este repositório é o dono do formato; o site só o consome.

```yaml
titulo: Trabalho de Conclusão de Curso      # obrigatório
resumo: Até 160 caracteres.                 # obrigatório
icone: graduation-cap                       # nome de ícone Lucide em kebab-case
ordem: 2                                    # inteiro; ordem de exibição
atualizado_em: 2026-10-10                   # AAAA-MM-DD
fontes:                                     # ao menos uma
  - titulo: Programa analítico SIN 488
    url: https://catalogo.ufv.br/...
```

## Critérios de aceite

- Cinco guias iniciais: matriz, TCC, extensão e atividades complementares, optativas, matrizes anteriores.
- Todo link relativo aponta para pasta ou arquivo existente neste repositório (o build do site falha se não apontar).

## Fora de escopo

- Regulamentos internos que não estão publicados (os guias apontam para a coordenação).
