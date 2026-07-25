#!/usr/bin/env python3
"""Render generated product docs from private scenarios.json files."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from product_docs import ROOT, iter_products


def render_product(config: dict[str, object]) -> None:
    scenarios_path = ROOT / str(config["scenarios_path"])
    output_dir = ROOT / str(config["output_dir"])
    if not scenarios_path.exists():
        raise SystemExit(f"Missing scenario source: {scenarios_path}")
    output_dir.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env.update(
        {
            "AIWATCHER_SCENARIOS_PATH": str(scenarios_path),
            "AIWATCHER_SCENARIO_OUT_DIR": str(output_dir),
            "AIWATCHER_PRODUCT_LABEL": str(config["label"]),
            "AIWATCHER_REVIEW_HOME_TITLE": str(config.get("review_home_title", f"{config['label']} Review Home")),
        }
    )
    if config.get("extra_nav"):
        env["AIWATCHER_EXTRA_NAV_JSON"] = json.dumps(config["extra_nav"])
    if config.get("extra_review_sections"):
        env["AIWATCHER_EXTRA_REVIEW_SECTIONS_JSON"] = json.dumps(config["extra_review_sections"])
    if config.get("implementation_order"):
        env["AIWATCHER_IMPLEMENTATION_ORDER_JSON"] = json.dumps(config["implementation_order"])
    if config.get("platform_guidance"):
        env["AIWATCHER_PLATFORM_GUIDANCE"] = str(config["platform_guidance"])
    if config.get("review_sections"):
        env["AIWATCHER_REVIEW_SECTIONS_JSON"] = json.dumps(config["review_sections"])
    if config.get("review_priority_limit"):
        env["AIWATCHER_REVIEW_PRIORITY_LIMIT"] = str(config["review_priority_limit"])

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_scenario_docs.py")],
        check=True,
        cwd=ROOT,
        env=env,
    )
    html_out = output_dir / "aiwatcher-scenario-tests.html"
    if html_out.exists():
        html_out.replace(output_dir / "index.html")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", help="Render one product slug from .github/product-docs.json.")
    args = parser.parse_args()

    for config in iter_products(args.product):
        render_product(config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
