Non-Normative Developer Appendix: Pytest Design Specification
==============================================================

Boundary statement
------------------

This appendix provides implementation guidance for validating conformance to Benchmark Specification v1.0. It does not introduce or modify normative benchmark requirements.

In the event of a conflict, the normative specification and requirements registry take precedence.

Primary normative anchors
-------------------------

- :doc:`benchmark_specification_v1_0`
- :doc:`requirements_registry`
- :doc:`conformance`
- :doc:`benchmark_formulas`
- :doc:`benchmark_invariants`

Implementation target scope
---------------------------

The pytest design is intended for the Python benchmark implementation path that reconstructs run-level records, computes benchmark statistics, emits provenance metadata, and generates release-facing artifacts.

Implementation anchor:

- ``xai/logs/explainer_runs/bundles/generate_benchmark_tables.py`` in the implementation repository.

Design intent
-------------

The suite should be organized around normative claims, equations, invariants, evidence levels, and release artifact contracts rather than around function coverage alone.

Recommended test layers:

- unit tests for formulas, canonicalization, semantic logic, ranking, and provenance primitives
- integration tests for end-to-end input-to-artifact generation paths
- release tests for frozen-profile guardrails, schema constraints, deterministic regeneration, and golden outputs

Traceability expectation
------------------------

Each implemented pytest module should trace to requirement identifiers in :doc:`requirements_registry`.

At minimum, tests should cover:

- REQ-SCORE-001 and REQ-SCORE-002 (scoring equations)
- REQ-SEM-001 and REQ-SEM-002 (semantic stability and dispersion)
- REQ-VAL-001 and REQ-VAL-002 (validation and release guardrails)
- REQ-PROV-001 and REQ-PROV-002 (provenance and integrity)
- REQ-ART-001 and REQ-ART-002 (artifact schema and release package expectations)

Verification carry-forward notes
--------------------------------

The equation-to-implementation verification pass identified two planning notes that should be explicit in pytest design.

Checksum contract note
^^^^^^^^^^^^^^^^^^^^^^

Checksum format handling is currently a documentation ambiguity, not a benchmark-semantic conflict.

Test guidance:

- validate the currently governed release checksum contract
- do not assume equivalence across every hash-manifest representation unless explicitly governed by release documentation

Frozen profile note
^^^^^^^^^^^^^^^^^^^

The hard-coded 4 x 3 x 5 design guardrail is currently implementation-defined for the frozen paper-release profile.

Test guidance:

- keep conformance tests that enforce the frozen paper-release profile
- keep separate future-facing parameterized-profile tests as deferred extension work for a later specification or implementation update

Companion implementation document
---------------------------------

The detailed implementation-facing design document is maintained separately from this public documentation repository.

This appendix is a navigational and governance bridge. It preserves normative/non-normative boundaries while directing developers to the concrete pytest implementation plan.
