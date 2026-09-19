Inter-Model and Intra-Model Statistics
======================================

Purpose
-------

This page documents the inter-model and intra-model statistical layers used in benchmark analytics outputs.

See Also
--------

- :doc:`score_key_taxonomy`
- :doc:`bundle_schema_reference`
- :doc:`validation_conformance_workflow`

Implementation source
---------------------

The analytics/statistical definitions on this page are implemented in ``lib/shapBundleAnalytics.ts``.

Inter-model report surface
--------------------------

Core inter-model outputs include:

- model summary rows
- pairwise model deltas
- section variability rows
- section spread rows
- aggregate dispersion metrics:
  - present-rate standard deviation
  - required-risk-rate standard deviation
  - required-risk-rate coefficient of variation

Advanced inter-model outputs include:

- Kendall's W by dimension
- bootstrap confidence intervals by dimension
- mixed-effects readiness gate

Intra-model report surface
--------------------------

Core intra-model outputs include:

- run-level score rows
- model-level summary rows:
  - mean/sd present rate
  - mean/sd required-risk rate
  - exact outcome agreement
  - mean pairwise Jaccard overlap

Advanced intra-model outputs include:

- ICC by dimension
- bootstrap confidence intervals by dimension
- mixed-effects readiness gate

For a cross-layer map of semantic-stability metrics and supplementary outcome-consistency analytics, see :doc:`appendix_metric_traceability`.

Governance defaults
-------------------

Current analytics governance defaults (``ADVANCED_STATS_GOVERNANCE``):

- minimumPrompts = 20
- minimumModels = 3
- minimumRunsPerModelPrompt = 3
- matrixCompletenessThresholdPct = 80
- bootstrap resamples = 2000
- bootstrap seed = 20260709
- bootstrap percentile interval = [2.5, 97.5]

Gate thresholds
---------------

Kendall's W gate:

- min prompts = 3
- min models = 3
- complete coverage required

ICC gate:

- min prompts with repeats = 2
- min runs per prompt = 2

Interpretation bands
--------------------

ICC bands:

- poor: -1.0 to 0.5
- moderate: 0.5 to 0.75
- good: 0.75 to 0.9
- excellent: 0.9 to 1.0

Kendall's W bands:

- weak: 0.0 to 0.3
- moderate: 0.3 to 0.6
- strong: 0.6 to 0.8
- very strong: 0.8 to 1.0

Readiness semantics
-------------------

The mixed-effects readiness surface is a gate/readiness signal. It does not itself execute mixed-effects modeling in this layer.

Release reporting note
----------------------

Statistical outputs must be interpreted with the declared governance/version metadata that accompanies exports.
