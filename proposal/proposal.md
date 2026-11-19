# Clinical Decision Support System (CDSS)

## AINL3001 - Knowledge-Driven Artificial Intelligence

**TU Dublin | BSc Data Science and Artificial Intelligence**

Revised following proposal feedback to clarify project scope, reasoning complexity, Bayesian integration and evaluation.

## 1. Team Information

**Group Name:** Group A

| Name | Student Number | GitHub Username |
|---|---|---|
| Hamza Zeeshan | C24333116 | Developere19 |
| Mohammed Younis | C24372973 | Mohammedyounis18 |

## 2. Problem Description

Many illnesses share similar symptoms, making it difficult to distinguish possible illness patterns from symptoms alone. Fever, cough and fatigue, for example, can occur across several respiratory illnesses. Users may also provide incomplete information, and some symptom combinations may fit more than one category.

Our project will develop an educational Clinical Decision Support System in Python. Users will enter symptoms through a simple command-line interface. The system will use rule-based reasoning to identify possible illness categories and Bayesian reasoning to rank selected overlapping respiratory categories while explaining how its conclusions were reached.

The knowledge base will contain approximately six illness categories, 18-20 symptoms, 8-10 intermediate concepts and 35-45 IF-THEN rules. Planned categories include influenza-like, COVID-like, common cold-like, allergy-like, strep-throat-like and gastroenteritis-like illness.

The system is for educational demonstration only. It will not diagnose conditions, prescribe medication or replace professional medical advice. All evaluation cases will be fictional.

## 3. Proposed AI Approach

The project will combine knowledge representation, rule-based reasoning, forward chaining and Bayesian reasoning under uncertainty.

### Knowledge Representation

Symptoms and derived concepts will be represented as facts. Medical relationships will be stored as structured IF-THEN rules separately from the main program logic.

The knowledge base will support multi-stage reasoning rather than only direct symptom matching. For example:

- IF fever AND body aches THEN systemic symptoms.
- IF cough AND sore throat THEN respiratory symptoms.
- IF systemic symptoms AND respiratory symptoms THEN influenza-like illness.

This allows one rule to derive a fact that can activate another rule.

Negative information will only be used when the user explicitly reports that a symptom is absent. Unreported symptoms will remain unknown.

### Forward-Chaining Inference

The inference engine will start with reported symptoms as known facts and repeatedly apply rules whose conditions are satisfied.

New conclusions will be added to the knowledge state until no further facts can be derived. The engine will also record which rules fired and which intermediate facts were produced, allowing the reasoning process to be explained.

### Bayesian Reasoning

Bayesian reasoning will be applied to three overlapping respiratory categories: influenza-like illness, COVID-like illness and common cold-like illness.

The Bayesian module will use predefined prior probabilities and symptom likelihoods to demonstrate how evidence changes the relative likelihood of each category. Probabilities will be documented and identified as educational values where illustrative.

The rule-based and Bayesian components will be integrated:

**User symptoms → Forward chaining → Candidate categories → Bayesian ranking → Explanation**

Forward chaining will identify possible categories and derived facts. When overlapping respiratory categories are identified, the Bayesian module will rank those candidates using the available evidence.

## 4. System Design

The system will use a modular Python architecture with five main components:

1. **User Interface** - collects and validates symptoms.
2. **Knowledge Base** - stores symptoms, intermediate concepts and IF-THEN rules.
3. **Forward-Chaining Engine** - derives new facts and candidate illness categories.
4. **Bayesian Module** - ranks selected overlapping respiratory categories.
5. **Integration and Explanation Module** - combines and explains the results.

The system will follow an AIMA-inspired structure. The state is the set of known and derived facts. An action is the application of an applicable rule. A transition occurs when a rule conclusion is added to the knowledge state. Reasoning stops when no rule can derive a new fact.

## 5. Evaluation Plan

The system will be evaluated using approximately 18 fictional test cases covering:

- clear illness-category matches;
- overlapping respiratory symptoms;
- incomplete information;
- multiple possible categories;
- cases where no rule applies;
- multi-step forward chaining.

Relevant respiratory cases will be compared using rule-based reasoning, Bayesian reasoning and the combined system.

Automated `pytest` tests will verify the knowledge base, chained inference, expected conclusions, Bayesian calculations and integration between the reasoning components.

The evaluation will compare expected and actual outputs and discuss limitations, including the simplified educational nature of the rules and probabilities.

## 6. Planned Contributions

| Team Member | Planned Responsibilities |
|---|---|
| Hamza Zeeshan | GitHub repository management, knowledge-base development, IF-THEN rule representation, forward-chaining inference engine and system integration |
| Mohammed Younis | Bayesian reasoning module, command-line interface, explanation mechanism, evaluation and testing |

Both team members will contribute to system design, documentation, evaluation and the final presentation.
