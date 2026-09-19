Data Provenance
===============

Purpose
-------

This chapter records the provenance chain for benchmark data from source input to publication.

Provenance chain
----------------

.. code-block:: text

   Input
     ↓
   Archive
     ↓
   Bundle
     ↓
   Telemetry
     ↓
   Benchmark
     ↓
   Paper
     ↓
   Publication

Produced by / consumed by / immutable / checksum / version
-----------------------------------------------------------

Input
  Produced by: data collection or upstream generation.
  Consumed by: run archive creation.
  Immutable: no.
  Checksum: optional.
  Version: upstream source version when applicable.

Archive
  Produced by: explainer run execution.
  Consumed by: bundle generation and scoring scripts.
  Immutable: yes once stored.
  Checksum: yes when archived.
  Version: run metadata versioning and toolchain versioning.

Bundle
  Produced by: master-bundle export flow.
  Consumed by: telemetry, benchmark table generation, and paper artifact builders.
  Immutable: yes once stored.
  Checksum: yes.
  Version: artifact schema version plus benchmark identity metadata.

Telemetry
  Produced by: telemetry reconstruction scripts.
  Consumed by: paper tables and downstream analytics.
  Immutable: yes when exported as a recorded run artifact.
  Checksum: yes for stored outputs.
  Version: generator version and source bundle hash.

Benchmark
  Produced by: validated bundle plus release controls.
  Consumed by: paper and publication workflows.
  Immutable: yes for a frozen release.
  Checksum: yes on the stored evidence package.
  Version: specification version and release version.

  Current governed release chain:

  .. code-block:: text

     MEDIXAI-REL-1.0.1
     ├── BENCHMARK_MANIFEST_benchmark-v1.0.1.yaml
     └── verification/
         ├── req_outcomes.json
         ├── conformance_report.json
         ├── conformance_report.md
         └── checksums.sha256

Paper
  Produced by: paper-artifact builder.
  Consumed by: manuscript drafting and appendix generation.
  Immutable: yes once published or archived.
  Checksum: yes for archived outputs.
  Version: paper artifact build version.

Publication
  Produced by: final manuscript and associated evidence package.
  Consumed by: readers, reviewers, and future maintainers.
  Immutable: yes once published.
  Checksum: should be preserved in archival storage.
  Version: publication revision and benchmark release version.

Provenance fields to preserve
-----------------------------

Across the pipeline, preserve the following fields whenever available:

- source path or source bundle identifier
- generation time
- producing commit or tool version
- benchmark specification version
- score specification version
- prompt template version
- artifact schema version
- selected run identifiers
- checksum or hash

Why provenance matters
----------------------

Provenance allows a future reader to answer four questions:

1. What was produced?
2. What input produced it?
3. What version generated it?
4. Can it be checked again?

If one of those answers is missing, the artifact is less useful as a scientific record.