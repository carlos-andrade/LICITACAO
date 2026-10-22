#!/usr/bin/env python3
"""Offline tests for PNCP capture URL parsing and item normalization."""
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "pncp_capture.py"
SPEC = importlib.util.spec_from_file_location("pncp_capture", SCRIPT)
pncp = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pncp)


class PncpCaptureTests(unittest.TestCase):
    def test_parse_official_editais_url(self):
        self.assertEqual(
            pncp.parse_url("https://pncp.gov.br/app/editais/33663683000116/2026/548"),
            ("33663683000116", "2026", "548"),
        )

    def test_parse_rejects_non_pncp_host(self):
        with self.assertRaises(ValueError):
            pncp.parse_url("https://example.com/app/editais/33663683000116/2026/548")

    def test_parse_rejects_unrecognized_path(self):
        with self.assertRaises(ValueError):
            pncp.parse_url("https://pncp.gov.br/app/editais/invalid")

    def test_normalize_item_preserves_reference_values(self):
        payload = {
            "resultado": [{
                "numeroItem": 1,
                "codigoCatmat": "617347",
                "descricao": "Copo descartável biodegradável 180 ml",
                "materialOuServico": "MATERIAL",
                "unidadeMedida": "pacote",
                "quantidade": 715,
                "valorUnitarioEstimado": 8.67,
                "valorTotalEstimado": 6199.05,
                "orcamentoSigiloso": False,
            }]
        }
        rows = pncp.normalize_items(payload)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["numero"], "1")
        self.assertEqual(rows[0]["codigo"], "617347")
        self.assertEqual(rows[0]["descricao"], "Copo descartável biodegradável 180 ml")
        self.assertEqual(rows[0]["quantidade"], "715")
        self.assertEqual(rows[0]["valor_unitario"], "8.67")
        self.assertEqual(rows[0]["valor_total"], "6199.05")
        self.assertIn('"numeroItem": 1', rows[0]["json_item"])

    def test_empty_payload_is_not_fabricated_as_item(self):
        self.assertEqual(pncp.normalize_items({"resultado": []}), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
