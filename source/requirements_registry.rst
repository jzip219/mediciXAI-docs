Requirement Identifier Registry
===============================

Purpose
-------

This page defines stable requirement identifiers that can be cited by conformance statements and release evidence.

Identifier format
-----------------

Identifiers follow this pattern:

``REQ-<DOMAIN>-<NNN>``

Domains used in this registry:

- ``VAL``: validation and execution structure
- ``SCORE``: scoring equations and aggregate metrics
- ``SEM``: semantic stability and dispersion metrics
- ``PROV``: provenance and integrity evidence
- ``ART``: artifact package and schema expectations

Core requirement set
--------------------

================ ============================================= ==============================================
Requirement ID   Statement                                     Reference
================ ============================================= ==============================================
REQ-VAL-001      Each subject-model cell shall contain         :doc:`benchmark_invariants`
                 exactly N repeated executions for the
                 declared release parameters.
REQ-VAL-002      Validation gates shall pass before a          :doc:`release_process`
                 benchmark release is frozen.
REQ-SCORE-001    Present Rate shall be computed according      :doc:`benchmark_formulas`
                 to the frozen v1.0 formula.
REQ-SCORE-002    Required-Risk Rate shall be computed          :doc:`benchmark_formulas`
                 using required and non-present outcomes
                 according to the frozen v1.0 formula.
REQ-SEM-001      Semantic stability shall be calculated        :doc:`benchmark_formulas`
                 using the declared embedding and
                 pairwise similarity procedure for the
                 release.
REQ-SEM-002      Semantic dispersion shall be reported         :doc:`benchmark_formulas`
                 according to the frozen v1.0 definition.
REQ-PROV-001     Provenance records shall be present and       :doc:`data_provenance`
                 auditable for release artifacts.
REQ-PROV-002     Integrity checksums shall be generated        :doc:`data_provenance`
                 for release artifacts.
REQ-ART-001      Release artifacts shall conform to the        :doc:`artifact_schema`
                 declared artifact schema and package rules.
REQ-ART-002      A benchmark release package shall include     :doc:`release_process`
                 the minimum required files for archival
                 and reproducibility.
================ ============================================= ==============================================

Conformance usage
-----------------

Conformance statements should cite requirement IDs directly, for example:

.. code-block:: text

   Conforms to:
   - REQ-SCORE-001
   - REQ-SCORE-002
   - REQ-SEM-001
   - REQ-PROV-001
   - REQ-ART-001

Governance note
---------------

Requirement IDs are stable identifiers within a specification version. If semantics change, a new specification version should define the revised requirement set and mappings.
