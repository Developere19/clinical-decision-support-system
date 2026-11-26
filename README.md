# Clinical Decision Support System (CDSS)

## AINL3001 - Knowledge-Driven Artificial Intelligence

**TU Dublin | BSc Data Science and Artificial Intelligence**

### Group A

| Name | Student Number | GitHub Username |
| --- | --- | --- |
| Hamza Zeeshan | C24333116 | Developere19 |
| Mohammed Younis | C24372973 | Mohammedyounis18 |

## 1. Project Overview

This project implements an educational Clinical Decision Support System (CDSS) using knowledge-driven artificial intelligence techniques in Python.

The system accepts symptoms through a command-line interface, applies rule-based forward-chaining inference to identify possible illness categories, and uses Bayesian reasoning to rank overlapping respiratory candidates.

The system also provides human-readable explanations showing how conclusions were derived.

This project is intended for educational purposes only. It does not provide medical diagnoses, prescribe medication or replace professional medical advice.

## 2. Project Objectives

- Develop a structured symptom knowledge base.
- Implement multi-stage forward-chaining inference.
- Distinguish between present, absent and unknown symptoms.
- Integrate rule-based and Bayesian reasoning.
- Provide transparent explanations of inferred conclusions.
- Evaluate system behaviour using fictional cases and automated tests.

## 3. System Scope

| Component | Quantity |
| --- | ---: |
| Illness categories | 6 |
| Symptoms | 20 |
| Intermediate concepts | 13 |
| IF-THEN rules | 35 |
| Bayesian respiratory categories | 3 |
| Fictional evaluation cases | 8 |
| Automated tests | 17 |

### Supported Illness Categories

- Influenza-like illness
- COVID-like illness
- Common cold-like illness
- Allergy-like illness
- Strep-throat-like illness
- Gastroenteritis-like illness

## 4. Repository Structure

```text
clinical-decision-support-system/
│
├── data/
│   ├── knowledge_base.json
│   └── bayesian_config.json
│
├── src/
│   └── cdss/
│       ├── knowledge_base.py
│       ├── inference.py
│       ├── bayes.py
│       ├── integration.py
│       ├── explanation.py
│       ├── cli.py
│       └── evaluation.py
│
├── tests/
│   └── test_cdss.py
│
└── README.md
```

### Component Responsibilities

| File | Purpose |
| --- | --- |
| `knowledge_base.json` | Stores symptoms, intermediate concepts, illness categories and inference rules. |
| `bayesian_config.json` | Stores prior probabilities and illustrative symptom likelihoods. |
| `knowledge_base.py` | Loads and validates the knowledge base. |
| `inference.py` | Implements the forward-chaining inference engine. |
| `bayes.py` | Implements Bayesian candidate ranking. |
| `integration.py` | Integrates the reasoning components. |
| `explanation.py` | Generates human-readable rule explanations. |
| `cli.py` | Handles user input and displays results. |
| `evaluation.py` | Evaluates expected and actual illness categories using fictional cases. |
| `test_cdss.py` | Contains automated tests for individual components and system integration. |

## 5. System Architecture

```mermaid
flowchart TD
    A[User Input] --> B[Input Validation]
    B --> C[Forward-Chaining Engine]
    K[JSON Knowledge Base] --> C
    C --> D[Candidate Illness Categories]
    D --> E{Two or More Eligible Respiratory Candidates?}
    E -->|Yes| F[Bayesian Ranking]
    P[Bayesian Configuration] --> F
    E -->|No| G[Retain Rule-Based Results]
    F --> H[System Integration]
    G --> H
    C --> I[Explanation Mechanism]
    I --> H
    H --> J[Final Output]
```

The rule-based component identifies possible illness categories before Bayesian reasoning is applied.

Bayesian ranking is conditional and is only performed when at least two eligible respiratory candidates are identified.

## 6. Knowledge Representation

The knowledge base is stored in JSON, separating domain knowledge from the reasoning engine.

It contains:

- Symptoms
- Intermediate concepts
- Illness categories
- IF-THEN rules
- Explicitly absent symptom conditions

Intermediate concepts allow the system to perform multi-stage reasoning rather than relying exclusively on direct symptom matching.

### Example Rule

```json
{
    "id": "R1",
    "conditions": ["fever", "body_aches"],
    "conclusion": "systemic_symptoms"
}
```

### Multi-Stage Reasoning Example

```text
IF fever AND body aches
THEN systemic symptoms

IF cough AND sore throat
THEN respiratory symptoms

IF systemic symptoms AND respiratory symptoms
THEN influenza-like illness
```

The conclusions produced by earlier rules become available as facts for subsequent rules.

### Symptom States

| State | Meaning |
| --- | --- |
| Present | The user explicitly reports experiencing the symptom. |
| Absent | The user explicitly reports not experiencing the symptom. |
| Unknown | The user does not provide information about the symptom. |

Unknown symptoms are not automatically treated as absent.

This distinction prevents rules requiring negative evidence from firing solely because a symptom was not reported.

### Knowledge Base Validation

The validation mechanism checks for:

- Duplicate rule identifiers.
- Unknown rule conditions.
- Invalid absent symptom references.
- Unknown rule conclusions.

This helps maintain consistency between the rules and declared knowledge base entities.

## 7. Forward-Chaining Inference

Forward chaining is a data-driven reasoning technique that begins with known facts and applies rules to derive additional conclusions.

The inference engine follows this process:

1. Initialise the knowledge state using reported present symptoms.
2. Retain explicitly absent symptoms separately.
3. Examine the available IF-THEN rules.
4. Check whether positive and negative conditions are satisfied.
5. Add newly derived conclusions to the knowledge state.
6. Record the identifiers of rules that derive new facts.
7. Repeat until no additional facts can be derived.

The reasoning process terminates at a fixed point.

### AIMA-Inspired Problem Formulation

| Element | Description |
| --- | --- |
| Initial state | Symptoms initially reported by the user. |
| State | Known and derived facts, with explicit absence retained separately. |
| Actions | Application of rules whose conditions are satisfied. |
| Transition model | Addition of a newly inferred fact to the knowledge state. |
| Termination condition | No applicable rule can produce an additional fact. |
| Output | Candidate illness categories and reasoning trace. |

The system uses an AIMA-inspired representation of states, actions and transitions. It does not implement a conventional path-finding search algorithm.

## 8. Bayesian Reasoning

### 8.1 Reasoning Under Uncertainty

In medical reasoning, the same symptoms can have multiple possible explanations. For example, fever, fatigue and cough may occur across several respiratory illness categories.

Rule-based reasoning identifies possible illness categories based on known facts. However, when multiple categories are inferred, the rules alone do not provide a numerical ranking.

Bayesian reasoning addresses this uncertainty by combining prior probabilities with observed symptom evidence.

The Bayesian component supports three overlapping respiratory categories:

- Influenza-like illness
- COVID-like illness
- Common cold-like illness

Bayesian reasoning is applied only when forward chaining identifies two or more of these categories.

### 8.2 Bayes' Theorem

Bayes' theorem allows an initial belief to be updated when new evidence becomes available.

The formula introduced in Topic 9: Reasoning under Uncertainty is:

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

| Term | Name | Meaning |
| --- | --- | --- |
| $P(A)$ | Prior | Initial probability before observing evidence. |
| $P(B\|A)$ | Likelihood | Probability of observing the evidence given the hypothesis. |
| $P(B)$ | Evidence | Overall probability of observing the evidence under the model. |
| $P(A\|B)$ | Posterior | Updated probability after observing the evidence. |

In the CDSS, the hypothesis represents an illness category and the evidence represents the reported symptoms.

### 8.3 Prior Probabilities

Prior probabilities represent the initial probabilities assigned to illness categories before symptom evidence is considered.

The system uses equal prior probabilities:

| Illness Category | Prior Probability |
| --- | ---: |
| Influenza-like illness | 0.333333 |
| COVID-like illness | 0.333333 |
| Common cold-like illness | 0.333333 |

Equal priors are used as an educational modelling assumption because the system does not contain real-world disease prevalence data.

### 8.4 Conditional Probability Tables

Conditional probability describes the probability of an event occurring given that another event is known.

In the CDSS, conditional probabilities represent the likelihood of observing a particular symptom given an illness category.

The system uses the following illustrative probability scale:

| Probability | Interpretation |
| --- | --- |
| 0.8 | Strong symptom association |
| 0.5 | Moderate symptom association |
| 0.2 | Weak symptom association |

The conditional probabilities are stored in `data/bayesian_config.json`.

| Symptom | Influenza-like | COVID-like | Common cold-like |
| --- | ---: | ---: | ---: |
| Fever | 0.8 | 0.8 | 0.2 |
| Fatigue | 0.8 | 0.8 | 0.2 |
| Cough | 0.8 | 0.8 | 0.5 |
| Sore throat | 0.5 | 0.5 | 0.8 |
| Loss of smell | 0.2 | 0.5 | 0.5 |
| Runny nose | 0.2 | 0.5 | 0.8 |
| Sneezing | 0.2 | 0.2 | 0.8 |
| Blocked nose | 0.2 | 0.5 | 0.8 |
| Headache | 0.8 | 0.5 | 0.5 |
| Body aches | 0.8 | 0.5 | 0.5 |

These values are project-specific educational modelling assumptions rather than clinically validated probabilities.

### 8.5 Conditional Independence

The Bayesian component assumes that symptoms are conditionally independent given an illness category. This allows multiple symptom likelihoods to be multiplied when calculating candidate scores.

For example, when calculating the score for influenza-like illness using fever and fatigue, the system combines their configured conditional probabilities:

```math
P(fever, fatigue \mid influenza) =
P(fever \mid influenza) \times P(fatigue \mid influenza)
```

Using the probabilities defined in our Bayesian configuration:

```math
0.8 \times 0.8 = 0.64
```

This assumption simplifies the probability calculations. However, symptoms may be correlated in real medical situations, which represents a limitation of the model.

### 8.6 Joint Probability Distribution

A joint probability distribution represents the probability of multiple events occurring together.

The CDSS calculates an unnormalised score for each eligible illness category by multiplying its prior probability by the conditional probabilities of the observed symptoms.

For example, the joint probability of influenza-like illness, fever and fatigue is calculated as:

```math
P(I,F,T)=P(I)P(F|I)P(T|I)
```

Where:

- I represents influenza-like illness.
- F represents fever.
- T represents fatigue.

Using the values defined in `bayesian_config.json`:

```math
P(I,F,T)=0.333333 \times 0.8 \times 0.8
```

```math
P(I,F,T)\approx0.213333
```

The resulting value represents an unnormalised score under the model. This score is subsequently normalised against the scores of other eligible illness categories.


### 8.7 Handling Present, Absent and Unknown Symptoms

The system distinguishes between symptoms that are present, explicitly absent or unknown.

For explicitly absent symptoms, the complement rule is applied:

$$
P(\neg A) = 1-P(A)
$$

When applied to conditional probability:

$$
P(\neg S|D) = 1-P(S|D)
$$

| Symptom State | Calculation |
| --- | --- |
| Present | Multiply by the conditional probability of the symptom. |
| Absent | Multiply by one minus the conditional probability. |
| Unknown | Exclude the symptom from the calculation. |
| No configured probability | Exclude the symptom from the calculation. |

For example, if the conditional probability of fever given an illness category is 0.8, the probability of fever being absent is:

$$
1-0.8=0.2
$$

Unknown symptoms are not automatically treated as absent.

### 8.8 Posterior Probability Calculation

Bayes' theorem updates prior probabilities using observed evidence.

The system first calculates an unnormalised score for each eligible respiratory candidate.

Each score is then divided by the sum of all eligible candidate scores.

For three eligible respiratory candidates:

$$
R_{\text{influenza}} =
\frac{S_{\text{influenza}}}
{S_{\text{influenza}}+S_{\text{COVID}}+S_{\text{cold}}}
$$

The same calculation is applied to the remaining candidates.

The resulting scores sum to approximately 1, subject to rounding, and are sorted from highest to lowest.

Because the calculation is restricted to respiratory candidates identified by forward chaining, the outputs are presented as relative ranking scores rather than clinical diagnostic probabilities.

### 8.9 Worked Bayesian Example

Consider the following reported symptoms:

```text
fever, fatigue, cough, sore_throat,
loss_of_smell, runny_nose, sneezing
```

Forward chaining identifies three possible illness categories:

- Influenza-like illness
- COVID-like illness
- Common cold-like illness

The Bayesian component calculates a score for each candidate using its prior probability and the conditional probabilities of the reported symptoms.

#### Step 1: Influenza-like Illness

```text
Score = 0.333333 × 0.8 × 0.8 × 0.8
                 × 0.5 × 0.2 × 0.2 × 0.2

Score ≈ 0.00068267
```

#### Step 2: COVID-like Illness

```text
Score = 0.333333 × 0.8 × 0.8 × 0.8
                 × 0.5 × 0.5 × 0.5 × 0.2

Score ≈ 0.00426666
```

#### Step 3: Common Cold-like Illness

```text
Score = 0.333333 × 0.2 × 0.2 × 0.5
                 × 0.8 × 0.5 × 0.8 × 0.8

Score ≈ 0.00170667
```

#### Step 4: Calculate the Total Score

```text
Total = 0.00068267 + 0.00426666 + 0.00170667

Total ≈ 0.006656
```

#### Step 5: Normalise the Scores

```text
Influenza-like = 0.00068267 / 0.006656
               ≈ 0.1026

COVID-like = 0.00426666 / 0.006656
           ≈ 0.6410

Common cold-like = 0.00170667 / 0.006656
                 ≈ 0.2564
```

#### Step 6: Final Bayesian Ranking

| Rank | Illness Category | Relative Score |
| --- | --- | ---: |
| 1 | COVID-like illness | 0.6410 |
| 2 | Common cold-like illness | 0.2564 |
| 3 | Influenza-like illness | 0.1026 |

Under the project's modelling assumptions, COVID-like illness receives the highest relative score for this fictional symptom combination.

This demonstrates how multiple observations can be combined to rank possible explanations under uncertainty.

### 8.10 Integration of Logical and Probabilistic Reasoning

Topic 9 discusses how reasoning under certainty and reasoning under uncertainty can be combined within an intelligent system.

The CDSS demonstrates this integration through two reasoning components:

| Reasoning Component | Purpose |
| --- | --- |
| Rule-based reasoning | Applies IF-THEN rules to derive facts and identify possible illness categories. |
| Bayesian reasoning | Uses prior and conditional probabilities to rank overlapping respiratory candidates. |

The integrated reasoning process is:

```text
User symptoms
      |
      v
Forward-chaining inference
      |
      v
Candidate illness categories
      |
      v
Bayesian ranking (where applicable)
      |
      v
Final results and explanations
```

Bayesian reasoning does not introduce new illness categories. It ranks eligible respiratory candidates identified by the rule-based inference engine.


### 8.11 Lecture Material

The theoretical approach is based on the following AINL3001 lecture material:

**TU Dublin (2026). Knowledge-Driven AI, Topic 9: Reasoning under Uncertainty.**

Relevant slides:

- Slides 12-18: Probability rules and conditional probability.
- Slides 27-35: Bayes' theorem.
- Slides 45-46: Conditional probability tables.
- Slide 50: Conditional independence.
- Slides 58-61: Joint and posterior probability calculations.
- Slides 85-86: Reasoning under certainty and uncertainty.

## 9. Explanation Mechanism

The explanation mechanism improves transparency by converting fired rule identifiers into readable explanations.

Each explanation identifies:

- The rule that fired.
- The conditions that were satisfied.
- The conclusion that was inferred.

Example:

```text
R2 fired because cough and sore_throat
were present or derived, so respiratory_symptoms
was inferred.
```

This allows users to understand how rule-based conclusions were reached.

## 10. Installation

### Requirements

- Python 3
- Git
- Pytest

### Clone the Repository

```bash
git clone https://github.com/Developere19/clinical-decision-support-system.git
```

Navigate to the project directory:

```bash
cd clinical-decision-support-system
```

### Install Testing Dependency

```bash
python -m pip install pytest
```

The core reasoning system uses Python's standard library.

## 11. Running the System

From the repository root, run:

```bash
python src/cdss/cli.py
```

The command-line interface allows users to:

1. View available symptoms.
2. Enter present symptoms.
3. Enter explicitly absent symptoms.
4. Receive inferred illness categories.
5. View Bayesian rankings where applicable.
6. View explanations of fired rules.

### Example Input

```text
Present symptoms:
fever, fatigue, cough, sore throat,
loss of smell, runny nose, sneezing

Absent symptoms:
```

### Expected Candidate Categories

```text
common_cold_like
covid_like
influenza_like
```

### Expected Bayesian Ranking

```text
1. covid_like        0.6410
2. common_cold_like  0.2564
3. influenza_like    0.1026
```

The system also displays the reasoning explanations associated with the inferred categories.

## 12. Evaluation

The system is evaluated using fictional symptom scenarios covering the supported illness categories and reasoning behaviours.

Run the evaluation framework:

```bash
python src/cdss/evaluation.py
```

### Evaluation Scenarios

| Scenario | Expected Behaviour |
| --- | --- |
| Influenza-like symptoms | Infer influenza-like illness. |
| Common cold-like symptoms | Infer common cold-like illness. |
| COVID-like symptoms | Infer COVID-like illness. |
| Allergy-like symptoms | Infer allergy-like illness. |
| Strep-throat-like symptoms | Infer strep-throat-like illness with appropriate negative evidence. |
| Gastrointestinal symptoms | Infer gastroenteritis-like illness. |
| Overlapping respiratory symptoms | Identify multiple respiratory candidates. |
| Insufficient information | Return no illness candidates. |

### Evaluation Results

| Metric | Result |
| --- | ---: |
| Evaluation cases | 8 |
| Passed | 8 |
| Failed | 0 |
| Pass rate | 100% |

These results measure agreement between expected and actual prototype behaviour, not medical diagnostic accuracy.

## 13. Automated Testing

Automated tests are implemented using Pytest.

Run the complete test suite:

```bash
python -m pytest -v
```

### Testing Coverage

The tests verify:

- Knowledge base validation.
- Inference across all six illness categories.
- Multi-stage forward chaining.
- Explicitly absent symptom handling.
- Unknown symptom handling.
- Present symptom handling.
- Overlapping illness candidates.
- Insufficient information behaviour.
- Explanation generation.
- Bayesian ranking of three respiratory candidates.
- Bayesian ranking of two respiratory candidates.
- Bayesian handling of explicitly absent evidence.
- Bayesian ranking being skipped for a single candidate.
- Integration between reasoning components.

### Automated Test Results

| Metric | Result |
| --- | ---: |
| Total tests | 17 |
| Passed | 17 |
| Failed | 0 |
| Pass rate | 100% |

The automated tests complement the fictional evaluation scenarios by verifying individual reasoning behaviours and integration.

## 14. Assumptions and Limitations

The system is an educational prototype and has several limitations.

### Simplified Knowledge Base

The knowledge base contains a limited number of symptoms, intermediate concepts and illness categories.

It does not represent the full complexity of medical knowledge.

### Illustrative Bayesian Parameters

Prior probabilities and symptom likelihoods are educational modelling assumptions rather than estimates obtained from clinical datasets.

The relative scores should not be interpreted as diagnostic probabilities.

### Conditional Independence

The Bayesian implementation assumes symptoms are conditionally independent given an illness category.

In reality, symptoms may be correlated.

### Limited Candidate Generation

Bayesian reasoning only ranks eligible respiratory candidates already identified by forward chaining.

An illness category that is not inferred by the rule-based system cannot subsequently be introduced by Bayesian ranking.

### Limited Evaluation

The system is evaluated using fictional scenarios and automated software tests rather than real patient records.

Passing all tests does not establish clinical validity, safety or diagnostic accuracy.

## 15. Future Improvements

Potential extensions include:

- Expanding the knowledge base.
- Supporting additional illness categories.
- Incorporating clinically validated probability estimates.
- Improving uncertainty representation.
- Investigating Bayesian networks to represent symptom dependencies.
- Developing a graphical user interface.
- Expanding evaluation datasets and scenarios.
- Providing more detailed explanations of probabilistic rankings.

## 16. Team Contributions

### Hamza Zeeshan

- GitHub repository setup and management.
- Knowledge base development.
- IF-THEN rule representation.
- Knowledge base validation.
- Forward-chaining inference engine.
- Present, absent and unknown symptom reasoning.
- System integration.
- Bayesian configuration and integration.
- Integration of Bayesian output into the CLI.
- Refinement and expansion of automated tests.
- End-to-end system testing and debugging.

### Mohammed Younis

- Bayesian ranking module.
- Command-line interface.
- Explanation mechanism.
- Evaluation framework.
- Initial automated Pytest suite.
- Component testing and debugging.

### Shared Responsibilities

- System design.
- Reasoning approach discussions.
- Evaluation planning.
- Integration testing.
- Project documentation.
- Final presentation and demonstration.

## 17. AI Assistance Acknowledgement

Generative AI tools were used to support brainstorming, code development, debugging, testing and documentation.

The team is responsible for reviewing the generated material, understanding the implemented techniques and verifying system behaviour.

## 18. Academic and Ethical Considerations

This project demonstrates knowledge representation, forward-chaining inference and probabilistic reasoning within an educational context.

It is not a clinically validated medical system.

No real patient records are required for its fictional evaluation scenarios.

The system must not be used to make real-world medical decisions.

---

**Developed for AINL3001 Knowledge-Driven Artificial Intelligence at TU Dublin.**
