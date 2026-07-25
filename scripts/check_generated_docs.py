#!/usr/bin/env python3
"""Fail when generated product docs are stale."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from render_product_docs import main as render_main

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", help="Check one product slug from .github/product-docs.json.")
    args = parser.parse_args()

    render_args = ["render_product_docs.py"]
    if args.product:
        render_args.extend(["--product", args.product])
    old_argv = sys.argv
    try:
        sys.argv = render_args
        render_main()
    finally:
        sys.argv = old_argv

    result = subprocess.run(
        ["git", "diff", "--exit-code", "--", "aiwatcher-local", "enterprise"],
        cwd=ROOT,
        text=True,
    )
    if result.returncode:
        print(
            "Generated docs are stale. Run `python3 scripts/render_product_docs.py` "
            "and commit the regenerated files.",
            file=sys.stderr,
        )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
