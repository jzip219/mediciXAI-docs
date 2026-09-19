Bundle Schema Reference
=======================

Purpose
-------

This page provides a focused schema reference for normalized rows and master bundle payloads used by benchmark analytics.

See Also
--------

- :doc:`score_key_taxonomy`
- :doc:`inter_intra_model_statistics`
- :doc:`validation_conformance_workflow`

Authoritative implementation references
---------------------------------------

- ``lib/shapBundleAnalytics.ts``
- ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py``
- :doc:`artifact_schema`

Normalized row schema
---------------------

Each normalized row represents one key outcome in one run.

.. list-table::
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``runId``
     - string
     - Archived run identifier.
   * - ``promptId``
     - string
     - Prompt identifier.
   * - ``modelId``
     - string
     - Model identifier.
   * - ``keyId``
     - string
     - Score-key identifier.
   * - ``section``
     - string
     - Prompt/contract section label.
   * - ``outcome``
     - enum
     - ``present`` | ``missing`` | ``contradicted`` | ``not_applicable``.
   * - ``severity``
     - string
     - Severity label.

Master bundle shape
-------------------

The analytics parser expects a bundle object containing:

- ``metadata``
- ``outcomeBundle.normalizedRows``
- optional ``runSummaryRows``
- optional ``scoredRuns``

Metadata fields currently consumed include:

- ``bundle_id``
- ``artifact_schema_version``
- ``generated_at``
- ``promptTemplateId``
- ``promptTemplateVersion``
- ``scoreSpecId``
- ``scoreSpecVersion``
- ``selectedRunCount``
- ``scoredRunCount``

Run summary row schema
----------------------

When present, each ``runSummaryRows`` entry may include:

- ``runId``
- ``readiness``
- ``present``
- ``missing``
- ``contradicted``
- ``notApplicable``
- ``integrityIssues``
- ``missingRequiredKeys``
- ``contradictedKeys``
- ``blockingReasons``
- ``startedAt``

Scored run schema
-----------------

When present, each ``scoredRuns`` entry may include:

- ``runId``
- ``promptId``
- ``modelId``
- ``provider``
- ``status``
- ``readinessForScoring``
- ``extractionTextLength``
- ``missingRequiredKeyCount``
- ``contradictedKeyCount``
- ``integrityIssueCount``
- ``startedAt``

Schema constraints
------------------

- ``outcomeBundle.normalizedRows`` is required for analytics parsing.
- Rows failing required field/type checks are dropped by parser validation.
- Descriptive summary surfaces must remain reconstructible from normalized rows.

Relationship to normative schema
--------------------------------

This page is a reference companion. Normative schema boundary and compatibility posture remain defined in :doc:`artifact_schema`.
