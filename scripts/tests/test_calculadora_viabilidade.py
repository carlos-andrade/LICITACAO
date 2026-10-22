#!/usr/bin/env python3
"""Unit tests for the LICITAÇÃO economic calculator."""
import importlib.util
import unittest
from argparse import Namespace
from decimal import Decimal
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "calculadora_viabilidade.py"
SPEC = importlib.util.spec_from_file_location("calculadora_viabilidade", SCRIPT)
calc_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(calc_module)


def args(**overrides):
    values = dict(
        scenario_id="TEST-1", opportunity_id="OP-1", item_id="ITEM-1",
        scenario_name="test", quantity=Decimal("715"),
        sale_price=Decimal("8.67"), acquisition_price=Decimal("3.00"),
        tax_rate=Decimal("0"), das_allocated=Decimal("82.05"),
        freight=Decimal("637.40"), local_delivery=Decimal("0"),
        handling=Decimal("0"), financial_costs=Decimal("0"),
        other_costs=Decimal("0"), contingency=Decimal("0"),
        target_margin=Decimal("0.50"), tax_confirmed=False,
        freight_confirmed=False, technical_compliance_confirmed=False,
        supplier_capacity_confirmed=False, pending_cost=[],
        assumption=["Valores de teste, não cotação formal"],
        calculated_at="2026-10-22T00:00:00-03:00"
    )
    values.update(overrides)
    return Namespace(**values)


class EconomicCalculatorTests(unittest.TestCase):
    def test_revenue_and_maximum_acquisition_match_reference(self):
        result = calc_module.calculate(args())
        self.assertEqual(result["revenue_total"], "6199.05")
        self.assertEqual(result["maximum_acquisition_total_for_target"], "2380.07")
        self.assertEqual(result["maximum_acquisition_unit_price_for_target"], "3.33")

    def test_pending_evidence_blocks_participation(self):
        result = calc_module.calculate(args())
        self.assertEqual(result["recommendation"], "PARTICIPATION_NOT_CLEARED")
        self.assertEqual(result["evidence_status"], "draft_estimate")
        self.assertGreaterEqual(len(result["pending_costs"]), 4)

    def test_margin_uses_revenue_denominator(self):
        result = calc_module.calculate(args(acquisition_price=Decimal("1.00"), das_allocated=Decimal("0"), freight=Decimal("0"), tax_confirmed=True, freight_confirmed=True, technical_compliance_confirmed=True, supplier_capacity_confirmed=True))
        self.assertEqual(result["margin_on_revenue"], "88.47")
        self.assertEqual(result["recommendation"], "MEETS_TARGET_MARGIN")

    def test_invalid_quantity_rejected(self):
        with self.assertRaises(ValueError):
            calc_module.calculate(args(quantity=Decimal("0")))

    def test_costs_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            calc_module.calculate(args(freight=Decimal("-1")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
