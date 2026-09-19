Benchmark Pipeline
==================

Pipeline summary
----------------

The benchmark path has one scoring layer and several downstream aggregation layers.

.. code-block:: text

   Archived run files
       -> response extraction
       -> key-level scoring
       -> normalized rows and summary counts
       -> master bundle packaging
       -> telemetry and benchmark tables
       -> paper artifacts and statistics

Step 1: Archived run retrieval
------------------------------

Batch scoring starts in ``app/developer/page.tsx``.

For each selected run ID, the developer page calls:

- ``/api/explainer-runs/[runId]``

That route delegates to ``lib/explainerRunsArchive.ts``, which reads archived run files from:

- ``xai/logs/explainer_runs/google/succeeded/<runId>/``
- ``xai/logs/explainer_runs/openai/succeeded/<runId>/``
- ``xai/logs/explainer_runs/xai/succeeded/<runId>/``

and the equivalent ``failed`` folders when applicable.

Important archived inputs include:

- ``manifest.json``
- ``prompt.envelope.json``
- ``request.full.json``
- ``response.full.json``
- ``provider.response.raw.json``

Step 2: Response extraction
---------------------------

The extraction layer is implemented in ``lib/xaiScoringExtraction.ts``.

This layer converts archived response text and metadata into:

- section states
- key states
- normalized response text
- extraction parser metadata

This is where the system decides whether a contract element is:

- ``present``
- ``absent``
- ``ambiguous``
- ``contradicted``
- ``not_applicable``

Step 3: Key-level scoring
-------------------------

The scoring layer is implemented in ``lib/xaiScoringCore.ts``.

The main entrypoint is ``scoreShapResponse(envelope, spec, extraction)``.

This function consumes:

- the archived case envelope
- the released score specification from ``lib/xaiScoring.ts``
- the extracted key and section states

It produces a score result containing:

- integrity issues
- missing required keys
- contradicted keys
- not-applicable keys
- unresolved non-required keys
- readiness status

This is the primary benchmark scoring function.

Step 4: Normalized rows and count summaries
-------------------------------------------

After scoring selected archived runs, ``app/developer/page.tsx`` derives:

- normalized rows
- key outcome counts
- section outcome counts
- model outcome counts
- model section outcome counts

These outputs form the canonical benchmark summary surface used by later tooling.

Step 5: Master bundle packaging
-------------------------------

The same developer page constructs a master bundle containing:

- bundle metadata
- ``outcomeBundle.normalizedRows``
- summary count tables
- run summary rows
- selected run IDs

The bundle storage route is ``app/api/explainer-runs/bundle/route.ts``.

Stored bundle files are written to:

- ``xai/logs/explainer_runs/bundles``

with filenames shaped like:

- ``shap_master_bundle_<timestamp>_<sha256>.json``

Step 6: Telemetry-aligned benchmark table generation
----------------------------------------------------

The script ``scripts/generate-paper-telemetry-tables.js`` reads a master bundle and computes run-level summary outputs.

Input discovery rules:

- If ``--bundle`` is supplied, that file is used.
- Otherwise the script selects the newest ``shap_master_bundle_*.json`` file in ``xai/logs/explainer_runs/bundles``.

It reads:

- ``outcomeBundle.normalizedRows`` from the master bundle
- archived run metadata by resolving each run ID back to its archived run folder

It writes timestamped outputs such as:

- ``telemetry_paper_tables_*.metadata.jsonl``
- ``telemetry_paper_tables_*.table1_subject_summary.jsonl``
- ``telemetry_paper_tables_*.table2_aggregate_summary.jsonl``
- ``telemetry_paper_tables_*.subject_breakdown.jsonl``
- ``telemetry_paper_tables_*.consolidated_long.jsonl``
- ``telemetry_paper_tables_*.run_scores.jsonl``
- ``telemetry_paper_tables_*.md``

Step 7: Python benchmark table package generation
-------------------------------------------------

The script ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py`` is a downstream packaging layer, not the original key-level scorer.

For implementation and test traceability of the published metrics, see :doc:`appendix_metric_traceability`.

It accepts one of four input classes:

1. Summary JSON payloads.
2. Canonical run-level CSV, JSON, or JSONL records.
3. A directory or ZIP of telemetry summary files.
4. A stored master bundle.

When given a master bundle, it recomputes run-level records from ``outcomeBundle.normalizedRows``.

Its output directory contains files such as:

- ``<prefix>.metadata.json``
- ``<prefix>.table1.csv``
- ``<prefix>.table2.csv``
- ``<prefix>.subject_breakdown.csv``
- ``<prefix>.aspect_mapping.csv``
- ``<prefix>.tables.md``
- ``<prefix>.consolidated_long.jsonl``
- ``<prefix>.sha256.json``
- optionally ``<prefix>.run_manifest.csv``

By default these are written into a timestamped ``run_<timestamp>`` folder beneath the chosen output directory.

Step 8: Full paper artifact orchestration
-----------------------------------------

The top-level orchestrator is ``scripts/build-paper-artifacts.py``.

This script takes a master bundle and produces a reproducible paper-artifact run under:

- ``xai/logs/explainer_runs/bundles/paper_artifacts``

Each run creates:

- ``tables/``
- ``statistics/``
- ``paper/``
- ``provenance/``

including both telemetry-driven outputs and the legacy benchmark table package.