Artifact Schema
===============

Purpose
-------

This page documents the frozen benchmark artifact schema used by the SHAP benchmark export flow and the downstream analytics consumers.

The schema is intentionally descriptive and reconstructible. It captures what the exporter produces, not a separate analytical interpretation layer.

Schema layers
-------------

The exported bundle has two main layers:

- ``metadata`` for producer and contract identity fields
- ``normalizedRows`` plus summary projections for the benchmark data itself

The current schema contract is described in the following repository references:

- ``docs/benchmark/PHASE3_ARTIFACT_SCHEMA_FREEZE.md``
- ``docs/research/DATA_DICTIONARY.md``
- ``lib/shapBundleAnalytics.ts``

Normalized row schema
---------------------

Each normalized row records one scored contract outcome for one archived run.

Required fields:

.. list-table::
   :header-rows: 1

   * - Field
     - Type
     - Meaning
   * - ``runId``
     - string
     - Archived run identifier.
   * - ``promptId``
     - string
     - Prompt identifier associated with the run.
   * - ``modelId``
     - string
     - Model identifier for the run.
   * - ``keyId``
     - string
     - Contract key identifier.
   * - ``section``
     - string
     - Prompt or contract section label for the key.
   * - ``outcome``
     - string enum
     - Deterministic outcome label: ``present``, ``missing``, ``contradicted``, or ``not_applicable``.
   * - ``severity``
     - string
     - Requirement severity or fallback severity label.

Schema rule
-----------

The normalized row is the canonical source of truth for descriptive benchmark artifacts.

Any summary table or report derived from the bundle must remain reconstructible from these rows.

Summary projections
-------------------

Summary projections are counts-only groupings over normalized rows.

Key outcome counts
^^^^^^^^^^^^^^^^^^

Grouped by ``keyId`` and ``outcome``.

Section outcome counts
^^^^^^^^^^^^^^^^^^^^^^

Grouped by ``section`` and ``outcome``.

Model outcome counts
^^^^^^^^^^^^^^^^^^^^

Grouped by ``modelId`` and ``outcome``.

Model section outcome counts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Grouped by ``modelId``, ``section``, and ``outcome``.

Bundle metadata
---------------

The bundle metadata records producer identity and benchmark lineage information.

Current fields used by the export flow include:

- ``bundle_id``
- ``artifact_schema_version``
- ``generated_at``
- ``generated_by_commit``
- ``promptTemplateId``
- ``promptTemplateVersion``
- ``scoreSpecId``
- ``scoreSpecVersion``
- ``selectedRunCount``
- ``scoredRunCount``

Versioning rules
----------------

The schema freeze contract uses the following compatibility expectations:

- additive optional fields require a minor version bump
- field renames, removals, or semantic redefinitions are breaking changes
- consumers should treat the normalized row schema and projection keys as stable within one artifact major version

Producer and consumer contract
------------------------------

Producer responsibilities:

- emit reconstructible normalized rows
- keep counts-only projections derivable from those rows
- preserve provenance fields needed for audit and replication

Consumer responsibilities:

- do not redefine schema semantics in analytics notebooks or dashboards
- treat bundle data as the source of truth for descriptive reporting

Scope limits
------------

This schema is descriptive only.

It explicitly excludes:

- percentages
- statistics
- similarity metrics
- weighted values

Those belong to reporting conventions or downstream analytics, not the frozen artifact schema itself.