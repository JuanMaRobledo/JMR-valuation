#!/usr/bin/env python3
"""Colombia entrypoint, deliberately independent of SEC/US valuation.

Calls the canonical Colombia collector in the web repository so the app and
CLI use the SAME identity, currency, evidence and missing-data contract.
No US CompanyInputs defaults, SEC loader, filled company model or automatic
publication is used. No credentials are needed for the data download.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ticker", help="Local Yahoo symbol, e.g. ECOPETROL.CL, not an ADR")
    parser.add_argument("--web-repo", required=True, type=Path,
                        help="Checkout of JuanMaRobledo/Modelo-JMR containing the Colombia module")
    parser.add_argument("--output", required=True, type=Path,
                        help="Parent of the fresh colombia/ticker/run-id working directory")
    args = parser.parse_args()
    node = shutil.which("node")
    if not node:
        parser.error("Node.js 20+ is required for the canonical Colombia collector")
    script = args.web_repo.resolve() / "scripts" / "colombia-datos.mjs"
    if not script.is_file():
        parser.error(f"Colombia collector not found: {script}")
    return subprocess.run([node, str(script), args.ticker, "--output", str(args.output.resolve())],
                          check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
