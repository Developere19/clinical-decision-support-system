# Clinical Decision Support System (CDSS)

## AINL3001 - Knowledge-Driven Artificial Intelligence

**TU Dublin | BSc Data Science and Artificial Intelligence**

Revised following proposal feedback to clarify project scope, reasoning complexity, Bayesian integration and evaluation.

## 1. Team Information

**Group Name:** Group A

| **Name** | **Student Number** | **GitHub Username** |
| --- | --- | --- |
| Hamza Zeeshan | C24333116 | Developere19 |
| Mohammed Younis | C24372973 | Mohammedyounis18 |

## 2. Problem Description

Many illnesses share similar symptoms, making it difficult to distinguish possible illness patterns from symptoms alone. Users may also provide incomplete information, while some symptom combinations may match multiple categories.

Our project will develop an educational Clinical Decision Support System in Python. Users will enter symptoms through a command-line interface. The system will use rule-based reasoning to identify possible illness categories and Bayesian reasoning to rank overlapping respiratory candidates while explaining how conclusions are reached.

The knowledge base will contain six illness categories, 18-20 symptoms, 10-15 intermediate concepts and 35-45 IF-THEN rules. The categories will include influenza-like, COVID-like, common-cold-like, allergy-like, strep-throat-like and gastroenteritis-like illness.

The system will be for educational demonstration only. It will not diagnose conditions, prescribe medication or replace professional medical advice.

## 3. Proposed AI Approach

The project will combine knowledge representation, forward-chaining inference and Bayesian reasoning under uncertainty.

### Knowledge Representation

Symptoms and intermediate concepts will be represented as facts. Structured IF-THEN rules will be stored in JSON, separately from the main Python logic.

The knowledge base will support multi-stage reasoning through rules such as:

- IF fever AND body aches THEN systemic symptoms.
- IF cough AND sore throat THEN respiratory symptoms.
- IF systemic symptoms AND respiratory symptoms THEN influenza-like illness.

The system will distinguish between present, explicitly absent and unknown symptoms. Negative conditions will only be satisfied when symptoms are explicitly reported as absent. Unreported symptoms will remain unknown.

### Forward-Chaining Inference

The inference engine will start with reported present symptoms and repeatedly apply rules whose conditions are satisfied. Derived facts will be added to the knowledge state and may activate additional rules. Reasoning will continue until no further facts can be derived.

The engine will record fired rule identifiers and derived facts for explainability.

### Bayesian Reasoning

Bayesian reasoning will rank overlapping influenza-like, COVID-like and common-cold-like candidates.

**User symptoms → Forward chaining → Candidate categories → Bayesian ranking → Explanation**

Forward chaining will identify possible illness categories. When at least two respiratory candidates are inferred, the Bayesian module will rank those candidates rather than independently generate new conclusions.

Equal priors will be used to avoid assumptions about real-world disease prevalence. Symptom likelihoods will follow an illustrative scale of 0.8 for strong, 0.5 for moderate and 0.2 for weak associations. These values will represent educational modelling assumptions rather than clinically validated probabilities.

The module will multiply the prior by likelihoods for reported present symptoms and complementary likelihoods for explicitly absent symptoms where parameters are available. Unknown symptoms will not contribute. Scores will be normalised across eligible candidates and presented as relative ranking scores, not diagnostic probabilities.

## 4. System Design

Five main components will be used:

1. **User Interface:** collects, normalises and validates symptoms.
2. **Knowledge Base:** stores symptoms, concepts and IF-THEN rules and validates rule references.
3. **Forward-Chaining Engine:** derives facts and illness candidates.
4. **Bayesian Module:** ranks overlapping respiratory candidates.
5. **Integration and Explanation:** connects components and explains conclusions using fired rules.

The system will follow an AIMA-inspired structure. The state will consist of known and derived facts, with explicitly absent symptoms retained separately. An action will involve applying an applicable rule. A transition will occur when a new conclusion is added. Reasoning will terminate at a fixed point when no additional facts can be derived.

## 5. Evaluation Plan

Approximately eight fictional evaluation cases will cover all six illness categories, overlapping respiratory symptoms, incomplete information, explicitly absent symptoms, no-match cases and multi-stage forward chaining.

Expected and actual illness categories will be compared. A respiratory overlap case will demonstrate the difference between unranked rule-based candidates and the combined system's ranked output.

Automated `pytest` tests will verify knowledge-base validation, inference, symptom states, expected conclusions, explanation output, Bayesian ranking and system integration.

Evaluation will discuss limitations, including simplified rules, illustrative likelihoods and the conditional independence assumption. Results will assess prototype behaviour rather than clinical accuracy.

## 6. Planned Contributions

| **Team Member** | **Planned Responsibilities** |
| --- | --- |
| Hamza Zeeshan | GitHub management, knowledge-base development, IF-THEN rules, forward chaining, knowledge-base validation, system integration, Bayesian configuration and integration, CLI integration and end-to-end testing. |
| Mohammed Younis | Bayesian ranking module, command-line interface, explanation mechanism, evaluation framework and automated testing. |

Both team members will contribute to system design, debugging, documentation, evaluation and the final presentation.
