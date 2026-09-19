MediXAI Benchmark Specification v1.0
====================================

Documentation Mode: |documentation_mode|

Public Repository Links: |public_repo_status|

This documentation defines the normative specification for the MediXAI benchmark used to evaluate structured LLM-generated medical XAI reports.

The specification freezes the benchmark equations, data schema, aggregation rules, validation requirements, provenance model, and artifact generation process for Version 1.0.

Current benchmark release
-------------------------

- 4 benchmark subjects
- 3 evaluated models
- 5 repeated executions
- 60 benchmark responses

These values describe the current benchmark release and may evolve in future releases without changing the Benchmark Specification.

This specification corresponds to the benchmark described in the IACIS 2026 paper "Bridging the Human-Centered Gap in Agentic XAI: A Multi-Modal Explanation User Interface Framework."

Normative vs implementation
---------------------------

The Sphinx pages in this tree define the frozen specification and its supporting concepts.

The repository's Markdown docs capture historical implementation notes, release milestones, and governance context.

New to the benchmark?
---------------------

If you want to execute the benchmark rather than review the specification, begin with :doc:`benchmark_operator_quick_start`.

The Quick Start provides a practical execution workflow. It is non-normative and does not modify or replace requirements defined in :doc:`benchmark_specification_v1_0`.

For specification, validation, and release requirements, begin with:

- :doc:`benchmark_specification_status`
- :doc:`requirements_registry`
- :doc:`conformance`
- :doc:`release_process`

Documentation surfaces
----------------------

- Normative Specification (Frozen)
- Implementation Documentation (Internal)
- Public Repository (Optional)

Public release and reproducibility
----------------------------------

The verifiable release unit is the assembled package, not the workspace tree.

Release checksums are generated and validated against package-relative artifact paths after assembly. For the operational release workflow, see :doc:`release_process`.

For the public verification path, see :doc:`benchmark_testing_guide` and :doc:`validation_conformance_workflow`.

Recommended reading
-------------------

1. Benchmark Overview
2. Benchmark State Machine
3. Benchmark Specification
4. Mathematical Definitions
5. Benchmark Design Rationale
6. Provenance Model
7. Artifact Generation
8. Version History

Historical implementation notes are intentionally omitted from this documentation-only repository.

.. toctree::
   :maxdepth: 2
   :caption: Guide

   benchmark_specification_status
   benchmark_operator_quick_start
   benchmark_overview
   benchmark_state_machine
   benchmark_specification_v1_0
   score_key_taxonomy
   bundle_schema_reference
   inter_intra_model_statistics
   requirements_registry
   conformance
   validation_conformance_workflow
   benchmark_testing_guide
   benchmark_formulas
   benchmark_design_rationale
   data_provenance
   artifact_schema
   release_process
   benchmark_invariants
   terminology
   reporting_conventions
   benchmark_version_history
   documentation_standards
   benchmark_pipeline
   rebuild_process

.. toctree::
   :maxdepth: 1
   :caption: Appendices

   appendix_pytest_design_specification
   appendix_metric_traceability