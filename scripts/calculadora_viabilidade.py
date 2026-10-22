#!/usr/bin/env python3
"""Transparent economic scenario calculator for Sistema LICITAÇÃO.

Uses Decimal arithmetic and keeps estimated inputs explicit. This tool is a
calculation aid, not tax advice; tax treatment must be supplied/validated by a
qualified professional.
"""
from __future__ import annotations
import argparse
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_DOWN, ROUND_HALF_UP
from pathlib import Path

CENT = Decimal("0.01")
ZERO = Decimal("0")

def money(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_UP)

def conservative_money(value: Decimal) -> Decimal:
    """Round an allowed budget down so rounding never breaches a cost ceiling."""
    return value.quantize(CENT, rounding=ROUND_DOWN)

def dec(value: str) -> Decimal:
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError(f"Invalid decimal: {value}") from exc
    if not result.is_finite():
        raise argparse.ArgumentTypeError("Value must be finite")
    return result

def calculate(args: argparse.Namespace) -> dict:
    quantity, sale_price, acquisition_price = args.quantity, args.sale_price, args.acquisition_price
    if quantity <= ZERO:
        raise ValueError("quantity must be greater than zero")
    for name in ("sale_price", "acquisition_price", "das_allocated", "freight", "local_delivery", "handling", "financial_costs", "other_costs", "contingency", "tax_rate"):
        if getattr(args, name) < ZERO:
            raise ValueError(f"{name} cannot be negative")
    if args.target_margin < ZERO or args.target_margin >= Decimal("1"):
        raise ValueError("target_margin must be >= 0 and < 1")
    if args.tax_rate >= Decimal("1"):
        raise ValueError("tax_rate must be < 1")

    revenue = quantity * sale_price
    acquisition = quantity * acquisition_price
    tax = revenue * args.tax_rate
    other_costs = sum((args.das_allocated, args.freight, args.local_delivery, args.handling, args.financial_costs, args.other_costs, args.contingency), ZERO)
    total_cost = acquisition + tax + other_costs
    profit = revenue - total_cost
    margin = profit / revenue if revenue else ZERO
    markup = profit / total_cost if total_cost else None
    non_acquisition_costs = tax + other_costs
    target_cost_ceiling = conservative_money(revenue * (Decimal("1") - args.target_margin))
    max_acquisition_total = target_cost_ceiling - non_acquisition_costs
    max_acquisition_unit = max_acquisition_total / quantity
    target_profit = revenue * args.target_margin

    pending_costs = list(args.pending_cost)
    if not args.tax_confirmed:
        pending_costs.append("Tratamento tributário/alíquota incremental não confirmado por contador ou fonte fiscal competente")
    if not args.freight_confirmed:
        pending_costs.append("Frete não confirmado por cotação válida que cubra todos os destinos e condições de entrega")
    if not args.technical_compliance_confirmed:
        pending_costs.append("Conformidade técnica do produto não confirmada por documentação adequada")
    if not args.supplier_capacity_confirmed:
        pending_costs.append("Estoque/capacidade de fornecimento para a quantidade integral não confirmados")

    blockers = []
    if pending_costs:
        blockers.append("Há custos ou evidências críticas pendentes")
    if margin < args.target_margin:
        blockers.append("Margem calculada inferior à meta")
    if max_acquisition_unit < ZERO:
        blockers.append("Custos não relacionados à aquisição já excedem o orçamento compatível com a meta")

    return {
        "schema_version": "1.0.0", "id": args.scenario_id,
        "opportunity_id": args.opportunity_id, "item_id": args.item_id,
        "scenario_name": args.scenario_name, "quantity": str(quantity),
        "sale_unit_price": str(money(sale_price)), "revenue_total": str(money(revenue)),
        "acquisition_unit_price": str(money(acquisition_price)), "acquisition_total": str(money(acquisition)),
        "taxes_total": str(money(tax)), "das_allocated": str(money(args.das_allocated)),
        "freight_total": str(money(args.freight)), "local_delivery_total": str(money(args.local_delivery)),
        "handling_total": str(money(args.handling)), "financial_costs_total": str(money(args.financial_costs)),
        "other_costs_total": str(money(args.other_costs)), "contingency_total": str(money(args.contingency)),
        "other_costs_including_das": str(money(other_costs)), "total_cost": str(money(total_cost)),
        "profit": str(money(profit)),
        "margin_on_revenue": str((margin * Decimal("100")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)),
        "markup_on_cost": None if total_cost == ZERO else str(((profit / total_cost) * Decimal("100")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)),
        "target_profit_margin": str(args.target_margin),
        "target_profit_margin_percent": str((args.target_margin * Decimal("100")).quantize(Decimal("0.01"))),
        "target_profit": str(money(target_profit)),
        "maximum_acquisition_total_for_target": str(money(max_acquisition_total)),
        "maximum_acquisition_unit_price_for_target": str(conservative_money(max_acquisition_unit)),
        "currency": "BRL", "evidence_status": "verified" if not pending_costs else "draft_estimate",
        "input_status": {"tax_confirmed": args.tax_confirmed, "freight_confirmed": args.freight_confirmed,
                         "technical_compliance_confirmed": args.technical_compliance_confirmed,
                         "supplier_capacity_confirmed": args.supplier_capacity_confirmed},
        "assumptions": args.assumption, "pending_costs": pending_costs, "blocking_issues": blockers,
        "recommendation": "PARTICIPATION_NOT_CLEARED" if blockers else ("MEETS_TARGET_MARGIN" if margin >= args.target_margin else "BELOW_TARGET"),
        "calculated_at": args.calculated_at
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario-id", default="CENARIO-001")
    parser.add_argument("--opportunity-id", required=True)
    parser.add_argument("--item-id", required=True)
    parser.add_argument("--scenario-name", default="base")
    parser.add_argument("--quantity", type=dec, required=True)
    parser.add_argument("--sale-price", type=dec, required=True, help="sale price per unit")
    parser.add_argument("--acquisition-price", type=dec, required=True, help="acquisition price per unit")
    parser.add_argument("--tax-rate", type=dec, default=Decimal("0"), help="incremental tax rate on revenue as decimal; do not infer")
    parser.add_argument("--das-allocated", type=dec, default=ZERO)
    parser.add_argument("--freight", type=dec, default=ZERO)
    parser.add_argument("--local-delivery", type=dec, default=ZERO)
    parser.add_argument("--handling", type=dec, default=ZERO)
    parser.add_argument("--financial-costs", type=dec, default=ZERO)
    parser.add_argument("--other-costs", type=dec, default=ZERO)
    parser.add_argument("--contingency", type=dec, default=ZERO)
    parser.add_argument("--target-margin", type=dec, default=Decimal("0.50"), help="target margin on revenue as decimal")
    parser.add_argument("--tax-confirmed", action="store_true")
    parser.add_argument("--freight-confirmed", action="store_true")
    parser.add_argument("--technical-compliance-confirmed", action="store_true")
    parser.add_argument("--supplier-capacity-confirmed", action="store_true")
    parser.add_argument("--pending-cost", action="append", default=[])
    parser.add_argument("--assumption", action="append", default=[])
    parser.add_argument("--calculated-at", default="2026-10-22T00:00:00-03:00")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = calculate(args)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
