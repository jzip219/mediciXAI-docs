Benchmark Testing Guide
=======================

Purpose
-------

This guide describes the reproducible test layers used to validate the benchmark implementation. It is intended for contributors and release reviewers working from a clean checkout.

Test layers
-----------

Python pytest tests validate benchmark formulas, input validation, provenance, pipeline behavior, and frozen release guardrails:

.. code-block:: powershell

   python -m pytest tests/unit tests/integration -q
   python -m pytest tests/release -q

The JavaScript and TypeScript tests validate analytics and manifest conformance. They remain part of benchmark validation and are not replaced by pytest:

.. code-block:: powershell

   npm run test:bench
   npm run test:manifest

The release wrapper runs the benchmark test layers together:

.. code-block:: powershell

   npm run test:benchmark-release

The Python stage is invoked by ``test:benchmark-python``. Running pytest directly is useful when iterating on a Python test failure; running the release wrapper is the authoritative cross-ecosystem gate.

Coverage
--------

Coverage can be collected for the Python implementation with:

.. code-block:: powershell

   python -m pytest --cov=xai --cov=scripts --cov-report=term-missing tests/unit tests/integration tests/release

Coverage is diagnostic evidence. A passing release gate, deterministic outputs, and requirement traceability remain the conformance criteria.

Requirements and evidence
--------------------------

Tests should map to the requirement identifiers in :doc:`requirements_registry`, including scoring, semantic stability, validation, provenance, and artifact requirements.

The conformance workflow produces machine-readable and human-readable evidence, including:

* ``tests/results/verification/req_outcomes.json``
* ``tests/results/verification/conformance_report.json``
* ``tests/results/verification/conformance_report.md``
* ``tests/results/verification/checksums.sha256``

Release expectations
--------------------

The benchmark test suite should run from a clean checkout, use deterministic fixtures, and avoid live API requests. Frozen-profile tests enforce the governed release shape; future parameterized profiles should be treated as separate extension work.

For the detailed, developer-facing pytest design and traceability plan, see :doc:`appendix_pytest_design_specification` and the companion ``docs/benchmark/PYTEST_DESIGN_SPECIFICATION_v1_0_1.md`` document in the repository.