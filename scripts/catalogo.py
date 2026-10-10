#!/usr/bin/env python3
"""Sincroniza as pastas e os READMEs das disciplinas com o Catálogo de Graduação da UFV.

Uso:
    python3 scripts/catalogo.py baixar     # gera dados/catalogo-<ano>.json a partir do site da UFV
    python3 scripts/catalogo.py organizar  # cria/renomeia pastas com git mv (use --aplicar)
    python3 scripts/catalogo.py gerar      # escreve os README.md das disciplinas e o índice da raiz
    python3 scripts/catalogo.py verificar  # testa os links de dados/referencias.json

Requer Python 3.9+ e `pdftotext` (poppler) para ler os programas analíticos.
"""
import argparse
import html
import json
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ANO = 2026
CURSO, CAMPUS = "SIP", "crp"
CATALOGO = "https://catalogo.ufv.br"
DADOS = RAIZ / "dados" / f"catalogo-{ANO}.json"
REFERENCIAS = RAIZ / "dados" / "referencias.json"  # curadoria: livros abertos, cursos, documentação e ferramentas
LEGADO_DIR = "Z-Matrizes Anteriores"
PERIODOS = ["1", "2", "3", "4", "5", "6", "7", "8", "0"]  # 0 = optativas

# Disciplinas de matrizes anteriores que têm pasta no repositório. O valor indica as disciplinas
# da matriz 2026 com conteúdo relacionado (não é tabela oficial de equivalência).
LEGADO = {
    "ADE101": ["ADE104"],
    "ADE192": [],
    "ADE302": [],
    "CRP192": ["ESP105"],
    "CRP199": ["MAP191"],
    "CRP290": [],
    "CRP298": ["MAP112", "MAP298"],
    "MAP199": ["MAP191"],
    "NUR493": [],
    "SIN110": ["SIN111"],
    "SIN211": ["SIN215", "SIN216"],
    "SIN342": ["SIN143"],
    "SIN391": [],
    "SIN496": ["SIN494"],
    "SIN498": ["SIN488"],
    "SIN499": ["SIN489"],
}

SECOES = {
    "Objetivos", "Ementa", "Pré e correquisitos", "Oferecimentos obrigatórios",
    "Oferecimentos optativos", "Conteúdo", "Planejamento pedagógico",
    "Bibliografias básicas", "Bibliografias complementares", "Pontos de controle",
}
RUIDO = re.compile(
    r"^(UNIVERSIDADE FEDERAL DE VIÇOSA|PRE \| PRÓ-REITORIA|Programa Analítico de Disciplina|"
    r"A autenticidade deste documento|Gerado em|www\.ufv\.br|Powered by TCPDF|Descrição\s+Exemplares|"
    r"Unidade\s+T\s+P|Teórica \(T\); Prática)"
)
UNIDADE = re.compile(r"^(\s*)(\d+)\.(.*?)\s{2,}(\d+)h\s+(\d+)h\s+(\d+)h\s+(\d+)h\s+(\d+)h\s*$")
ITEM = re.compile(r"^(\s*)\d+\.(.*)$")
CODIGO = re.compile(r"\b([A-Z]{3}) ?(\d{3})(\*?)")


# ---------------------------------------------------------------------------------------------
# baixar
# ---------------------------------------------------------------------------------------------

def http(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (repo CA-SI)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def listar_matriz():
    """Retorna [(codigo, nome, periodo)] na ordem do catálogo."""
    disciplinas = []
    for p in PERIODOS:
        q = urllib.parse.urlencode({"ano": ANO, "curso": CURSO, "campus": CAMPUS, "complemento": "*", "periodo": p})
        pagina = http(f"{CATALOGO}/interno.php?{q}")
        for cod, nome in re.findall(rb'disciplina=([A-Z]{3} \d{3})#disciplina"[^>]*>[^<]*<span\s*>([^<]+)</span>', pagina):
            try:  # a página mistura trechos em UTF-8 e em Latin-1
                nome = nome.decode("utf-8")
            except UnicodeDecodeError:
                nome = nome.decode("latin-1")
            disciplinas.append((cod.decode().replace(" ", ""), html.unescape(nome).strip(), int(p) or None))
    return disciplinas


def url_pdf(codigo, ano):
    return f"{CATALOGO}/pdf.php?" + urllib.parse.urlencode(
        {"campus": CAMPUS, "disciplina": f"{codigo[:3]} {codigo[3:]}", "ano": ano}, quote_via=urllib.parse.quote)


def texto_pdf(codigo, ano):
    try:
        dados = http(url_pdf(codigo, ano))
    except urllib.error.HTTPError:
        return None
    if not dados.startswith(b"%PDF"):
        return None
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(dados)
        f.flush()
        return subprocess.run(["pdftotext", "-layout", f.name, "-"], capture_output=True, text=True, check=True).stdout


def paragrafos(linhas):
    blocos, atual = [], []
    for linha in linhas + [""]:
        if linha.strip():
            atual.append(linha.strip())
        elif atual:
            blocos.append(" ".join(atual))
            atual = []
    texto = [b for b in blocos if b != "Não definidos"]
    return texto


def interpretar_conteudo(linhas):
    unidades, pilha = [], []
    for linha in linhas:
        if not linha.strip() or linha.strip().startswith("Total"):
            continue
        m = UNIDADE.match(linha)
        if m:
            unidades.append({"titulo": m.group(3).strip(), "horas": int(m.group(8)), "itens": []})
            pilha = [len(m.group(1))]
            continue
        if not unidades:
            continue
        m = ITEM.match(linha)
        if m:
            recuo = len(m.group(1))
            while len(pilha) > 1 and recuo < pilha[-1] - 2:
                pilha.pop()
            if recuo > pilha[-1] + 3:
                pilha.append(recuo)
            unidades[-1]["itens"].append([max(len(pilha) - 1, 1), m.group(2).strip()])
        elif unidades[-1]["itens"]:
            unidades[-1]["itens"][-1][1] += " " + linha.strip()
        else:
            unidades[-1]["titulo"] += " " + linha.strip()
    return unidades


def interpretar_bibliografia(linhas):
    # Cada referência começa na linha que traz o nº de exemplares na coluna da direita; linhas sem
    # esse número (ou que terminam num ano antes da coluna) continuam a referência anterior.
    fins = [len(l.rstrip()) for l in linhas if re.search(r"\S\s{2,}\d+\s*$", l)]
    coluna = max(set(fins), key=fins.count) - 2 if fins else 0
    refs = []
    for linha in linhas:
        s = linha.strip()
        if not s or s in {"Não definidos", "Não definidas"}:
            continue
        m = re.match(r"^(.*?)\s*(\d+)$", s)
        autor = re.match(r"^[A-ZÀ-Ý]{2,}[A-ZÀ-Ý'\- ]*,", s)  # linha longa empurra o nº para fora da coluna
        if m and m.group(1) and (len(linha.rstrip()) >= coluna or autor):
            refs.append(m.group(1).strip())
        elif refs:
            refs[-1] += " " + s
        else:
            refs.append(s)
    return refs


def interpretar_pdf(texto, codigo):
    linhas = texto.splitlines()
    titulo = f"{codigo[:3]} {codigo[3:]} - "
    nome = ""
    for i, linha in enumerate(linhas):
        if linha.strip().startswith(titulo):
            nome = linha.strip()[len(titulo):]
            for prox in linhas[i + 1:]:
                if not prox.strip() or prox.strip().startswith("Campus"):
                    break
                nome += " " + prox.strip()
            break
    meta = {}
    for chave, padrao in {
        "creditos": r"Número de créditos:\s*(\d+)",
        "horas": r"Carga horária semestral:\s*(\d+)h",
        "extensao": r"Carga horária de extensão:\s*(\d+)h",
        "teorica": r"Carga horária semanal teórica:\s*(\d+)h",
        "pratica": r"Carga horária semanal prática:\s*(\d+)h",
        "semestres": r"Semestres:\s*(.+)$",
    }.items():
        m = re.search(padrao, texto, re.M)
        meta[chave] = (m.group(1).strip() if chave == "semestres" else int(m.group(1))) if m else None

    secoes, atual = {}, None
    for linha in linhas:
        s = linha.strip()
        if s in SECOES:
            atual = s
            secoes[atual] = []
        elif atual and not RUIDO.match(s) and not (nome and s == f"{titulo}{nome}"[: len(s)] and s.startswith(titulo)):
            secoes[atual].append(linha)

    oferecimentos = []
    for linha in secoes.get("Oferecimentos obrigatórios", []):
        m = re.match(r"^\s*(.+?)\s{2,}(\d+)\s*$", linha)
        if m:
            oferecimentos.append([m.group(1).strip(), int(m.group(2))])
    pre = " ".join(paragrafos(secoes.get("Pré e correquisitos", [])))
    return {
        "nome_pdf": nome,
        **meta,
        "objetivos": paragrafos(secoes.get("Objetivos", [])),
        "ementa": paragrafos(secoes.get("Ementa", [])),
        "prerequisitos": pre,
        "oferecimentos": oferecimentos,
        "conteudo": interpretar_conteudo(secoes.get("Conteúdo", [])),
        "bibliografia_basica": interpretar_bibliografia(secoes.get("Bibliografias básicas", [])),
        "bibliografia_complementar": interpretar_bibliografia(secoes.get("Bibliografias complementares", [])),
    }


def quadro_matriz(url):
    """Lê o quadro de horas e prazos do topo da página da matriz."""
    texto = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", http(url).decode("latin-1"))))
    quadro = {}
    for chave, padrao in {"horas_obrigatorias": r"Disciplinas obrigatórias (\d+)",
                          "horas_optativas": r"Disciplinas optativas (\d+)", "horas_total": r"Total (\d{3,})",
                          "anos_minimo": r"Mínimo ([\d,]+)", "anos_padrao": r"Padrão ([\d,]+)",
                          "anos_maximo": r"Máximo ([\d,]+)"}.items():
        m = re.search(padrao, texto)
        quadro[chave] = m.group(1) if m else None
    return quadro


def baixar(_args):
    fonte = f"{CATALOGO}/matriz.php?campus={CAMPUS}&complemento=*&curso={CURSO}&ano={ANO}"
    saida = {"ano": ANO, "fonte": fonte, "quadro": quadro_matriz(fonte), "disciplinas": {}}
    itens = [(c, n, p, "obrigatoria" if p else "optativa") for c, n, p in listar_matriz()]
    itens += [(c, None, None, "anterior") for c in LEGADO]
    for codigo, nome, periodo, tipo in itens:
        anos = [ANO] if tipo != "anterior" else range(ANO - 1, 2014, -1)
        for ano in anos:
            texto = texto_pdf(codigo, ano)
            if texto:
                break
        if not texto:
            print(f"aviso: programa de {codigo} não encontrado", file=sys.stderr)
            continue
        info = interpretar_pdf(texto, codigo)
        saida["disciplinas"][codigo] = {
            "codigo": codigo, "nome": info["nome_pdf"] or nome, "tipo": tipo, "periodo": periodo,
            "catalogo": ano, "pdf": url_pdf(codigo, ano), **info,
        }
        print(f"{codigo} ({tipo}, catálogo {ano}): {saida['disciplinas'][codigo]['nome']}", file=sys.stderr)
    DADOS.parent.mkdir(exist_ok=True)
    DADOS.write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"gravado {DADOS.relative_to(RAIZ)}")


# ---------------------------------------------------------------------------------------------
# organizar
# ---------------------------------------------------------------------------------------------

def carregar():
    return json.loads(DADOS.read_text(encoding="utf-8"))


def nome_pasta(d):
    nome = re.sub(r"\s+", " ", d["nome"].replace("/", " ").replace(":", "")).strip()
    return f"{d['codigo']}-{nome}"


def caminho(d):
    return Path(LEGADO_DIR) / nome_pasta(d) if d["tipo"] == "anterior" else Path(nome_pasta(d))


def organizar(args):
    cat = carregar()["disciplinas"]
    existentes = [p for p in RAIZ.iterdir() if p.is_dir()] + \
        ([p for p in (RAIZ / LEGADO_DIR).iterdir() if p.is_dir()] if (RAIZ / LEGADO_DIR).exists() else [])
    for codigo, d in cat.items():
        destino = caminho(d)
        candidatas = [p for p in existentes if p.name.split("-")[0] == codigo]
        exata = [p for p in candidatas if p.relative_to(RAIZ) == destino]
        if exata:
            continue
        # Se houver mais de uma pasta com o código, prefere a de nome mais parecido.
        candidatas.sort(key=lambda p: -len(set(p.name.lower().split()) & set(destino.name.lower().split())))
        if candidatas:
            origem = candidatas[0].relative_to(RAIZ)
            print(f"git mv '{origem}' '{destino}'")
            if args.aplicar:
                (RAIZ / destino).parent.mkdir(exist_ok=True)
                subprocess.run(["git", "mv", str(origem), str(destino)], cwd=RAIZ, check=True)
                existentes.remove(candidatas[0])
        else:
            print(f"mkdir '{destino}'")
            if args.aplicar:
                (RAIZ / destino).mkdir(parents=True)
    restantes = sorted(p.name for p in existentes if CODIGO.match(p.name) and p.name.split("-")[0] not in cat
                       or (p.name.split("-")[0] in cat and p.relative_to(RAIZ) != caminho(cat[p.name.split("-")[0]])
                           and (RAIZ / caminho(cat[p.name.split("-")[0]])).exists()))
    for nome in restantes:
        print(f"# sem correspondência no catálogo (revisar manualmente): {nome}")


# ---------------------------------------------------------------------------------------------
# gerar
# ---------------------------------------------------------------------------------------------

def link(destino, origem_dir=Path(".")):
    rel = Path(*([".."] * len(origem_dir.parts))) / destino if origem_dir.parts else destino
    return urllib.parse.quote(rel.as_posix())


def linkar_codigos(texto, cat, origem):
    def troca(m):
        cod = m.group(1) + m.group(2)
        rotulo = f"{m.group(1)} {m.group(2)}{m.group(3)}"
        if cod in cat and (RAIZ / caminho(cat[cod])).exists():
            return f"[{rotulo}]({link(caminho(cat[cod]), origem)})"
        return rotulo
    texto = re.sub(r"\b(\d+) OBR\b", r"\1 h de disciplinas obrigatórias concluídas", texto)
    return CODIGO.sub(troca, texto)


def submodulos():
    arq = RAIZ / ".gitmodules"
    if not arq.exists():
        return {}
    texto = arq.read_text(encoding="utf-8")
    return dict(re.findall(r"path = (.+)\n\s*url = (.+)", texto))


def materiais(pasta):
    subs = {Path(k): v for k, v in submodulos().items()}
    itens = []
    for p in sorted(pasta.rglob("*")):
        rel = p.relative_to(RAIZ)
        if rel in subs:
            itens.append(f"- [{p.relative_to(pasta).as_posix()}]({subs[rel]}) (submódulo git)")
        elif p.is_file() and p.name not in {"README.md", "keep", ".DS_Store"} \
                and not any(s in rel.parents for s in subs):
            itens.append(f"- [{p.relative_to(pasta).as_posix()}]({urllib.parse.quote(p.relative_to(pasta).as_posix())})")
    return itens


def dependentes(cat):
    deps = {}
    for cod, d in cat.items():
        if d["tipo"] == "anterior":
            continue
        for m in CODIGO.finditer(d["prerequisitos"]):
            deps.setdefault(m.group(1) + m.group(2), []).append(cod)
    return deps


def rotulo_tipo(d):
    if d["tipo"] == "obrigatoria":
        return f"Obrigatória · {d['periodo']}º período"
    if d["tipo"] == "optativa":
        return "Optativa"
    return f"Matriz anterior (programa do Catálogo {d['catalogo']})"


def readme_disciplina(d, cat, deps, uteis):
    pasta = caminho(d)
    carga = f"{d['horas']} h" if d["horas"] is not None else ""
    if d.get("teorica") is not None:
        carga += f" ({d['teorica']} h teóricas + {d['pratica']} h práticas por semana)"
    if d.get("extensao"):
        carga += f" · {d['extensao']} h de extensão"
    linhas = [f"# {d['codigo']} — {d['nome']}", "",
              f"> **{rotulo_tipo(d)}** · {carga} · {d['creditos']} créditos"
              + (f" · Semestres: {d['semestres']}" if d.get("semestres") else ""), ""]

    pre = linkar_codigos(d["prerequisitos"], cat, pasta) or "Nenhum"
    if "*" in d["prerequisitos"]:
        pre += " (`*` = correquisito: pode ser cursada no mesmo semestre)"
    tabela = [("Pré-requisitos", pre)]
    if d["tipo"] != "anterior" and deps.get(d["codigo"]):
        tabela.append(("É pré-requisito de", ", ".join(linkar_codigos(c, cat, pasta) for c in deps[d["codigo"]])))
    if d["tipo"] == "anterior":
        rel = LEGADO.get(d["codigo"], [])
        tabela.append(("Na matriz 2026", ", ".join(linkar_codigos(c, cat, pasta) + f" — {cat[c]['nome']}" for c in rel)
                       if rel else "Sem disciplina correspondente"))
    outros = [f"{c} ({p}º)" for c, p in d["oferecimentos"] if c != "Sistemas de Informação"]
    if outros:
        tabela.append(("Obrigatória também em", ", ".join(outros)))
    tabela.append(("Programa analítico", f"[Catálogo de Graduação UFV {d['catalogo']} (PDF)]({d['pdf']})"))
    linhas += ["| | |", "|---|---|"] + [f"| **{k}** | {v} |" for k, v in tabela] + [""]

    if d["tipo"] == "anterior":
        linhas += ["Esta disciplina não faz parte da matriz curricular 2026. A pasta guarda o material de quem cursou "
                   "matrizes anteriores. Aproveitamento de estudos e equivalências são definidos pela coordenação do curso.", ""]

    for titulo, chave in (("Ementa", "ementa"), ("Objetivos", "objetivos")):
        if d[chave]:
            linhas += [f"## {titulo}", ""] + [p + "\n" for p in d[chave]]

    if d["conteudo"]:
        linhas += ["## Conteúdo programático", ""]
        for i, u in enumerate(d["conteudo"], 1):
            linhas.append(f"{i}. **{u['titulo']}** ({u['horas']} h)")
            for nivel, item in u["itens"]:
                linhas.append("   " + "  " * (nivel - 1) + f"- {item}")
        linhas.append("")

    if any(r not in {"Não definidas", "Não definidos"} for r in d["bibliografia_basica"] + d["bibliografia_complementar"]):
        linhas += ["## Bibliografia", ""]
        for titulo, chave in (("Básica", "bibliografia_basica"), ("Complementar", "bibliografia_complementar")):
            refs = [r for r in d[chave] if r not in {"Não definidas", "Não definidos"}]
            if refs:
                linhas += [f"### {titulo}", ""] + [f"- {r}" for r in refs] + [""]

    if uteis.get(d["codigo"]):
        linhas += ["## Referências úteis", ""]
        linhas += [f"- [{r['titulo']}]({r['url']})" + (f" — {r['nota']}" if r["nota"] else "") for r in uteis[d["codigo"]]]
        linhas.append("")

    itens = materiais(RAIZ / pasta)
    if itens:
        linhas += ["## Materiais neste repositório", ""] + itens + [""]

    contribuir = f"{link(Path('README.md'), pasta)}#como-contribuir"
    linhas += ["---", "",
               "<sub>Ementa, objetivos, conteúdo e bibliografia transcritos do programa analítico oficial da UFV; "
               f"referências úteis em `dados/referencias.json`. Tem material ou indicação desta disciplina? "
               f"[Contribua]({contribuir}). Gerado por `scripts/catalogo.py`; edite o script ou os dados, não este "
               "arquivo.</sub>", ""]
    return "\n".join(linhas)


def mermaid(cat):
    obrig = {c: d for c, d in cat.items() if d["tipo"] == "obrigatoria"}
    linhas = ["```mermaid", "flowchart TD"]
    for p in range(1, 9):
        linhas.append(f"    subgraph P{p}[{p}º período]")
        for c, d in obrig.items():
            if d["periodo"] == p:
                linhas.append(f'        {c}["{c}<br/>{d["nome"]}"]')
        linhas.append("    end")
    for c, d in obrig.items():
        for m in CODIGO.finditer(d["prerequisitos"]):
            pre = m.group(1) + m.group(2)
            if pre in obrig:
                linhas.append(f"    {pre} {'-.->' if m.group(3) else '-->'} {c}")
    linhas.append("```")
    return linhas


def indice_raiz(cat):
    obrig = [d for d in cat.values() if d["tipo"] == "obrigatoria"]
    opt = sorted((d for d in cat.values() if d["tipo"] == "optativa"), key=lambda d: d["codigo"])
    ant = sorted((d for d in cat.values() if d["tipo"] == "anterior"), key=lambda d: d["codigo"])
    h_obrig = sum(d["horas"] for d in obrig)

    def linha(d):
        pre = linkar_codigos(d["prerequisitos"], cat, Path(".")) or "—"
        return f"| [{d['codigo']}]({link(caminho(d))}) | {d['nome']} | {d['horas']} h | {pre} |"

    cab = ["| Código | Disciplina | Carga | Pré-requisitos |", "|---|---|---|---|"]
    dados = carregar()
    q = dados.get("quadro", {})
    out = [f"## Matriz curricular {ANO}", "",
           f"Matriz do curso de Sistemas de Informação (SIP) no [Catálogo de Graduação UFV {ANO}]({dados['fonte']}).", "",
           "| Carga horária | Horas | | Prazo de integralização | Anos |", "|---|---|---|---|---|",
           f"| Disciplinas obrigatórias | {q.get('horas_obrigatorias')} | | Mínimo | {q.get('anos_minimo')} |",
           f"| Disciplinas optativas | {q.get('horas_optativas')} | | Padrão | {q.get('anos_padrao')} |",
           f"| **Total** | **{q.get('horas_total')}** | | Máximo | {q.get('anos_maximo')} |", ""]
    if q.get("horas_obrigatorias") and int(q["horas_obrigatorias"]) != h_obrig:
        out += [f"O quadro acima é o do catálogo. A soma das disciplinas obrigatórias listadas na matriz dá {h_obrig} h.", ""]
    out += ["Cada pasta tem um `README.md` com ementa, objetivos, conteúdo programático e bibliografia do programa "
            "analítico oficial, além de referências úteis (livros abertos, cursos, documentação e ferramentas).", "",
           "### Fluxograma", "",
           "Setas contínuas indicam pré-requisito; setas tracejadas, correquisito (marcado com `*` no catálogo).", ""]
    out += mermaid(cat) + [""]
    out += ["### Disciplinas obrigatórias", ""]
    for p in range(1, 9):
        do_periodo = [d for d in obrig if d["periodo"] == p]
        out += [f"#### {p}º período ({sum(d['horas'] for d in do_periodo)} h)", ""] + cab + [linha(d) for d in do_periodo] + [""]
    out += ["### Disciplinas optativas", ""] + cab + [linha(d) for d in opt] + [""]
    out += ["### Matrizes anteriores", "",
            f"Disciplinas que saíram da matriz ficam em [`{LEGADO_DIR}/`]({link(Path(LEGADO_DIR))}) com seus materiais. "
            "A coluna da direita aponta disciplinas da matriz 2026 com conteúdo relacionado; não é tabela oficial de "
            "equivalência.", "",
            "| Código | Disciplina | Relacionada na matriz 2026 |", "|---|---|---|"]
    for d in ant:
        rel = ", ".join(f"[{c}]({link(caminho(cat[c]))})" for c in LEGADO.get(d["codigo"], [])) or "—"
        out.append(f"| [{d['codigo']}]({link(caminho(d))}) | {d['nome']} | {rel} |")
    out += ["", "### Outras pastas", "",
            "- [`guias`](guias) — guias do curso: matriz, TCC, extensão, optativas e matrizes anteriores",
            "- [`1-Artigos e Monografias`](1-Artigos%20e%20Monografias) — artigos, monografias e TCCs da comunidade",
            "- [`2-Interdisciplinar`](2-Interdisciplinar) — materiais que atendem a várias disciplinas",
            "- [`Z-Outros`](Z-Outros) — regulamentos, modelos de documento e links úteis"]
    return out


def gerar(_args):
    cat = carregar()["disciplinas"]
    deps = dependentes(cat)
    refs = json.loads(REFERENCIAS.read_text(encoding="utf-8")) if REFERENCIAS.exists() else {}
    for d in cat.values():
        pasta = RAIZ / caminho(d)
        if not pasta.exists():
            print(f"aviso: pasta ausente {pasta.relative_to(RAIZ)} (rode `organizar --aplicar`)", file=sys.stderr)
            continue
        (pasta / "README.md").write_text(readme_disciplina(d, cat, deps, refs), encoding="utf-8")
    readme = RAIZ / "README.md"
    texto = readme.read_text(encoding="utf-8")
    inicio, fim = "<!-- MATRIZ:INICIO -->", "<!-- MATRIZ:FIM -->"
    if inicio not in texto:
        sys.exit("README.md da raiz não tem os marcadores MATRIZ:INICIO/FIM")
    antes, resto = texto.split(inicio, 1)
    _, depois = resto.split(fim, 1)
    bloco = "\n".join([inicio, "<!-- Gerado por scripts/catalogo.py; não edite à mão. -->", ""] + indice_raiz(cat) + ["", fim])
    readme.write_text(antes + bloco + depois, encoding="utf-8")
    print(f"{len(cat)} READMEs de disciplina e índice da raiz atualizados")


NAVEGADOR = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
}


def verificar(_args):
    """Testa os links de dados/referencias.json. 403 costuma ser bloqueio anti-robô, não link quebrado."""
    from concurrent.futures import ThreadPoolExecutor
    refs = json.loads(REFERENCIAS.read_text(encoding="utf-8"))
    urls = sorted({r["url"] for lista in refs.values() for r in lista})

    def status(url):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=NAVEGADOR), timeout=30) as r:
                return url, r.status
        except urllib.error.HTTPError as e:
            return url, e.code
        except Exception as e:  # timeout, DNS, TLS
            return url, type(e).__name__

    with ThreadPoolExecutor(16) as ex:
        falhas = [(u, s) for u, s in ex.map(status, urls) if s != 200]
    for url, s in falhas:
        print(f"{s}\t{url}")
    print(f"{len(urls) - len(falhas)}/{len(urls)} links responderam 200")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("baixar").set_defaults(func=baixar)
    org = sub.add_parser("organizar")
    org.add_argument("--aplicar", action="store_true", help="executa os git mv/mkdir em vez de só listar")
    org.set_defaults(func=organizar)
    sub.add_parser("gerar").set_defaults(func=gerar)
    sub.add_parser("verificar", help="testa os links de dados/referencias.json").set_defaults(func=verificar)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
