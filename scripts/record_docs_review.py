#!/usr/bin/env python3
"""Create a private docs-review record from source repo metadata."""

from __future__ import annotations

import os
import re
from datetime import datetime, timezone
from pathlib import Path

from product_docs import ROOT, product_config


def clean(value: str, fallback: str = "unknown") -> str:
    value = (value or "").strip()
    return value or fallback


def slugify(value: str) -> str:
    value = clean(value).lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    return value.strip("-") or "unknown"


def github_output(values: dict[str, str]) -> None:
    output = os.environ.get("GITHUB_OUTPUT")
    if not output:
        for key, value in values.items():
            print(f"{key}={value}")
        return
    with open(output, "a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def main() -> int:
    product = clean(os.environ.get("PRODUCT_DOCS_PRODUCT"), "aiwatcher-local")
    config = product_config(product)
    source_repo = clean(os.environ.get("PRODUCT_DOCS_SOURCE_REPO"), str(config.get("source_repo", "")))
    source_pr = clean(os.environ.get("PRODUCT_DOCS_SOURCE_PR"), "")
    source_sha = clean(os.environ.get("PRODUCT_DOCS_SOURCE_SHA"), "")
    source_ref = clean(os.environ.get("PRODUCT_DOCS_SOURCE_REF"), "")
    source_url = clean(os.environ.get("PRODUCT_DOCS_SOURCE_URL"), "")
    source_run_url = clean(os.environ.get("PRODUCT_DOCS_SOURCE_RUN_URL"), "")
    source_event = clean(os.environ.get("PRODUCT_DOCS_SOURCE_EVENT"), "")

    if source_pr:
        review_id = f"pr-{slugify(source_pr)}"
        source_label = f"{source_repo}#{source_pr}"
    elif source_sha:
        review_id = f"sha-{slugify(source_sha[:12])}"
        source_label = f"{source_repo}@{source_sha[:12]}"
    else:
        review_id = f"manual-{os.environ.get('GITHUB_RUN_ID', 'local')}"
        source_label = source_repo

    review_dir = ROOT / "reviews" / product
    review_dir.mkdir(parents=True, exist_ok=True)
    review_file = review_dir / f"{review_id}.md"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    checklist = [
        "- [ ] Does the product scenario source need a status or wording update?",
        "- [ ] Are generated Markdown/HTML docs refreshed from `scenarios.json`?",
        "- [ ] Does code behavior still match the product scenario/spec?",
    ]
    if config.get("propagation_required"):
        checklist.append("- [ ] Does `enterprise/propagation-matrix.md` need Propagate / Adapt / OSS-only / Enterprise-only updates?")
        checklist.append("- [ ] Does `enterprise/scenarios.json` need a corresponding scenario or status update?")

    lines = [
        f"# Product Docs Review: {config.get('label', product)}",
        "",
        f"Source: `{source_label}`",
        f"Source repo: `{source_repo}`",
        f"Source ref: `{source_ref}`",
        f"Source SHA: `{source_sha}`",
        f"Source event: `{source_event}`",
        f"Recorded: `{now}`",
        "",
    ]
    if source_url:
        lines.append(f"Source URL: {source_url}")
    if source_run_url:
        lines.append(f"Source run: {source_run_url}")
    lines.extend([
        "",
        "## Review Prompt",
        "",
        str(config.get("review_prompt", "Review product docs for this source change.")),
        "",
        "## Checklist",
        "",
        *checklist,
        "",
        "## Decision",
        "",
        "- [ ] `docs-impact:none`",
        "- [ ] `docs-impact:local`",
        "- [ ] `docs-impact:enterprise`",
        "- [ ] `docs-impact:local-and-enterprise`",
        "",
    ])
    review_file.write_text("\n".join(lines), encoding="utf-8")

    branch = f"docs/review/{product}-{review_id}"
    title = f"docs: review {config.get('label', product)} docs for {source_label}"
    github_output(
        {
            "branch": branch,
            "review_file": str(review_file.relative_to(ROOT)),
            "pr_title": title,
            "commit_message": title,
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
