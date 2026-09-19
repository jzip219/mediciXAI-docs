Benchmark Specification v1.0
=============================

Status
------

Frozen normative specification for the benchmark.

This page is the reference point for benchmark meaning, not an implementation note.

Design rule
-----------

Everything in the implementation, documentation, paper pipeline, and future releases should conform to this specification.

The specification does not conform to the implementation.

Benchmark layers
----------------

The benchmark is structured as:

.. code-block:: text

   Benchmark Specification v1.0
           │
           ├── Sphinx Documentation
           ├── JavaScript
           ├── Python
           ├── Paper
           └── Future releases

Normative boundary
------------------

The specification defines:

- benchmark meaning
- benchmark unit
- required formulas
- required schema
- aggregation rules
- validation requirements
- provenance requirements

The specification does not define:

- a particular UI
- a particular storage implementation
- a particular scripting language
- a particular paper layout

Benchmark unit
--------------

One benchmark unit is one model, one subject, and one execution.

That unit is the basis for all downstream classification and aggregation.

Frozen formulas
---------------

The formulas in this benchmark lineage are frozen within v1.0:

- Present Rate
- Required-Risk Rate
- Within-subject SD
- Pooled SD
- Semantic similarity
- Semantic dispersion

Current benchmark parameters
----------------------------

The current release uses these parameter values:

- subjects = 4
- models = 3
- repetitions per subject-model cell = 5
- expected responses = 60

These are benchmark release parameters, not the specification itself.

Release versus specification
----------------------------

The specification freezes design.

The release declares the values used for one benchmark run.

The execution records one actual run of the benchmark release.

Normative artifact boundary
---------------------------

The following are normative benchmark artifacts under this v1.0 lineage:

- normalized rows
- run summary rows
- subject summary rows
- model summary rows
- bundle metadata
- validation outputs
- provenance manifest

Non-retroactive rule
--------------------

Published benchmark releases MUST be interpreted using the specification and governance versions declared at release time.

Historical releases MUST NOT be silently reinterpreted under later methodology.

Version label
-------------

This page freezes the benchmark as:

- Benchmark Specification v1.0

Any substantive change to meaning, equations, terminology, or validation gates requires a new specification version.