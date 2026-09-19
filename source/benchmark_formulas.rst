Benchmark Formulas
==================

Scope
-----

This page records the formulas that are currently implemented in the benchmark pipeline.

It is intentionally explicit about where each formula comes from in the codebase.

Key-level outcome precedence
----------------------------

In ``lib/xaiScoringCore.ts``, each evaluated key maps to exactly one primary outcome.

The implemented precedence is:

1. If the extracted state is ``present``, the key is ``satisfied``.
2. If the extracted state is ``contradicted``, the key is ``contradicted``.
3. If the key is required and not present, the key is ``missing_required``.
4. If the extracted state is ``not_applicable``, the key is ``not_applicable``.
5. Otherwise the key is ``unresolved_non_required``.

This is not yet a scalar score. It is a deterministic classification scheme over benchmark keys.

Run-level present-rate
----------------------

Both downstream aggregation paths compute a run-level present-rate percentage.

The formula is:

.. math::

   \mathrm{presentRatePct} = \frac{N_{\mathrm{present}}}{N_{\mathrm{total\ keys}}} \times 100

where:

- :math:`N_{\mathrm{present}}` is the number of normalized rows with outcome ``present``
- :math:`N_{\mathrm{total\ keys}}` is the total number of normalized rows for that run

Derivation note:

- normalized rows are grouped by run identifier
- each row contributes one score-key outcome to the run total
- the numerator counts only rows with outcome ``present``

Run-level required-risk rate
----------------------------

The telemetry JavaScript path and the Python master-bundle recomputation path both use the same definition:

.. math::

   \mathrm{requiredRiskRatePct} = \frac{N_{\mathrm{severity=required\ and\ outcome\neq present}}}{N_{\mathrm{total\ keys}}} \times 100

This is implemented in:

- ``scripts/generate-paper-telemetry-tables.js`` when reconstructing run-level telemetry rows
- ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py`` when recomputing run-level records from a master bundle

Symbol definitions:

- :math:`N_{\mathrm{severity=required\ and\ outcome\neq present}}` counts normalized rows whose severity is ``required`` and whose outcome is anything other than ``present``
- :math:`N_{\mathrm{total\ keys}}` is the total number of normalized rows for the run

Interpretation note:

This definition intentionally excludes non-required failures from the required-risk numerator.

Model-level means
-----------------

When a downstream table summarizes a model across runs, the implemented mean is the arithmetic mean.

For any run-level metric :math:`x_1, x_2, \dots, x_n`:

.. math::

   \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i

This is used for:

- mean present-rate
- mean required-risk rate
- mean within-subject dispersion summaries

Derivation note:

Model-level aggregates are computed after run-level metrics are reconstructed, so the mean is over runs rather than over raw normalized rows.

Standard deviation conventions
------------------------------

The Python benchmark table generator uses sample standard deviation when run-level records are available.

For :math:`n \ge 2` observations:

.. math::

   s = \sqrt{\frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2}

Within the code, this is produced by Python's ``statistics.stdev``.

The JavaScript telemetry helper currently uses population standard deviation for its own immediate summaries, while the Python benchmark table generator uses sample standard deviation when operating from run-level records. When normative reporting is finalized, one convention should be explicitly frozen for each reporting layer.

Within-subject pooled standard deviation
----------------------------------------

In ``generate_benchmark_tables.py``, pooled within-subject standard deviation is computed across subject cells for a model.

If subject cell :math:`j` has :math:`n_j` observations and sample SD :math:`s_j`, then:

.. math::

   s_{\mathrm{pooled}} = \sqrt{\frac{\sum_j (n_j - 1) s_j^2}{\sum_j (n_j - 1)}}

This is used for both:

- ``withinSubjectPooledSdPresentRatePct``
- ``withinSubjectPooledSdRequiredRiskRatePct``

Derivation note:

Each subject cell first produces its own sample standard deviation, then those subject-level variances are pooled with the usual :math:`n_j - 1` weighting.

Within-subject mean standard deviation
--------------------------------------

If the within-subject sample standard deviations for a model are :math:`s_1, s_2, \dots, s_k`, the mean within-subject SD is:

.. math::

   \mathrm{meanWithinSubjectSd} = \frac{1}{k} \sum_{j=1}^{k} s_j

This is used for both:

- ``withinSubjectMeanSdPresentRatePct``
- ``withinSubjectMeanSdRequiredRiskRatePct``

This metric answers a different question than pooled SD. It treats each subject cell equally after each cell's SD has been estimated.

Semantic stability
------------------

When ``sentence-transformers`` is installed and run folders are available, ``generate_benchmark_tables.py`` computes semantic stability from repeated response texts.

For the five repeated outputs in one subject-model cell, let the cosine similarities across all unique response pairs be:

.. math::

   c_1, c_2, \dots, c_{10}

because five texts yield :math:`\binom{5}{2} = 10` unique pairs.

Then the implemented semantic stability is:

.. math::

   \mathrm{meanWithinSubjectCosineSimilarity} = \frac{1}{10} \sum_{i=1}^{10} c_i

and semantic dispersion is:

.. math::

   \mathrm{semanticDispersion} = 1 - \mathrm{meanWithinSubjectCosineSimilarity}

Aggregation gate
----------------

Model-level semantic aggregation is only emitted when all four subject cells are complete.

That means the pipeline requires:

- 4 computed subject cells per model
- 20 total texts per model
- 40 pairwise similarities per model

Ranking rule
------------

Benchmark table ranking is currently applied as:

.. math::

   	ext{rank key} = (\mathrm{meanRequiredRiskRatePct}\ \uparrow,\ \mathrm{meanPresentRatePct}\ \downarrow,\ \mathrm{modelId}\ \uparrow)

where:

- lower required-risk is better
- higher present-rate is better
- model identifier ordering is used only as a deterministic final tie-breaker

Current status note
-------------------

This page is a code-aligned formula inventory and a suitable base for a future normative equations chapter.