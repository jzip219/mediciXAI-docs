Reporting Conventions
=====================

Purpose
-------

This page defines how benchmark outputs should be reported to users when the source data comes from the SHAP benchmark artifact pipeline.

It separates descriptive telemetry from normative benchmark reporting so the same metric names are not reused with different meanings.

Reporting layers
----------------

There are two reporting layers in the current repository:

1. Telemetry and artifact reconstruction reports.
2. Benchmark-release and user-facing analytic reports.

Telemetry and artifact reconstruction reports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are operational outputs used to rebuild tables and packages from stored bundles.

Relevant scripts:

- ``scripts/generate-paper-telemetry-tables.js``
- ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py``
- ``scripts/build-paper-artifacts.py``

They report metrics such as:

- run-level present-rate
- run-level required-risk rate
- model means
- run dispersion
- semantic stability when embeddings are available

Benchmark-release and user-facing analytic reports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are the reports that should be read as benchmark interpretation artifacts.

Relevant references:

- ``docs/benchmark/BENCHMARK_SPECIFICATION.md``
- ``docs/benchmark/BENCHMARK_ANALYTICS.md``
- ``docs/benchmark/PHASE3_SCORE_RESULTS_ARTIFACTS.md``

Metric conventions
------------------

Present-rate
^^^^^^^^^^^^

Present-rate is the share of normalized rows whose outcome is ``present``.

.. math::

   \mathrm{presentRatePct} = \frac{N_{\mathrm{present}}}{N_{\mathrm{total}}} \times 100

Required-risk rate
^^^^^^^^^^^^^^^^^^

Required-risk is the share of normalized rows that are required and not present.

.. math::

   \mathrm{requiredRiskRatePct} = \frac{N_{\mathrm{severity=required\ and\ outcome\neq present}}}{N_{\mathrm{total}}} \times 100

This convention is used consistently in the current telemetry path and in the Python master-bundle recomputation path.

Ranking convention
------------------

When a report sorts models for human review, the ordering is:

1. lower required-risk first
2. higher present-rate second
3. model identifier as a deterministic tie-breaker

This mirrors the implementation in the paper-artifact builder and should be preserved whenever the generated tables are intended for comparison rather than raw inspection.

Dispersion conventions
----------------------

Use the following language carefully:

- ``sdPresentRatePct`` and ``sdRequiredRiskRatePct`` describe dispersion across repeated runs.
- ``withinSubjectMeanSd...`` describes average within-subject variability across subject cells.
- ``withinSubjectPooledSd...`` describes pooled within-subject variability.

Do not use these terms interchangeably.

Semantic stability convention
-----------------------------

When embedding-backed text comparison is available, report semantic stability as mean pairwise cosine similarity across the repeated outputs in a subject-model cell.

If embeddings are unavailable, do not substitute a different statistic under the same label.

Use one of the following instead:

- omit the semantic metric
- mark it as unavailable
- explain that only score-dispersion proxies are available

Reporting guardrails
--------------------

1. Do not mix bundle reconstruction metrics with normative benchmark-release claims without labeling the layer.
2. Do not change metric names if the underlying computation changes.
3. Do not move schema meaning from the artifact contract into a reporting page.
4. If a metric becomes governed, update the formulas page and the schema page together.

Recommended wording
-------------------

For operational exports, prefer wording like:

- "reconstructed from master bundle"
- "telemetry-aligned"
- "descriptive artifact output"

For benchmark interpretation, prefer wording like:

- "benchmark-release summary"
- "normative metric"
- "frozen artifact schema"

This keeps the documentation clear about what is reconstructed, what is reported, and what is normative.