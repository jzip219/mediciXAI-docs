Benchmark Design Rationale
==========================

Purpose
-------

This chapter records why the benchmark was designed the way it was.

It explains the intent behind the release shape, not the implementation mechanics.

Why 5 repetitions?
------------------

Five repetitions give the benchmark enough repeated observations to measure run-to-run variability while keeping the release manageable for manual review and archival storage.

The choice also enables pairwise stability analysis, because five outputs yield ten pairwise comparisons.

Why 4 subjects?
---------------

The current release uses four subjects because the benchmark was scoped to a compact, reviewable cohort that still exercises cross-subject comparison.

This is a release parameter, not a specification constraint.

Why 3 models?
-------------

Three models were enough to test inter-model ranking, tie-breaking, and repeatability without turning the release into a large-scale evaluation problem.

Why cosine similarity?
----------------------

Cosine similarity is a stable and interpretable way to compare embedding vectors across repeated outputs.

It is sensitive to semantic proximity without requiring a separate symbolic alignment step.

Why MiniLM?
-----------

The ``all-MiniLM-L6-v2`` embedding model is compact, deterministic enough for reproducible evaluation, and lightweight enough to run in a benchmark pipeline without excessive resource cost.

Its revision is pinned so the metric remains reproducible across time.

Why SD?
-------

Standard deviation is a familiar dispersion measure for repeated quantitative observations.

It is easy to explain, easy to reproduce, and useful for both per-run and per-model variation summaries.

Why pooled SD?
--------------

Pooled SD provides a single measure of within-subject variability across multiple subject cells for a model.

It is more appropriate than a plain aggregate SD when the goal is repeatability rather than overall spread.

Why bootstrap?
--------------

Bootstrap confidence intervals provide uncertainty estimates without assuming a fragile closed-form distributional model.

The deterministic bootstrap approach keeps the analysis reproducible.

Why deterministic scoring?
--------------------------

Deterministic scoring makes the benchmark auditable.

If the same bundle is scored again, the same result should appear.

Why provenance?
---------------

Provenance is required so future readers can reconstruct how a release was produced and verify that nothing was silently substituted.

Why checksum?
-------------

Checksums provide a quick integrity test for stored artifacts and help distinguish an archived file from an altered copy.

Why three evidence levels?
--------------------------

The repository currently distinguishes raw run-level observations, master-bundle recomputation, and summary-derived telemetry.

Those layers answer different questions and should not be collapsed into one undifferentiated reporting mode.

Why direct computation over summary reconstruction?
---------------------------------------------------

Direct computation is preferable when the underlying run records are available because it preserves the richest traceability.

Summary reconstruction is still useful when the bundle is the only available artifact or when the pipeline is intentionally packaging already-computed outputs.

Design principle
----------------

The benchmark should be able to grow in size without changing its meaning.

That is why the specification freezes design and formula semantics while leaving release parameters flexible.