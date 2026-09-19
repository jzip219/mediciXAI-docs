Conformance
===========

Purpose
-------

This chapter defines how implementation conformance is evaluated against Benchmark Specification v1.0.

It separates:

- normative specification requirements
- implementation-defined behavior
- measured conformance status

Conformance scope
-----------------

Conformance applies to benchmark releases and reference implementation behavior used to generate those releases.

This chapter does not redefine the benchmark semantics. Semantics remain governed by :doc:`benchmark_specification_v1_0`.

Conformance statement model
---------------------------

Each benchmark release should include a conformance statement with:

- specification version
- implementation identifier (commit, tag, or release)
- conformance status
- implementation-defined behaviors
- declared exceptions and rationale

Recommended conformance status values:

- ``conformant``
- ``conformant_with_exceptions``
- ``non_conformant``

Minimum conformance evidence
----------------------------

A conformance claim should be supported by evidence that includes:

- declared governing versions
- deterministic scoring outputs for the release artifact set
- validation gate outputs
- provenance and checksum coverage
- reproducible benchmark tables and statistics artifacts

Implementation evidence note
----------------------------

The reference implementation generates machine-readable and human-readable conformance reports from REQ-indexed pytest evidence.

A release is classified as conformant only when all in-scope requirements pass, no requirements remain unevaluated, and pytest exits successfully.

These report artifacts are informative implementation evidence. Unless explicitly frozen in a normative artifact contract, report filenames and package layout remain implementation-defined.

For the governed release ``MEDIXAI-REL-1.0.1``, the concrete implementation-conformance statement is anchored by ``docs/research/BENCHMARK_MANIFEST_benchmark-v1.0.1.yaml`` and the linked verification evidence set:

- ``tests/results/verification/req_outcomes.json``
- ``tests/results/verification/conformance_report.json``
- ``tests/results/verification/conformance_report.md``
- ``tests/results/verification/checksums.sha256``

Implementation-defined behavior
-------------------------------

Implementation-defined behavior is allowed when it does not alter normative semantics.

Examples include:

- storage layout and folder structure
- UI and workflow orchestration
- log formatting and non-normative metadata fields

All implementation-defined behaviors should be explicitly documented.

Exceptions and deviations
-------------------------

If implementation behavior diverges from a normative requirement, the release should declare:

- requirement identifier
- deviation description
- impact on comparability
- mitigation or remediation plan

Normative semantics must not be changed silently through implementation updates.

Conformance template
--------------------

Use this template for release notes or benchmark release records:

.. code-block:: text

   Conformance Statement
   - Benchmark Specification: v1.0
   - Implementation: <tag-or-commit>
   - Status: conformant | conformant_with_exceptions | non_conformant
   - Implementation-defined behaviors:
     - <item>
     - <item>
   - Exceptions:
     - Requirement: <id>
       Description: <summary>
       Impact: <comparability effect>
       Mitigation: <plan>

    Informative example
    -------------------

    This example is informative and may be adapted for individual releases; conformance remains determined by the normative requirements and release evidence.

    Example: Benchmark v1.0 Reference Implementation Conformance Statement
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block:: text

       Implementation: MedixAI benchmark reference implementation
       Specification: Benchmark Specification v1.0
       Implementation version: <git tag or commit>
       Release identifier: <benchmark release ID>
       Conformance date: <ISO 8601 timestamp>

       Declaration
       The MedixAI benchmark reference implementation conforms to Benchmark Specification v1.0
       for scoring semantics, required-risk computation, aggregation rules,
       semantic-stability calculation, artifact generation, provenance requirements,
       and release validation.

       Evidence
       - release gate passed
       - manifest conformance validation passed
       - fixture and snapshot tests passed
       - checksums and provenance manifest generated
       - no unresolved normative deviations

       Implementation-defined behaviors
       - filesystem layout
       - CLI argument names
       - timestamped output-directory naming
       - internal logging format
       - user-interface presentation

       Exceptions or deviations
       None.

       When applicable:
       <requirement ID> - <deviation description, rationale, impact, and remediation plan>

       Approval
       - Prepared by:
       - Reviewed by:
       - Approval date:
       - Archived evidence location:

Versioning rule
---------------

If a proposed change alters benchmark semantics, equations, normative vocabulary, aggregation meaning, or validation meaning, a new specification version is required.

If a proposed change is implementation-only and preserves normative semantics, a specification version bump is not required.

Current draft posture
---------------------

This chapter is a governance scaffold for v1.x lineage.

As future releases are produced, this chapter can be extended with concrete conformance records and requirement-level traceability tables.
