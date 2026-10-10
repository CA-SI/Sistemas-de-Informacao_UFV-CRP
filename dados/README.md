# Dados

| Arquivo | Conteúdo | Origem |
|---|---|---|
| [`catalogo-2026.json`](catalogo-2026.json) | Matriz de Sistemas de Informação (SIP, Campus Rio Paranaíba) no Catálogo de Graduação UFV 2026 e programa analítico de cada disciplina (ementa, objetivos, conteúdo, bibliografia), mais as disciplinas de matrizes anteriores que têm pasta no repositório. | Gerado por `python3 scripts/catalogo.py baixar`; não edite à mão. |
| [`referencias.json`](referencias.json) | Referências úteis por disciplina (livros abertos, cursos, documentação e ferramentas), no formato `{código: [{titulo, url, nota}]}`. | Mantido à mão. Teste os links com `python3 scripts/catalogo.py verificar`. |

Os READMEs das disciplinas são gerados a partir dos dois arquivos com `python3 scripts/catalogo.py gerar`.
