Documentation Standards
=======================

Purpose
-------

This page defines the documentation standard for benchmark pipeline scripts that feed the user-facing Sphinx documentation.

Scope
-----

Apply this standard to scripts that directly participate in:

- benchmark scoring
- master-bundle generation or recomputation
- telemetry or benchmark table exports
- paper-artifact generation

Language-specific rule
----------------------

Use Python docstrings for Python scripts and JSDoc for JavaScript scripts.

The goal is not stylistic symmetry. The goal is that each language uses its native documentation convention while exposing the same information.

Required function documentation fields
--------------------------------------

Every non-trivial function in these scripts should document:

- what the function does
- every parameter or argument
- the type of every parameter or argument
- what the function returns
- the return type
- raised exceptions when that behavior is important to callers

Python format
-------------

For Python helpers, use docstrings with explicit ``Args`` and ``Returns`` sections.

Preferred shape:

.. code-block:: python

   def example(path: Path, strict: bool = False) -> dict[str, Any]:
       """Summarize one artifact file.

       Args:
           path (Path): Input artifact path.
           strict (bool): Whether to fail on soft validation issues.

       Returns:
           dict[str, Any]: Parsed artifact summary.

       Raises:
           ValueError: Raised when strict validation fails.
       """

JavaScript format
-----------------

For JavaScript helpers, use JSDoc with ``@param`` and ``@returns``.

Preferred shape:

.. code-block:: javascript

   /**
    * Summarize one artifact file.
    *
    * @param {string} filePath Input artifact path.
    * @param {boolean} strict Whether to fail on soft validation issues.
    * @returns {Object} Parsed artifact summary.
    */
   function example(filePath, strict = false) {
     // ...
   }

Module-level requirement
------------------------

Each benchmark pipeline script should also have a module-level docstring or top-of-file JSDoc block that states:

- the script's role in the pipeline
- its primary inputs
- its primary outputs

Why this matters
----------------

This documentation standard serves three purposes:

1. It makes the scripts understandable without reverse-engineering every helper.
2. It gives the Sphinx documentation a traceable code-level source.
3. It reduces ambiguity when formulas or artifact contracts change.

Practical rule
--------------

When a benchmark-affecting script changes behavior, update both:

- the relevant function docstrings or JSDoc
- the corresponding Sphinx page that describes the pipeline or formulas