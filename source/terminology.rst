Terminology
===========

Purpose
-------

This page freezes the benchmark vocabulary used across the specification, Sphinx documentation, scripts, and reports.

Canonical Terms
---------------

Benchmark Response
  One model response for one subject in one execution.

Run
  One archived execution record with traceable files, metadata, and outputs.

Execution
  One benchmark run instance used to produce a bundle or report.

Subject
  One benchmark subject identifier.

Prompt
  One benchmark prompt identifier associated with a subject and contract lineage.

Present Rate
  The share of normalized rows whose outcome is ``present``.

Required-Risk Rate
  The share of normalized rows whose severity is required and whose outcome is not ``present``.

Semantic Stability
  Mean pairwise cosine similarity across repeated outputs in a subject-model cell when embeddings are available.

Semantic Dispersion
  ``1 - Semantic Stability`` for the same repeated-output cell.

Within-subject SD
  The sample standard deviation of a metric within one subject cell.

Pooled SD
  The pooled within-subject standard deviation across multiple subject cells for one model.

Master Bundle
  The stored JSON container that packages normalized rows, summary projections, metadata, and run identifiers for reproducible downstream work.

Telemetry
  Operational reconstruction output derived from a stored master bundle or archived run set.

Paper Artifact
  A reproducible output intended for paper tables, appendix material, or publication support.

Normalized Row
  One canonical scored contract outcome row with run, prompt, model, key, section, outcome, and severity fields.

Summary Projection
  A counts-only grouping derived from normalized rows.

Benchmark Release
  One declared set of benchmark parameters and frozen versions used for a reproducible evaluation run.

Benchmark Specification
  The normative document that defines benchmark meaning, formulas, schema, and validation expectations.

Vocabulary rule
---------------

Use these names exactly in the documentation and code-aligned reporting.

Do not introduce synonyms when the same concept already has a frozen term.