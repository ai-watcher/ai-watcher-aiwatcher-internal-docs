# AIWatcher Internal Docs

Owner-only status and planning docs for AIWatcher.

This repository exists because `ai-watcher/aiwatcher-local` is public. Keep
scenario status, planning details, roadmap decisions, and generated review
surfaces here instead of in the OSS repo.

## Layout

```text
aiwatcher-local/
  scenarios.json
  index.html
  scenario-status.md
  release-checklist.md
```

- `aiwatcher-local/scenarios.json` is the source of truth.
- `index.html`, `scenario-status.md`, and `release-checklist.md` are generated.
- Do not put secrets in this repo. GitHub Actions secrets stay on the public
  `ai-watcher/aiwatcher-local` repo.

