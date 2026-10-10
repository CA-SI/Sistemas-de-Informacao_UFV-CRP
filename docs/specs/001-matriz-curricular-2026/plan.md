# Plano — 001 Matriz curricular 2026

## Fontes

- Lista de disciplinas por período: `interno.php?ano=2026&curso=SIP&campus=crp&periodo=N`
  (`N` = 1–8; `0` = optativas).
- Programa analítico: `pdf.php?campus=crp&disciplina=XXX%20NNN&ano=AAAA`, convertido com
  `pdftotext -layout` (poppler).
- Disciplinas de matrizes anteriores: o mesmo PDF, buscando do catálogo mais recente para o mais
  antigo até encontrar.

## Arquitetura

`scripts/catalogo.py` com quatro subcomandos:

- `baixar`: lê a matriz, baixa e interpreta os PDFs e grava `dados/catalogo-2026.json`.
- `organizar`: compara as pastas com o catálogo e lista (ou, com `--aplicar`, executa) os `git mv` e `mkdir`.
- `gerar`: lê o JSON e escreve o `README.md` de cada pasta, e o bloco entre
  `<!-- MATRIZ:INICIO -->` e `<!-- MATRIZ:FIM -->` no README da raiz.
- `verificar`: testa os links de `dados/referencias.json`.

`dados/referencias.json` é curadoria manual (`{código: [{titulo, url, nota}]}`), separada do JSON do catálogo para
não ser sobrescrita por `baixar`.

A lista de disciplinas de matrizes anteriores e as correspondências ficam numa tabela no próprio
script (`LEGADO`), por serem curadoria e não dado do catálogo.

## Decisões

- Nome da pasta = `CÓDIGO-Nome`, sem `/` e `:` (inválidos ou problemáticos em sistemas de arquivos).
- Na bibliografia, uma referência começa na linha que traz o nº de exemplares na coluna da direita; as demais
  linhas são continuação (anos no fim da linha não abrem referência nova).
- O catálogo declara 2700 h obrigatórias, mas a soma da tabela dá 2640 h; o README mostra os dois valores.
- O README lista os arquivos já existentes na pasta, para que os materiais apareçam no GitHub.
- Os arquivos `keep` vazios ficam redundantes quando a pasta ganha README; a remoção só acontece
  com aprovação explícita.
