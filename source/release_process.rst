Release Process
===============

Purpose
-------

This chapter defines the operational procedure for producing a complete benchmark release under Benchmark Specification v1.0.

It focuses on governance execution, not new benchmark semantics.

Release workflow
----------------

1. Implementation complete.
2. Run validation suite.
3. Verify benchmark invariants.
4. Produce benchmark artifacts.
5. Generate provenance manifest.
6. Complete conformance statement and machine-readable conformance evidence.
7. Freeze benchmark release.
8. Tag release.
9. Archive release package.

Workflow model
--------------

.. code-block:: text

   Implementation complete
           |
           v
   Validation suite
           |
           v
   Invariant verification
           |
           v
   Artifact production
           |
           v
   Provenance generation
           |
           v
   Conformance statement
           |
           v
   Release freeze
           |
           v
   Release tag
           |
           v
   Archived release package

Required release package
------------------------

A complete benchmark release package should include the following minimum artifact set:

.. code-block:: text

   Benchmark Release
   ├── manifest.json
   ├── provenance.json
   ├── benchmark_tables.csv
   ├── benchmark_tables.md
   ├── benchmark_metadata.json
        ├── conformance_statement.md
        ├── conformance_report.json
        ├── conformance_report.md
        ├── conformance_report.html
   ├── checksums.sha256
   └── release_notes.md

Each file should be generated or validated as part of the release workflow.

Release gates
-------------

At release time, teams should verify:

- validation suite status is passing
- benchmark invariants are satisfied
- conformance statement and report are complete
- checksums are present for release artifacts
- provenance references are complete and auditable

Checksum contract
-----------------

Release checksum manifests are generated and verified against the assembled package layout, using package-relative artifact paths inside the release verification directory.

Workspace-relative source paths are not considered release-verifiable because they do not represent the final archived package structure.

The developer pytest completion record is maintained in the implementation repository and is not part of this public documentation package.

Relationship to other chapters
------------------------------

- Normative semantics are governed by :doc:`benchmark_specification_v1_0`.
- Requirement interpretation and conformance language are governed by :doc:`conformance`.
- Provenance details are governed by :doc:`data_provenance`.
- Artifact structure and fields are governed by :doc:`artifact_schema`.

Governance posture
------------------

This release process defines how a release is finalized and archived.

It does not authorize changing the benchmark semantics. Semantic changes require a new specification version according to the versioning rules.
