Non-Normative Developer Appendix: Metric Traceability Across Evaluation Layers
===============================================================================

Boundary statement
------------------

This appendix documents implementation traceability for benchmark and analytics metrics.
It is non-normative and does not introduce, alter, or supersede benchmark requirements.

In the event of a conflict, the normative specification and requirements registry govern.

Primary normative anchors
-------------------------

- :doc:`benchmark_specification_v1_0`
- :doc:`requirements_registry`
- :doc:`benchmark_formulas`
- :doc:`conformance`

Purpose
-------

This map answers recurring developer and reviewer questions:

- where a metric is implemented,
- where the equation or procedure is validated,
- which layer is authoritative for published benchmark metrics,
- why Python and TypeScript components compute different consistency measures.

Traceability map
----------------

.. list-table::
   :header-rows: 1
   :widths: 20 26 28 26

   * - Paper / Analytics Metric
     - Purpose
     - Implementation
     - Validation
   * - Present Rate
     - Benchmark criterion satisfaction
     - ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py``
     - ``tests/unit/test_scoring_formulas.py``
   * - Required-Risk Rate
     - Required benchmark omissions and contradictions
     - ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py``
     - ``tests/unit/test_scoring_formulas.py``
   * - Within-subject SD
     - Numerical repeatability within subject/model cells
     - ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py``
     - ``tests/unit/test_repeatability_metrics.py``
   * - Pooled SD
     - Aggregate repeatability across subject cells
     - ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py``
     - ``tests/unit/test_repeatability_metrics.py``
   * - Mean pairwise cosine similarity
     - Semantic stability of repeated responses
     - ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py``
     - ``tests/unit/test_semantic_stability.py``
   * - Semantic dispersion
     - Semantic variability, defined as ``1 - cosine similarity``
     - ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py``
     - ``tests/unit/test_semantic_stability.py``
   * - Exact outcome agreement
     - Outcome consistency analytics over extracted benchmark outcomes
     - ``lib/shapBundleAnalytics.ts``
     - ``lib/__tests__/shapBundleAnalytics.fixtures.test.ts``
   * - Present-key Jaccard overlap
     - Outcome overlap analytics over extracted benchmark outcomes
     - ``lib/shapBundleAnalytics.ts``
     - ``lib/__tests__/shapBundleAnalytics.fixtures.test.ts``

Evaluation-layer note
---------------------

The benchmark distinguishes between semantic stability and outcome consistency.

- Semantic stability is evaluated using embedding-based cosine similarity of repeated responses.
- Outcome consistency evaluates agreement and overlap of extracted benchmark criteria across repeated executions.

These measures are complementary and quantify different aspects of reproducibility.

Layer responsibilities
----------------------

The implementation separates responsibilities across three layers:

1. Benchmark Evaluation Layer (Python)

   - Computes published benchmark metrics and benchmark tables.
   - Normative implementation path for paper-aligned benchmark evaluation metrics.

2. Operational Analytics Layer (TypeScript)

   - Computes supplementary consistency analytics over extracted benchmark outcomes.
   - Supports application-facing quality analytics and operational monitoring.

3. Presentation Layer

   - Renders artifacts, tables, and reviewer/developer summaries.

Interpretation guidance
-----------------------

This layer split should not be framed as competing implementations.

- The Python benchmark path is authoritative for published benchmark evaluation metrics.
- The TypeScript analytics path provides supplementary operational analytics.

Both are expected to remain traceable to explicit metric definitions and test evidence.
