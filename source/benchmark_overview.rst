Benchmark Overview
==================

Purpose
-------

The SHAP benchmark evaluates archived explainer runs as governed artifacts rather than informal UI outputs.

This page is a companion overview. The normative specification lives in :doc:`benchmark_specification_v1_0`.

At a high level, the benchmark treats each scored run as a traceable unit with:

- a prompt contract
- a score specification
- an extraction schema
- a reproducible archive bundle

Core repository references
--------------------------

The main benchmark governance and artifact references remain the Markdown sources already present in the repository:

- ``docs/benchmark/BENCHMARK_SPECIFICATION.md``
- ``docs/benchmark/BENCHMARK_ANALYTICS.md``
- ``docs/benchmark/PHASE3_SCORE_RESULTS_ARTIFACTS.md``
- ``docs/research/BENCHMARK_VERSION_1_0.md``

This Sphinx tree does not replace those sources. It organizes the most important operational and user-facing concepts into a form that can be built as a documentation site.

Architecture checkpoint
-----------------------

The benchmark pipeline is intentionally layered:

.. code-block:: text

   Prompt Template
       |
       v
   PromptScoreKeySpec (versioned + validated)
       |
       v
   CaseEnvelope + ResponseExtraction
       |
       v
   ScoreResult
       |
       v
   Consistency and variability analysis

This separation matters because it keeps benchmark interpretation stable:

- extraction is distinct from scoring
- scoring is distinct from packaging
- packaging is distinct from downstream analytics

Canonical benchmark artifact layers
-----------------------------------

The current implementation exposes four practical artifact layers:

1. Archived explainer run folders under ``xai/logs/explainer_runs``.
2. Scored normalized rows and count outputs produced in the developer flow.
3. Master bundles written under ``xai/logs/explainer_runs/bundles``.
4. Downstream benchmark tables, paper artifacts, and analytics exports.

Documentation intent
--------------------

The remaining pages in this Sphinx project focus on:

- where scoring actually happens
- how later scripts find their inputs
- the formulas presently implemented
- how to rebuild and extend this documentation process later

Historical implementation notes live in the implementation repository and are not included in this documentation-only repository.