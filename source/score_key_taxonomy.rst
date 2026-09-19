Score-Key Taxonomy
==================

Purpose
-------

This page documents the full SHAP score-key taxonomy defined in the scoring contract.

See Also
--------

- :doc:`bundle_schema_reference`
- :doc:`inter_intra_model_statistics`
- :doc:`validation_conformance_workflow`

Authoritative source
--------------------

The canonical source of this taxonomy is the released score specification in ``lib/xaiScoring.ts``:

- ``shapPromptScoreSpec``
- ``SHAP_SCORE_KEY_IDS``
- ``SHAP_SCORE_GROUP_IDS``
- ``SHAP_PROMPT_SECTION_IDS``

Any semantic change to this taxonomy requires score-spec/version governance.

Prompt section taxonomy
-----------------------

Released prompt sections:

- ``image_grounded_visual_summary``
- ``model_behavior_summary``
- ``observed_evidence``
- ``attribution_highlights``
- ``overlay_agreement``
- ``interpretability_assessment``
- ``potential_confounding_factors``
- ``cohort_alignment``
- ``failure_mode_analysis``
- ``model_vs_biology``
- ``safety_caveats``
- ``overall_interpretability_confidence``

Score-group taxonomy
--------------------

.. list-table::
   :header-rows: 1

   * - Group
     - Tier
     - Role
   * - ``integrity``
     - 0
     - Transport/input gating checks.
   * - ``image_grounding``
     - 1
     - Required image-first interpretation behavior.
   * - ``required_metadata``
     - 1
     - Required case metadata carry-through.
   * - ``shap_quantitative_facts``
     - 2
     - Supporting quantitative attribution details.
   * - ``model_behavior``
     - 2
     - Localization and model-attention interpretation.
   * - ``epistemic_safety``
     - 2
     - Safety/restraint and evidence-separation rules.
   * - ``failure_modes``
     - 3
     - Conditional failure-mode taxonomy.
   * - ``cohort_context``
     - 3
     - Cohort context as supporting evidence.
   * - ``overall_confidence``
     - 3
     - Final interpretability confidence statement.

Key inventory summary
---------------------

Current released key inventory (57 total keys):

.. list-table::
   :header-rows: 1

   * - Group
     - Key count
   * - ``integrity``
     - 7
   * - ``image_grounding``
     - 7
   * - ``required_metadata``
     - 8
   * - ``shap_quantitative_facts``
     - 9
   * - ``model_behavior``
     - 5
   * - ``epistemic_safety``
     - 7
   * - ``failure_modes``
     - 9
   * - ``cohort_context``
     - 3
   * - ``overall_confidence``
     - 2

Key-level attributes
--------------------

Each key is declared with a typed contract that includes:

- key identifier
- group identifier
- tier
- applicability (``required``, ``conditional``, ``optional``)
- section mapping
- extraction method
- expected extraction states
- provenance metadata

Integrity gating
----------------

Some integrity keys are marked ``gating: true`` and are used as release-readiness gate conditions in scoring flows.

Contract health and invariants
------------------------------

Contract health helpers in ``lib/xaiScoring.ts`` enforce taxonomy consistency:

- ``validateShapPromptContractInvariants``
- ``summarizeShapPromptContractHealth``

These checks cover section-key mapping, provenance completeness, expected states, and extraction metadata completeness.

Versioning rule
---------------

The taxonomy is part of benchmark semantics for this lineage. Adding/removing/redefining keys, groups, or state meaning requires a specification/versioned contract update.
