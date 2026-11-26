# Clinical Decision Support System (CDSS)

## AINL3001 - Knowledge-Driven Artificial Intelligence

**TU Dublin | BSc Data Science and Artificial Intelligence**

Revised following proposal feedback and implementation progress to clarify scope, reasoning complexity, Bayesian integration, evaluation and team contributions.

## 1. Team Information

**Group Name:** Group A

| Name | Student Number | GitHub Username |
| --- | --- | --- |
| Hamza Zeeshan | C24333116 | Developere19 |
| Mohammed Younis | C24372973 | Mohammedyounis18 |

## 2. Problem Description

Many illnesses share similar symptoms, making possible illness patterns difficult to distinguish from symptoms alone. Fever, cough and fatigue, for example, can occur across several respiratory illnesses. Users may also provide incomplete information, and some symptom combinations may match more than one category.

Our project develops an educational Clinical Decision Support System in Python. Users enter symptoms through a command-line interface. The system uses rule-based reasoning to identify possible illness categories and Bayesian reasoning to rank overlapping respiratory candidates while explaining how conclusions were reached.

The knowledge base contains six illness categories, 20 symptoms, 13 intermediate concepts and 35 IF-THEN rules. The categories are influenza-like, COVID-like, common-cold-like, allergy-like, strep-throat-like and gastroenteritis-like illness.

The system is for educational demonstration only. It does not diagnose conditions, prescribe medication or replace professional medical advice. All evaluation cases are fictional.

## 3. Proposed AI Approach

The project combines knowledge representation, forward chaining and Bayesian reasoning.

### Knowledge Representation

Symptoms and derived concepts are represented as facts. Medical relationships are stored as structured IF-THEN rules in JSON, separate from the main Python logic.

The knowledge base supports multi-stage reasoning. For example:

- IF fever AND body aches THEN systemic symptoms.
- IF cough AND sore throat THEN respiratory symptoms.
- IF systemic symptoms AND respiratory symptoms THEN influenza-like illness.

The system distinguishes between symptoms that are present, explicitly absent or unknown. Negative information is only used when the user explicitly reports that a symptom is absent.

### Forward-Chaining Inference

The inference engine starts with reported symptoms as known facts and repeatedly applies rules whose conditions are satisfied. New conclusions are added to the knowledge state and may activate later rules. Reasoning stops when no further facts can be derived.

The engine records fired rules and derived facts so the reasoning process can be explained.

### Bayesian Reasoning

Bayesian reasoning is applied to influenza-like, COVID-like and common-cold-like categories.

The Bayesian component is integrated with the rule-based system:

**User symptoms → Forward chaining → Candidate categories → Bayesian ranking → Explanation**

Forward chaining first identifies possible categories. If two or more respiratory categories are inferred, the Bayesian module ranks those candidates using the available evidence.

Equal priors are used so the prototype does not assume real-world disease prevalence. Symptom likelihoods use an illustrative scale of 0.8 for strong, 0.5 for moderate and 0.2 for weak associations. These are educational modelling assumptions rather than clinically validated probabilities. Bayesian outputs are presented as relative ranking scores, not diagnostic probabilities.

## 4. System Design

The system uses a modular Python architecture with five main components:

1. **User Interface** - collects, normalises and validates symptoms.
2. **Knowledge Base** - stores symptoms, intermediate concepts and IF-THEN rules.
3. **Forward-Chaining Engine** - derives facts and candidate illness categories.
4. **Bayesian Module** - ranks overlapping respiratory candidates.
5. **Integration and Explanation** - combines outputs and presents readable reasoning.

The design follows an AIMA-inspired structure. The state is the set of known and derived facts. An action is the application of an applicable rule. A transition occurs when a rule conclusion is added. Reasoning stops at a fixed point when no new facts can be derived.

## 5. Evaluation Plan

The system is evaluated using eight fictional cases covering all six illness categories, multi-stage forward chaining, overlapping respiratory symptoms, explicit absent symptoms, incomplete information and cases where no rule applies.

Automated `pytest` tests separately verify knowledge-base validation, illness-category inference, present/absent/unknown handling, explanation output, overlapping candidates, Bayesian ranking and integration between components.

The current implementation passes **8/8 evaluation cases** and **14/14 automated tests**.

Evaluation will also discuss limitations, especially the simplified educational nature of the rules and Bayesian likelihood values.

## 6. Team Contributions

| Team Member | Responsibilities |
| --- | --- |
| **Hamza Zeeshan** | GitHub repository management, knowledge-base development, IF-THEN rules, forward-chaining engine, present/absent/unknown reasoning, knowledge-base validation, system integration, Bayesian integration and end-to-end testing |
| **Mohammed Younis** | Bayesian ranking module, command-line interface, explanation mechanism, evaluation framework and automated testing |

Both team members contribute to system design, documentation, evaluation and the final presentation.
