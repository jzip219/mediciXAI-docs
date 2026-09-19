import os

project = "MedixAI Benchmark Documentation"
author = "MedixAI"
copyright = "2026, MedixAI"

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.duration",
    "sphinx.ext.mathjax",
    "sphinx.ext.extlinks",
]

templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
autosectionlabel_prefix_document = True

html_theme = "sphinx_rtd_theme"
html_static_path = []

master_doc = "index"

# Internal repository links are always available for internal documentation builds.
INTERNAL_REPO_ROOT = os.getenv(
    "MEDIXAI_INTERNAL_REPO",
    "file:///C:/Users/jzip/Desktop/medixai",
)

# Public repository links are optional and only enabled when explicitly configured.
PUBLIC_REPO_BLOB_BASE = os.getenv(
    "MEDIXAI_REPO_BLOB_BASE_URL",
    "",
)

DOCUMENTATION_MODE = os.getenv(
    "MEDIXAI_DOC_MODE",
    "internal",
).strip().lower()

if DOCUMENTATION_MODE not in {"internal", "public"}:
    raise RuntimeError(
        "MEDIXAI_DOC_MODE must be one of: internal, public."
    )

if DOCUMENTATION_MODE == "public" and not PUBLIC_REPO_BLOB_BASE:
    raise RuntimeError(
        "MEDIXAI_REPO_BLOB_BASE_URL must be set when MEDIXAI_DOC_MODE=public."
    )

extlinks = {
    "internalrepo": (
        INTERNAL_REPO_ROOT.rstrip("/") + "/%s",
        "%s",
    ),
}

if PUBLIC_REPO_BLOB_BASE:
    extlinks["repo"] = (
        PUBLIC_REPO_BLOB_BASE.rstrip("/") + "/%s",
        "%s",
    )

doc_mode_label = (
    "Internal Development Documentation"
    if DOCUMENTATION_MODE == "internal"
    else "Public Benchmark Specification"
)

public_repo_label = (
    "Configured"
    if PUBLIC_REPO_BLOB_BASE
    else "Not configured for this build"
)

rst_epilog = (
    f".. |documentation_mode| replace:: {doc_mode_label}\n"
    f".. |public_repo_status| replace:: {public_repo_label}\n"
)