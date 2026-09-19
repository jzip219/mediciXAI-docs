Validation and Conformance Workflow
===================================

Purpose
-------

This page gives an operational validation and conformance workflow for benchmark releases.

It complements, but does not replace, :doc:`release_process` and :doc:`conformance`.

See Also
--------

- :doc:`score_key_taxonomy`
- :doc:`bundle_schema_reference`
- :doc:`inter_intra_model_statistics`
- :doc:`release_process`
- :doc:`conformance`

Workflow
--------

1. Complete implementation updates for the release candidate.
2. Run benchmark release validation tests.
3. Build Sphinx HTML documentation.
4. Build Sphinx linkcheck report.
5. Verify invariants and required artifact set.
6. Complete conformance statement.
7. Freeze and tag the release.
8. Archive package plus checksums and provenance evidence.

Command reference
-----------------

Benchmark release test gate:

.. code-block:: powershell

   npm run test:benchmark-release

For focused Python iteration, see :doc:`benchmark_testing_guide` or run:

.. code-block:: powershell

   python -m pytest tests/unit tests/integration -q
   python -m pytest tests/release -q

Sphinx HTML gate:

.. code-block:: powershell

   $env:MEDIXAI_DOC_MODE='internal'
   Remove-Item Env:MEDIXAI_REPO_BLOB_BASE_URL -ErrorAction SilentlyContinue
   python -m sphinx -b html docs/sphinx/source docs/sphinx/build/html

Sphinx linkcheck gate:

.. code-block:: powershell

   $env:MEDIXAI_DOC_MODE='internal'
   Remove-Item Env:MEDIXAI_REPO_BLOB_BASE_URL -ErrorAction SilentlyContinue
   python -m sphinx -b linkcheck docs/sphinx/source docs/sphinx/build/linkcheck

Required evidence package
-------------------------

A conformant release package should include at minimum:

- release manifest
- conformance statement
- benchmark tables and metadata
- provenance manifest
- checksums
- release notes

Conformance linkage
-------------------

Conformance reporting should cite requirement IDs from :doc:`requirements_registry` where applicable.

Suggested pattern:

.. code-block:: text

   Conforms to:
   - REQ-SCORE-001
   - REQ-SCORE-002
   - REQ-SEM-001
   - REQ-PROV-001
   - REQ-ART-001

Non-semantic errata handling
----------------------------

If a release needs integrity-only correction (for example, checksum reproducibility), use a non-semantic erratum release ID and new corrective tags while preserving original freeze tags.

Relationship to governance chapters
-----------------------------------

- Process and artifact freeze posture: :doc:`release_process`
- Conformance language and evidence model: :doc:`conformance`
- Provenance/audit chain: :doc:`data_provenance`
- Requirement identifiers: :doc:`requirements_registry`
