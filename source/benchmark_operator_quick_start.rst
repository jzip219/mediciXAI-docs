Benchmark Operator Quick Start (Non-Normative)
==============================================

Purpose
-------

This onboarding guide is for first-time benchmark operators who need a practical, one-afternoon path to run the benchmark workflow.

This page is intentionally non-normative. It does not modify the frozen Benchmark Specification v1.0 semantics, equations, invariants, or conformance requirements.

Use this guide with the normative pages:

- :doc:`benchmark_specification_v1_0`
- :doc:`conformance`
- :doc:`release_process`

When to use this page
---------------------

- You are new to the benchmark and need an execution checklist.
- You want to produce a valid release candidate quickly.
- You want links to the canonical normative requirements while you work.

If implementation behavior differs from this guide, the normative specification and conformance requirements take precedence.

This guide describes one reference workflow for executing the benchmark. Alternative implementations may conform to Benchmark Specification v1.0 if they satisfy all normative requirements.

Operator workflow
-----------------

1. Install dependencies

   - Install repository dependencies and verify the toolchain required by this workspace.
   - Confirm that benchmark scripts and documentation tooling run successfully.

   See also:

   - :doc:`rebuild_process`
   - :doc:`documentation_standards`

2. Obtain benchmark inputs

   - Prepare or retrieve the benchmark case set and required metadata.
   - Confirm that identifiers, score keys, and expected response structures align with the frozen contract.

   See also:

   - :doc:`requirements_registry`
   - :doc:`score_key_taxonomy`
   - :doc:`bundle_schema_reference`

3. Run API prompt benchmark

   - Execute benchmark prompts against the configured model endpoints.
   - Store raw responses and execution metadata for repeatability and auditability.

   See also:

   - :doc:`benchmark_pipeline`
   - :doc:`data_provenance`

4. Validate artifact structure

   - Validate output artifacts against the schema and required fields.
   - Verify extraction and scoring preconditions before analytics generation.

   See also:

   - :doc:`artifact_schema`
   - :doc:`validation_conformance_workflow`

5. Generate benchmark tables

   - Run benchmark table generation for the current release candidate.
   - Confirm generated tables align with reporting conventions.

   See also:

   - :doc:`reporting_conventions`
   - :doc:`inter_intra_model_statistics`

6. Interpret outputs

   - Interpret benchmark score outputs using specification-defined terminology.
   - Distinguish criterion satisfaction metrics from broader clinical or deployment claims.

   See also:

   - :doc:`benchmark_formulas`
   - :doc:`terminology`
   - :doc:`benchmark_design_rationale`

7. Package release artifacts

   - Assemble release artifacts, provenance, checksums, and required manifests.
   - Run conformance checks and release gating before publication.
   - Run ``npm run test:benchmark-release`` as the final validation command.
   - Successful completion produces verification artifacts for the release package:

     - ``verification/req_outcomes.json``
     - ``verification/conformance_report.json``
     - ``verification/conformance_report.md``

   See also:

   - :doc:`conformance`
   - :doc:`release_process`
   - :doc:`benchmark_version_history`

One-afternoon checklist
-----------------------

- Environment validated
- Benchmark inputs prepared
- API benchmark run completed
- Artifact validation passed
- Benchmark tables generated
- Output interpretation completed
- Release package generated with checksums
- Conformance evidence captured

Boundary statement
------------------

This quick start is an onboarding and operational aid. It is not part of the frozen normative specification.
