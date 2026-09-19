Rebuild This Process
====================

Purpose
-------

This page documents exactly how this Sphinx documentation scaffold was created so the process can be repeated later without guesswork.

What was added
--------------

The initial Sphinx setup added these files:

- ``docs/sphinx/requirements.txt``
- ``docs/sphinx/Makefile``
- ``docs/sphinx/make.bat``
- ``docs/sphinx/source/conf.py``
- ``docs/sphinx/source/index.rst``
- ``docs/sphinx/source/benchmark_overview.rst``
- ``docs/sphinx/source/benchmark_pipeline.rst``
- ``docs/sphinx/source/benchmark_formulas.rst``
- ``docs/sphinx/source/rebuild_process.rst``

Why this structure was chosen
-----------------------------

The repository already had extensive benchmark documentation in Markdown, but it did not have:

- a Sphinx config
- a Sphinx index and table of contents
- a reproducible build command for user-facing docs

The goal of this initial structure is therefore modest:

1. Create a working Sphinx root.
2. Capture the benchmark pipeline in one navigable place.
3. Capture formulas and code-path ownership before equation work expands.
4. Keep the setup small enough that later contributors can maintain it.

How to recreate the setup manually
----------------------------------

From the repository root, create the folder structure:

.. code-block:: text

   docs/
     sphinx/
       requirements.txt
       Makefile
       make.bat
       source/
         conf.py
         index.rst
         benchmark_overview.rst
         benchmark_pipeline.rst
         benchmark_formulas.rst
         rebuild_process.rst

Then place the following minimal settings into ``conf.py``:

- set the project title
- enable ``sphinx.ext.mathjax`` for formulas
- enable ``sphinx.ext.autosectionlabel`` for stable references
- keep the theme simple to avoid extra dependencies

Install and build
-----------------

Install Sphinx:

.. code-block:: powershell

   python -m pip install -r docs/sphinx/requirements.txt

Build HTML from the repository root:

.. code-block:: powershell

   python -m sphinx -b html docs/sphinx/source docs/sphinx/build/html

Or on Windows from inside ``docs/sphinx``:

.. code-block:: powershell

   .\make.bat html

How to extend the docs later
----------------------------

When you add more benchmark documentation later, prefer this order:

1. Put governed benchmark definitions in the benchmark Markdown sources first.
2. Add a Sphinx page that explains the user-facing meaning of those definitions.
3. If a formula becomes normative, document its exact code path and then freeze the equation text.
4. If a script becomes part of the official benchmark path, document its inputs, discovery rules, and outputs.

Recommended next Sphinx pages
-----------------------------

Good next additions would be:

- a page for the full score-key taxonomy from ``lib/xaiScoring.ts``
- a page for normalized row schema and master bundle schema
- a page for inter-model and intra-model statistics
- a page for benchmark release validation and conformance workflow

Practical maintenance rule
--------------------------

Keep the Sphinx pages explanatory and user-oriented.

Keep the Markdown benchmark sources normative and change-controlled.

That split makes the site easier to maintain without turning the Sphinx tree into a second source of truth for benchmark governance.