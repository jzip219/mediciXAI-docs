Benchmark State Machine
=======================

Purpose
-------

This page describes the canonical benchmark state machine from raw response to paper tables.

The state machine defines the transitions, the fields produced at each step, and the invariants that must hold.

State flow
----------

.. code-block:: text

   Raw Response
        │
        ▼
   Extraction
        │
        ▼
   Normalized Key
        │
        ▼
   Outcome Classification
        │
        ▼
   Run Summary
        │
        ▼
   Subject Summary
        │
        ▼
   Model Summary
        │
        ▼
   Paper Tables

Transition 1: Raw Response -> Extraction
----------------------------------------

Input:

- archived response text
- archived envelope metadata
- prompt and score contract context

Output:

- section states
- key states
- normalized response text
- parser metadata

Invariant:

- extraction must preserve traceability back to the archived run

Transition 2: Extraction -> Normalized Key
------------------------------------------

Input:

- extracted key states
- extracted section states

Output:

- one canonical state per released key

Invariant:

- every released key must be accounted for exactly once in the scoring pass

Transition 3: Normalized Key -> Outcome Classification
------------------------------------------------------

Input:

- key state
- key applicability
- key required flag
- section context

Output:

- ``present``
- ``missing`` or ``missing_required`` depending on the reporting layer
- ``contradicted``
- ``not_applicable``
- ``unresolved_non_required``

Invariant:

- one key maps to one primary outcome

Transition 4: Outcome Classification -> Run Summary
---------------------------------------------------

Input:

- all normalized key outcomes for one run

Output:

- run-level present rate
- run-level required-risk rate
- run-level traceability metadata

Invariant:

- the run summary is reconstructible from normalized rows alone

Transition 5: Run Summary -> Subject Summary
--------------------------------------------

Input:

- all runs for one subject

Output:

- mean present rate
- mean required-risk rate
- run dispersion
- within-subject dispersion metrics when applicable

Invariant:

- all subject summaries must preserve the original run identifiers in the underlying bundle or telemetry source

Transition 6: Subject Summary -> Model Summary
----------------------------------------------

Input:

- all subject summaries for one model

Output:

- model means
- model dispersion
- pooled within-subject dispersion when applicable

Invariant:

- model summaries must be derived from subject and run summaries, not from ad hoc side calculations

Transition 7: Model Summary -> Paper Tables
-------------------------------------------

Input:

- model summaries
- subject summaries
- bundle metadata

Output:

- table 1
- table 2
- subject breakdown
- markdown exports
- csv exports

Invariant:

- paper tables must be reproducible from the bundle or telemetry source used to generate them

Additional gates
----------------

Some transitions have extra validation gates:

- cosine similarity requires exactly 5 repeated outputs per subject-model cell
- pooled SD requires at least two observations per subject cell
- release conformance requires provenance and checksum coverage

Why this matters
----------------

This state machine is the bridge between the abstract specification and the implemented scripts.

It keeps the benchmark readable as a process, not just as a collection of output files.