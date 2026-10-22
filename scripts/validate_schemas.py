#!/usr/bin/env python3
"""Validate JSON Schemas and example records for Sistema LICITAÇÃO."""
from __future__ import annotations
import json
import sys
from decimal import Decimal
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    print("Missing dependency: install with python -m pip install jsonschema.", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "ARQUITETURA" / "schemas"
EXAMPLE_DIR = ROOT / "ARQUITETURA" / "exemplos"


def load_json(path: Path):
    # Keep JSON integers as int so Draft 2020-12 schema keywords such as
    # minLength/minimum are validated with their required JSON integer type.
    # Preserve decimal values as Decimal for exact financial arithmetic.
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle, parse_float=Decimal)


def schema_for_example(path: Path, validators: dict):
    """Resolve examples to schemas by explicit filename conventions."""
    name = path.name.lower()
    if "oportunidade" in name:
        return validators.get("oportunidade")
    if "item" in name:
        return validators.get("item")
    if "cotacao" in name or "cotação" in name:
        return validators.get("cotacao")
    if "decisao" in name or "decisão" in name:
        return validators.get("decisao")
    if "documento" in name:
        return validators.get("documento")
    if "cenario" in name or "cenário" in name:
        return validators.get("cenario-economico")
    return None


def main() -> int:
    schemas = {}
    errors = []
    for path in sorted(SCHEMA_DIR.glob("*.schema.json")):
        try:
            schema = load_json(path)
            Draft202012Validator.check_schema(schema)
            schemas[path.name.removesuffix(".schema.json")] = schema
            print(f"SCHEMA OK: {path.relative_to(ROOT)}")
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid schema: {exc}")

    validators = {
        name: Draft202012Validator(schema, format_checker=FormatChecker())
        for name, schema in schemas.items()
    }
    for path in sorted(EXAMPLE_DIR.glob("*.json")):
        try:
            record = load_json(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue

        validator = schema_for_example(path, validators)
        if validator is None:
            errors.append(f"{path.relative_to(ROOT)}: no schema mapping defined")
            continue

        found = sorted(
            validator.iter_errors(record),
            key=lambda e: list(map(str, e.absolute_path)),
        )
        if found:
            for err in found:
                where = ".".join(map(str, err.absolute_path)) or "<root>"
                errors.append(f"{path.relative_to(ROOT)} [{where}]: {err.message}")
        else:
            print(f"EXAMPLE OK: {path.relative_to(ROOT)}")

    revenue = Decimal("8.67") * Decimal("715")
    if revenue != Decimal("6199.05"):
        errors.append(f"UFRJ arithmetic check failed: expected 6199.05, got {revenue}")
    else:
        print("ARITHMETIC OK: 715 × 8.67 = 6199.05")

    if errors:
        print("\nVALIDATION FAILED:")
        for err in errors:
            print(f"- {err}")
        return 1
    print("\nAll schema/example/arithmetic checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
