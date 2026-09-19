# Sphinx Docs

This repository contains the public Sphinx project for the MedixAI benchmark documentation.

## Why this exists

The repository is intentionally documentation-only. Implementation code, private datasets, runtime logs, and generated benchmark results remain outside this repository.

## Install

From this repository's root:

```powershell
python -m pip install -r requirements.txt
```

## Build HTML

From this repository's root:

```powershell
python -m sphinx -b html source build/html
```

Or from inside `docs/sphinx` on Windows:

```powershell
.\make.bat html
```

## Publish on GitHub Pages

The repository workflow at `.github/workflows/pages.yml` builds the public documentation and deploys it to GitHub Pages when changes are pushed to `main`. Generated HTML is uploaded as a Pages artifact; `build/` does not need to be committed.

In the GitHub repository settings, open **Pages** and set **Build and deployment** to **GitHub Actions**. After the workflow completes, GitHub displays the public documentation URL in the workflow summary and Pages settings.

The workflow builds with `MEDIXAI_DOC_MODE=public` and sets `MEDIXAI_REPO_BLOB_BASE_URL` to the repository commit being built. This keeps repository links usable on GitHub without exposing local filesystem paths.

## Build modes and environment variables

The Sphinx configuration supports two documentation modes:

- internal: default mode for internal development and internal repository links
- public: publication mode with optional public repository links

Environment variables:

- `MEDIXAI_DOC_MODE`: `internal` or `public` (default: `internal`)
- `MEDIXAI_INTERNAL_REPO`: internal repository root for `:internalrepo:` links
	- default: `file:///C:/Users/jzip/Desktop/medixai`
- `MEDIXAI_REPO_BLOB_BASE_URL`: public repository blob base URL (optional unless `MEDIXAI_DOC_MODE=public`)

Behavior summary:

- Internal mode builds without a public URL and keeps implementation references available through internal repository links.
- Public mode requires `MEDIXAI_REPO_BLOB_BASE_URL`; build fails if it is unset.

### Example: internal build

```powershell
$env:MEDIXAI_DOC_MODE='internal'
Remove-Item Env:MEDIXAI_REPO_BLOB_BASE_URL -ErrorAction SilentlyContinue
python -m sphinx -b html source build/html
python -m sphinx -b linkcheck source build/linkcheck
```

### Example: public build

```powershell
$env:MEDIXAI_DOC_MODE='public'
$env:MEDIXAI_REPO_BLOB_BASE_URL='https://github.com/<org>/<repo>/blob/main'
python -m sphinx -b html source build/html
python -m sphinx -b linkcheck source build/linkcheck
```

## Current scope

The initial Sphinx set documents:

- benchmark concepts and boundaries
- the benchmark scoring and packaging pipeline
- the benchmark formulas currently implemented
- the exact steps used to create and extend this Sphinx project later

## Important note

The telemetry path and the Python master-bundle recomputation path now use the same required-risk definition:

- required-risk = required, non-present rows divided by total normalized rows for the run

The formulas page documents that shared definition and preserves the code-path ownership for traceability.