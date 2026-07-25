#!/usr/bin/env python3
"""Shared helpers for product-doc automation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / ".github" / "product-docs.json"


def load_config() -> dict[str, Any]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def product_config(product: str) -> dict[str, Any]:
    products = load_config().get("products", {})
    if product not in products:
        known = ", ".join(sorted(products)) or "none"
        raise SystemExit(f"Unknown product '{product}'. Known products: {known}")
    config = dict(products[product])
    config["slug"] = product
    return config


def iter_products(selected: str | None = None) -> list[dict[str, Any]]:
    config = load_config()
    products = config.get("products", {})
    if selected:
        return [product_config(selected)]
    return [dict(value, slug=key) for key, value in products.items()]
