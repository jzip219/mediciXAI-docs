Benchmark Invariants
====================

Purpose
-------

This page freezes the benchmark invariants that guard the specification and the current release shape.

Invariant B-001
---------------

The benchmark release must contain the configured subject count, model count, and repetition count.

Parameter form:

.. math::

   N_{\mathrm{expected}} = N_{\mathrm{subjects}} \times N_{\mathrm{models}} \times N_{\mathrm{repeats}}

Observed responses must equal expected responses.

Invariant B-002
---------------

Each subject-model cell must contain exactly the configured number of repetitions.

If the cell is incomplete, the release is invalid for normative reporting.

Invariant B-003
---------------

Cosine similarity analysis requires exactly 5 repeated responses for the subject-model cell in the current release.

For five responses:

.. math::

   \binom{5}{2} = 10

That yields 10 pairwise comparisons.

Generalized form:

.. math::

   \binom{N_{\mathrm{repeats}}}{2} = \frac{N_{\mathrm{repeats}}(N_{\mathrm{repeats}} - 1)}{2}

Invariant B-004
---------------

Required-Risk Rate must be computed from required and non-present rows only.

That means the numerator is:

.. math::

   N_{\mathrm{severity=required\ and\ outcome\neq present}}

and not a broader missing-plus-contradicted surrogate.

Invariant B-005
---------------

All summary projections must be reconstructible from normalized rows.

No summary may introduce inferred weights or hidden state.

Invariant B-006
---------------

All published benchmark outputs must preserve provenance.

At minimum this includes:

- generation timestamp
- source bundle or source archive
- version identifiers
- checksum or hash information when available

Invariant B-007
---------------

The benchmark must keep terminology stable within one specification lineage.

Do not relabel a concept when the concept already has a frozen term.

Invariant B-008
---------------

Experimental metrics must not silently enter normative benchmark reporting.

They must be labeled experimental or excluded.

Invariant B-009
---------------

The specification is frozen for v1.0.

Meaning changes require a new specification version.

Release parameter note
----------------------

The current release parameters are descriptive, not normative:

- 4 subjects
- 3 models
- 5 repetitions
- 60 expected responses

These values may change in a future release without changing the meaning of the specification, as long as the benchmark parameters are updated and validated.