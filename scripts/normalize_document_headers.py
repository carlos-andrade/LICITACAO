#!/usr/bin/env python3
"""Normalize project-owned Markdown headers and produce a verifiable inventory.

Mirrored upstream governance documents under .governanca/upstream are audited but
not rewritten, preserving the upstream source of truth.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/carlos-andrade/LICITACAO"
AUTHORITY_URL = f"{REPO_URL}/blob/main/CONSTITUICAO.md"
EXCLUDED_PREFIXES = (".git/",)
UPSTREAM_PREFIX = ".governanca/upstream/"
INVENTORY_PATH = "docs/governanca/INVENTARIO-CONFORMIDADE-DOCUMENTAL.md"
REQUIRED_FIELDS = [
    "ID", "Projeto", "Repositório", "Tipo documental", "Fase", "Estado",
    "Versão", "SHA-256 (conteúdo canónico)",
    "Commit de referência (versão anterior)", "Data de criação",
    "Data de atualização", "Responsável", "Aprovador", "Origem",
    "Autoridade superior", "Cadeia de autoridade",
]
HASH_LABEL = "**SHA-256 (conteúdo canónico)**"
COMMIT_LABEL = "**Commit de referência (versão anterior)**"


def git_output(*args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    except Exception:
        return ""


def canonical_hash(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    lines = [line for line in text.splitlines() if not (
        line.startswith("| " + HASH_LABEL + " |")
        or line.startswith("| " + COMMIT_LABEL + " |")
    )]
    payload = "\n".join(lines).rstrip("\n") + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def md_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md")
                  if ".git" not in p.parts and "node_modules" not in p.parts)


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def title_of(text: str, path: Path) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def deterministic_id(path: str) -> str:
    slug = re.sub(r"[^A-Z0-9]+", "-", path.upper()).strip("-")
    slug = slug[-48:]
    digest = hashlib.sha256(path.encode("utf-8")).hexdigest()[:8].upper()
    return f"LIC-DOC-{slug}-{digest}"


def type_of(path: str) -> str:
    name = Path(path).name.lower()
    if name == "readme.md":
        return "README"
    if "comparativo" in name or "tabela" in name:
        return "COMPARATIVO_PRECOS"
    if "auditoria" in name or "inventario" in name:
        return "AUDITORIA"
    if "analise" in name or "análise" in name:
        return "ANALISE"
    if "roadmap" in name:
        return "ROADMAP"
    if "constituicao" in name:
        return "GOVERNANCA"
    if "arquitetura" in name:
        return "ARQUITETURA"
    if "schema" in path.lower():
        return "DOCUMENTACAO_TECNICA"
    return "DOCUMENTO_TECNICO"


def preserve_or_default(text: str, field: str, default: str) -> str:
    match = re.search(r"^\| \*\*" + re.escape(field) + r"\*\* \| (.*?) \|$", text, re.M)
    return match.group(1).strip() if match else default


def with_header(path: Path, text: str, base_commit: str) -> str:
    path_s = rel(path)
    title = title_of(text, path)
    had_header = bool(re.match(r"^# .+\n\n\| Campo \| Valor \|", text))
    old = text
    if had_header:
        body = re.sub(r"^# .+\n(?:\n\| Campo \| Valor \|\n(?:\|.*\n)+\n)?", "", text, count=1)
        # Extract all existing fields before replacing the header.
        values = {field: preserve_or_default(text, field, "") for field in REQUIRED_FIELDS}
    else:
        body = re.sub(r"^# .+\n?", "", text, count=1)
        values = {field: "" for field in REQUIRED_FIELDS}

    values["ID"] = values["ID"] or deterministic_id(path_s)
    values["Projeto"] = values["Projeto"] or "LICITAÇÃO"
    values["Repositório"] = values["Repositório"] or f"[carlos-andrade/LICITACAO]({REPO_URL})"
    values["Tipo documental"] = values["Tipo documental"] or type_of(path_s)
    values["Fase"] = values["Fase"] or "N/A — fase não definida no conteúdo de origem"
    state = values["Estado"]
    values["Estado"] = state if state in {"RASCUNHO", "EM_REVISAO", "APROVADO", "DEPRECADO", "REJEITADO"} else "EM_REVISAO"
    values["Versão"] = values["Versão"] or "1.0.0"
    values["Commit de referência (versão anterior)"] = values["Commit de referência (versão anterior)"] or (
        f"[{base_commit}]({REPO_URL}/commit/{base_commit})" if base_commit else "N/A — referência Git não disponível"
    )
    values["Data de criação"] = values["Data de criação"] or "N/A — data histórica não verificada"
    values["Data de atualização"] = date.today().isoformat()
    values["Responsável"] = values["Responsável"] or "Responsável pelo projeto LICITAÇÃO"
    values["Aprovador"] = values["Aprovador"] or "Pendente — não há evidência de aprovação neste documento"
    values["Origem"] = values["Origem"] or f"Conteúdo existente no repositório; caminho: `{path_s}`"
    values["Autoridade superior"] = values["Autoridade superior"] or f"[Constituição do projeto]({AUTHORITY_URL})"
    values["Cadeia de autoridade"] = values["Cadeia de autoridade"] or "PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO"

    rows = [
        f"# {title}", "", "| Campo | Valor |", "|---|---|",
    ]
    for field in REQUIRED_FIELDS:
        value = values[field]
        if field == "SHA-256 (conteúdo canónico)":
            value = "PENDENTE"
        elif field == "Commit de referência (versão anterior)":
            value = values[field]
        rows.append(f"| **{field}** | {value} |")
    # Preserve the existing document body, including its original title text only once.
    result = "\n".join(rows) + "\n\n" + body.lstrip("\n")
    result = result.rstrip() + "\n"
    digest = canonical_hash(result)
    result = re.sub(
        r"^\| \*\*SHA-256 \(conteúdo canónico\)\*\* \| .*? \|$",
        f"| **SHA-256 (conteúdo canónico)** | {digest} |",
        result, count=1, flags=re.M
    )
    return result


def verify(text: str) -> tuple[bool, list[str]]:
    problems = []
    if not re.match(r"^# .+\n\n\| Campo \| Valor \|", text):
        problems.append("cabeçalho visual ausente")
    for field in REQUIRED_FIELDS:
        if not re.search(r"^\| \*\*" + re.escape(field) + r"\*\* \| .+ \|$", text, re.M):
            problems.append(f"campo ausente/vazio: {field}")
    match = re.search(r"^\| \*\*SHA-256 \(conteúdo canónico\)\*\* \| ([0-9a-f]{64}) \|$", text, re.M)
    if not match:
        problems.append("SHA-256 ausente ou inválido")
    elif match.group(1) != canonical_hash(text):
        problems.append("SHA-256 divergente")
    return not problems, problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    base_commit = git_output("rev-parse", "HEAD^") or git_output("rev-parse", "HEAD")
    today = date.today().isoformat()
    all_md = md_files()
    project_md = [p for p in all_md if not rel(p).startswith(UPSTREAM_PREFIX)]
    upstream_md = [p for p in all_md if rel(p).startswith(UPSTREAM_PREFIX)]
    changed = []
    for p in project_md:
        old = p.read_text(encoding="utf-8")
        new = with_header(p, old, base_commit)
        if new != old:
            if args.write:
                p.write_text(new, encoding="utf-8", newline="\n")
            changed.append(rel(p))

    # Build an inventory of all project-owned Markdown and binary office/PDF files.
    rows = []
    ids: dict[str, list[str]] = {}
    valid_count = 0
    for p in project_md:
        text = p.read_text(encoding="utf-8")
        ok, problems = verify(text)
        id_match = re.search(r"^\| \*\*ID\*\* \| (.*?) \|$", text, re.M)
        doc_id = id_match.group(1) if id_match else ""
        if doc_id:
            ids.setdefault(doc_id, []).append(rel(p))
        if ok:
            valid_count += 1
        rows.append((rel(p), doc_id, ok, "; ".join(problems) if problems else "Conforme"))
    duplicates = {k: v for k, v in ids.items() if len(v) > 1}
    for doc_id, files in duplicates.items():
        for path in files:
            for i, row in enumerate(rows):
                if row[0] == path:
                    rows[i] = (row[0], row[1], False, f"ID duplicado: {doc_id}")

    binary = sorted(p for p in ROOT.rglob("*") if p.is_file()
                    and ".git" not in p.parts
                    and p.suffix.lower() in {".pdf", ".docx", ".doc", ".xlsx", ".xls", ".odt", ".ods", ".pptx"})
    inventory = [
        "# Inventário de conformidade documental — LICITAÇÃO", "",
        "| Campo | Valor |", "|---|---|",
        "| **ID** | LIC-AUD-DOC-001 |",
        "| **Projeto** | LICITAÇÃO |",
        f"| **Repositório** | [carlos-andrade/LICITACAO]({REPO_URL}) |",
        "| **Tipo documental** | AUDITORIA |",
        "| **Fase** | Normalização e controlo documental |",
        "| **Estado** | EM_REVISAO |",
        "| **Versão** | 1.0.0 |",
        "| **SHA-256 (conteúdo canónico)** | PENDENTE |",
        f"| **Commit de referência (versão anterior)** | [{base_commit}]({REPO_URL}/commit/{base_commit}) |" if base_commit else "| **Commit de referência (versão anterior)** | N/A — referência Git não disponível |",
        "| **Data de criação** | N/A — data histórica não verificada |",
        f"| **Data de atualização** | {today} |",
        "| **Responsável** | Responsável pelo projeto LICITAÇÃO |",
        "| **Aprovador** | Pendente — auditoria técnica, não aprovação substantiva |",
        "| **Origem** | Inventário gerado por scripts/normalize_document_headers.py |",
        f"| **Autoridade superior** | [Constituição do projeto]({AUTHORITY_URL}) |",
        "| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |", "",
        "## Resultado", "",
        f"- Documentos Markdown do projeto (fora de .governanca/upstream): **{len(project_md)}**.",
        f"- Documentos conformes após normalização e verificação de hash: **{valid_count}/{len(project_md)}**.",
        f"- IDs duplicados: **{len(duplicates)}**.",
        f"- Ficheiros PDF/Office no repositório: **{len(binary)}**.",
        f"- Documentos Markdown espelhados em `{UPSTREAM_PREFIX}` auditados sem reescrita: **{len(upstream_md)}** (a fonte de verdade é o repositório upstream).",
        f"- Ficheiros Markdown alterados nesta execução: **{len(changed)}**.", "",
        "## Inventário Markdown", "",
        "| Caminho | ID | Resultado |",
        "|---|---|---|",
    ]
    for path, doc_id, ok, note in rows:
        inventory.append(f"| `{path}` | `{doc_id}` | {'CONFORME' if ok else 'PENDENTE'} — {note} |")
    inventory += ["", "## Ficheiros PDF e Office no repositório", ""]
    if binary:
        inventory += ["| Caminho | Formato | Estado |", "|---|---|---|"]
        for p in binary:
            inventory.append(f"| `{rel(p)}` | {p.suffix.lower()} | REVISÃO ESPECÍFICA NECESSÁRIA — verificar cabeçalho visual sem alterar conteúdo técnico |")
    else:
        inventory.append("Não foram encontrados ficheiros PDF, DOC/DOCX, XLS/XLSX, ODT/ODS ou PPTX versionados neste repositório. Os anexos enviados diretamente na conversa não são ficheiros versionados do Git e exigem uma operação separada para serem editados e publicados.")
    inventory += ["", "## Critérios e limitações", "",
        "- O cabeçalho segue a norma Markdown local: título de nível 1, tabela de metadados e campos canónicos.",
        "- O SHA-256 é calculado em UTF-8/LF sobre o documento integral, removendo apenas as linhas SHA-256 e commit de referência.",
        "- A data de criação histórica não é inferida; usa-se N/A quando não verificada.",
        "- Documentos não aprovados não recebem estado APROVADO; usa-se EM_REVISAO quando o estado não é demonstrável.",
        "- A presença do cabeçalho e a validade do hash são verificações estruturais, não aprovação substantiva do conteúdo.",
        "- Os documentos upstream não são reescritos automaticamente para preservar a autoridade e o histórico do repositório de origem.", "",
        "## Próxima ação", "",
        "Rever exceções do inventário e validar separadamente qualquer documento binário antes de alterar o layout visual.",
        ""
    ]
    inv_text = "\n".join(inventory)
    inv_path = ROOT / INVENTORY_PATH
    # Normalize inventory with its own header and calculate its checksum.
    inv_text = with_header(inv_path, inv_text, base_commit)
    if args.write:
        inv_path.parent.mkdir(parents=True, exist_ok=True)
        inv_path.write_text(inv_text, encoding="utf-8", newline="\n")
    ok, problems = verify(inv_text)
    if not ok:
        print("Inventário gerado com problemas:", problems)
        return 1
    print(f"Markdown projeto: {len(project_md)}; alterados: {len(changed)}; hashes verificados: {valid_count}/{len(project_md)}; IDs duplicados: {len(duplicates)}; binários versionados: {len(binary)}")
    if duplicates:
        print("IDs duplicados:", duplicates)
    return 0 if not duplicates and valid_count == len(project_md) else 1


if __name__ == "__main__":
    raise SystemExit(main())
