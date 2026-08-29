#!/usr/bin/env python
"""Punto de entrada: corre la valoracion completa de una empresa desde su CSV.

Uso:
    python main.py data/example_adbe.csv
"""
from __future__ import annotations

import sys

from jmr_valuation.io.inputs import load_company_inputs
from jmr_valuation.valuation import run_valuation


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Uso: python main.py <ruta_al_csv_de_la_empresa>")
        return 1

    inputs = load_company_inputs(argv[1])
    report = run_valuation(inputs)
    print(report.summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
