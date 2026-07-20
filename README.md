# AIWatcher Internal Docs

Owner-only status and planning docs for AIWatcher.

This repository exists because `ai-watcher/aiwatcher-local` is public. Keep
scenario status, planning details, roadmap decisions, and generated review
surfaces here instead of in the OSS repo.

## Layout

```text
aiwatcher-local/
  scenarios.json
  README.md
  scope.md
  requirements.md
  platforms.md
  test-cases.md
  index.html

enterprise/
  scenarios.json
  README.md
  scope.md
  requirements.md
  platforms.md
  test-cases.md
  propagation-matrix.md
  index.html
```

- `*/scenarios.json` is the source of truth.
- `README.md`, `scope.md`, `requirements.md`, `platforms.md`,
  `test-cases.md`, `propagation-matrix.md`, and `index.html` are generated or
  derived review surfaces.
- Use Markdown pages for GitHub review.
- Use `index.html` for offline interactive viewing.
- Do not put secrets in this repo. GitHub Actions secrets stay on the public
  `ai-watcher/aiwatcher-local` repo or the private enterprise repo.

## Review Hubs

- [AIWatcher Local](aiwatcher-local/README.md)
- [AIWatcher Enterprise](enterprise/README.md)
- [OSS to Enterprise Propagation Matrix](enterprise/propagation-matrix.md)
