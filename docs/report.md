# Clinical Decision Support System (CDSS) - Technical Report

## AINL3001 - Knowledge-Driven Artificial Intelligence

**TU Dublin | BSc Data Science and Artificial Intelligence**

**Group A:** Hamza Zeeshan and Mohammed Younis

## 1. Introduction

This project implements an educational Clinical Decision Support System (CDSS) in Python. Its purpose is to demonstrate knowledge representation, forward-chaining inference and Bayesian reasoning using fictional symptom information.

Several illness categories may share similar symptoms, and users may provide incomplete information. The system addresses this problem by identifying candidate illness categories through rule-based reasoning, ranking overlapping respiratory candidates through Bayesian reasoning and explaining rule-based conclusions.

The knowledge base contains 20 symptoms, 13 intermediate concepts, six illness categories and 35 IF-THEN rules. The system is an educational prototype and is not intended for medical diagnosis.

For installation instructions, repository structure, system architecture, example usage and team contributions, see the [README](../README.md).

## 2. Problem Modelling and AIMA-Inspired Formulation

The system models reported symptoms as facts and illness categories as possible conclusions. Intermediate concepts represent relationships between symptoms and allow conclusions to be derived through multiple inference stages.

| Element | Description |
| --- | --- |
| Initial state | Symptoms initially reported by the user as present, with explicitly absent symptoms retained separately. |
| State | Known and derived facts, with explicit absence retained separately. |
| Actions | Application of rules whose conditions are satisfied and whose conclusions are not already known. |
| Transition model | Addition of a newly inferred fact to the knowledge state. |
| Goal and termination condition | Reach a fixed point at which no applicable rule can produce an additional fact. |
| Output | Candidate illness categories and reasoning trace, with Bayesian ranking where applicable. |

The system uses an AIMA-inspired representation of states, actions and transitions. It does not implement a conventional path-finding search algorithm.

Reaching a fixed point allows the engine to return all categories supported by the available facts rather than stopping at the first inferred category.

## 3. Knowledge Representation

The symptom relationships used in the knowledge base were informed by publicly available HSE health information. The IF-THEN rules are simplified educational representations rather than clinically validated diagnostic rules.

The knowledge base is stored in JSON, separating domain knowledge from the reasoning engine.

It contains:

- Symptoms
- Intermediate concepts
- Illness categories
- IF-THEN rules
- Explicitly absent symptom conditions

Intermediate concepts allow the system to perform multi-stage reasoning rather than relying exclusively on direct symptom matching.

### 3.1 Example Rule

```json
{
    "id": "R1",
    "conditions": ["fever", "body_aches"],
    "conclusion": "systemic_symptoms"
}
```

### 3.2 Multi-Stage Reasoning Example

```text
IF fever AND body aches
THEN systemic symptoms

IF cough AND sore throat
THEN respiratory symptoms

IF systemic symptoms AND respiratory symptoms
THEN influenza-like illness
```

The conclusions produced by earlier rules become available as facts for subsequent rules.

### 3.3 Symptom States

| State | Meaning |
| --- | --- |
| Present | The user explicitly reports experiencing the symptom. |
| Absent | The user explicitly reports not experiencing the symptom. |
| Unknown | The user does not provide information about the symptom. |

Unknown symptoms are not automatically treated as absent.

This distinction prevents rules requiring negative evidence from firing solely because a symptom was not reported.

For example, R16 requires cough to be explicitly absent alongside the relevant derived throat-related facts before strep-throat-like illness is inferred.

### 3.4 Knowledge Base Validation

The validation mechanism checks for:

- Duplicate rule identifiers.
- Unknown rule conditions.
- Invalid absent symptom references.
- Unknown rule conclusions.

This helps maintain consistency between the rules and declared knowledge base entities. It checks structural references rather than the clinical validity of the rules.

## 4. Forward-Chaining Inference

Forward chaining is a data-driven reasoning technique that begins with known facts and applies rules to derive additional conclusions.

It is suitable for the CDSS because the starting information consists of reported symptoms, while the possible conclusions are not known in advance.

The inference engine follows this process:

1. Initialise the knowledge state using reported present symptoms.
2. Retain explicitly absent symptoms separately.
3. Examine the available IF-THEN rules.
4. Check whether positive and negative conditions are satisfied.
5. Add newly derived conclusions to the knowledge state.
6. Record the identifiers of rules that derive new facts.
7. Repeat until no additional facts can be derived.

The reasoning process terminates at a fixed point. A set is used to store known facts, preventing duplicate conclusions from being added repeatedly.

## 5. Bayesian Reasoning

### 5.1 Reasoning Under Uncertainty

In medical reasoning, the same symptoms can have multiple possible explanations. For example, fever, fatigue and cough may occur across several respiratory illness categories.

Rule-based reasoning identifies possible illness categories based on known facts. However, when multiple categories are inferred, the rules alone do not provide a numerical ranking.

Bayesian reasoning addresses this uncertainty by combining prior probabilities with observed symptom evidence.

The Bayesian component supports three overlapping respiratory categories:

- Influenza-like illness
- COVID-like illness
- Common cold-like illness

Bayesian reasoning is applied only when forward chaining identifies two or more of these categories.

### 5.2 Bayes' Theorem

Bayes' theorem allows an initial belief to be updated when new evidence becomes available.

The formula introduced in Topic 9: Reasoning under Uncertainty is:

```math
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
```

| Term | Name | Meaning |
| --- | --- | --- |
| $P(A)$ | Prior | Initial probability before observing evidence. |
| $P(B\mid A)$ | Likelihood | Probability of observing the evidence given the hypothesis. |
| $P(B)$ | Evidence | Overall probability of observing the evidence under the model. |
| $P(A\mid B)$ | Posterior | Updated probability after observing the evidence. |

In the CDSS, the hypothesis represents an illness category and the evidence represents the reported symptoms.

### 5.3 Prior Probabilities

Prior probabilities represent the initial probabilities assigned to illness categories before symptom evidence is considered.

The system uses equal prior probabilities:

| Illness Category | Prior Probability |
| --- | ---: |
| Influenza-like illness | 0.333333 |
| COVID-like illness | 0.333333 |
| Common cold-like illness | 0.333333 |

Equal priors are used as an educational modelling assumption because the system does not contain real-world disease prevalence data.

### 5.4 Conditional Probability Tables

Conditional probability describes the probability of an event occurring given that another event is known.

In the CDSS, conditional probabilities represent the likelihood of observing a particular symptom given an illness category.

The system uses the following illustrative probability scale:

| Probability | Interpretation |
| --- | --- |
| 0.8 | Strong symptom association |
| 0.5 | Moderate symptom association |
| 0.2 | Weak symptom association |

The conditional probabilities are stored in [`data/bayesian_config.json`](../data/bayesian_config.json).

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

### 5.5 Conditional Independence

The Bayesian component assumes that symptoms are conditionally independent given an illness category. This allows multiple symptom likelihoods to be multiplied when calculating candidate scores.

For example, the model combines the configured conditional probabilities of fever and fatigue for influenza-like illness:

```math
P(\text{fever},\text{fatigue}\mid\text{influenza}) =
P(\text{fever}\mid\text{influenza}) \times P(\text{fatigue}\mid\text{influenza})
```

Using the probabilities defined in our Bayesian configuration:

```math
0.8 \times 0.8 = 0.64
```

This assumption simplifies the probability calculations. However, symptoms may be correlated in real medical situations, which represents a limitation of the model.

### 5.6 Joint Probability Distribution

A joint probability distribution represents the probability of multiple events occurring together.

The CDSS calculates an unnormalised score for each eligible illness category by multiplying its prior probability by the conditional probabilities of the observed symptoms.

For example, under the model's conditional independence assumption, the joint probability of influenza-like illness, fever and fatigue is calculated as:

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
P(I,F,T)\approx 0.213333
```

The resulting value illustrates an unnormalised score under the model.

In a full ranking scenario, the system includes all reported symptoms with configured probabilities and normalises each score against the scores of other eligible illness categories.

Fever and fatigue alone are not a complete example that activates Bayesian ranking.

### 5.7 Handling Present, Absent and Unknown Symptoms

The system distinguishes between symptoms that are present, explicitly absent or unknown.

For explicitly absent symptoms, the complement rule is applied:

```math
P(\neg A)=1-P(A)
```

When applied to conditional probability:

```math
P(\neg S|D)=1-P(S|D)
```

| Symptom State | Calculation |
| --- | --- |
| Present | Multiply by the conditional probability of the symptom. |
| Absent | Multiply by one minus the conditional probability. |
| Unknown | Exclude the symptom from the calculation. |
| No configured probability | Exclude the symptom from the calculation. |

For example, if the conditional probability of fever given an illness category is 0.8, the probability of fever being absent under the model is:

```math
1-0.8=0.2
```

Unknown symptoms are not automatically treated as absent.

### 5.8 Posterior Probability Calculation

Bayes' theorem updates prior probabilities using observed evidence.

The system first calculates an unnormalised score for each eligible respiratory candidate. Each score is then divided by the sum of all eligible candidate scores.

For three eligible respiratory candidates:

```math
R_{\text{influenza}}=
\frac{S_{\text{influenza}}}
{S_{\text{influenza}}+S_{\text{COVID}}+S_{\text{cold}}}
```

The same calculation is applied to the remaining candidates.

The resulting scores sum to approximately 1, subject to rounding, and are sorted from highest to lowest.

Because the calculation is restricted to respiratory candidates identified by forward chaining, the outputs are presented as relative ranking scores rather than clinical diagnostic probabilities.

### 5.9 Worked Bayesian Example

Consider the following reported symptoms:

```text
fever, fatigue, cough, sore_throat,
loss_of_smell, runny_nose, sneezing
```

No explicitly absent symptoms are provided in this example.

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

The worked scores match the values produced by the system in the respiratory overlap example.

## 6. Integration of Logical and Probabilistic Reasoning

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

This design retains the knowledge base as the source of candidate conclusions while using probability calculations to distinguish between overlapping respiratory candidates.

The integration module is shared by the CLI and the evaluation framework, so both use the same reasoning process.

## 7. Explanation Mechanism

The explanation mechanism improves transparency by converting fired rule identifiers into readable explanations.

Each explanation identifies:

- The rule that fired.
- The conditions that were satisfied.
- The conclusion that was inferred.

Example:

```text
R2 fired because cough and sore_throat were present or derived,
so respiratory_symptoms was inferred.
```

This allows users to understand how rule-based conclusions were reached.

The explanations describe the rules that derived new facts; the Bayesian relative scores are presented separately.

## 8. Evaluation and Results

The system is evaluated using fictional symptom scenarios covering the supported illness categories and reasoning behaviours.

The evaluation framework compares the expected and actual sets of inferred categories.

### 8.1 Evaluation Scenarios

| Scenario | Expected Behaviour | Result |
| --- | --- | --- |
| Influenza-like symptoms | Infer influenza-like illness. | Pass |
| Common cold-like symptoms | Infer common cold-like illness. | Pass |
| COVID-like symptoms | Infer COVID-like illness. | Pass |
| Allergy-like symptoms | Infer allergy-like illness. | Pass |
| Strep-throat-like symptoms | Infer strep-throat-like illness with appropriate negative evidence. | Pass |
| Gastrointestinal symptoms | Infer gastroenteritis-like illness. | Pass |
| Overlapping respiratory symptoms | Identify multiple respiratory candidates. | Pass |
| Insufficient information | Return no illness candidates. | Pass |

### 8.2 Evaluation Results

| Metric | Result |
| --- | ---: |
| Evaluation cases | 8 |
| Passed | 8 |
| Failed | 0 |
| Pass rate | 100% |

All eight scenarios produced the expected candidate categories.

The overlap case demonstrates that the inference engine can identify multiple categories instead of forcing a single conclusion.

The insufficient information case demonstrates that the engine does not infer a category when the necessary rule conditions are not satisfied.

These results measure agreement between expected and actual prototype behaviour, not medical diagnostic accuracy.

The evaluation framework verifies candidate categories; Bayesian ranking behaviour is verified separately through automated tests and the worked example.

### 8.3 Automated Testing

Automated tests are implemented using Pytest.

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

| Metric | Result |
| --- | ---: |
| Total tests | 17 |
| Passed | 17 |
| Failed | 0 |
| Pass rate | 100% |

The automated tests complement the fictional evaluation scenarios by verifying individual reasoning behaviours and integration.

Tests for present, absent and unknown cough evidence verify that the negative condition in R16 is not satisfied by missing information.

The Bayesian tests verify that relative rankings change when explicitly absent evidence is supplied and that ranking is skipped when only one eligible candidate is inferred.

See the [README](../README.md#8-evaluation-and-automated-testing) for commands to reproduce these results.

## 9. Assumptions and Limitations

The system is an educational prototype and has several limitations.

### 9.1 Simplified Knowledge Base

The knowledge base contains a limited number of symptoms, intermediate concepts and illness categories.

It does not represent the full complexity of medical knowledge.

### 9.2 Illustrative Bayesian Parameters

Prior probabilities and symptom likelihoods are educational modelling assumptions rather than estimates obtained from clinical datasets.

The relative scores should not be interpreted as diagnostic probabilities.

### 9.3 Conditional Independence

The Bayesian implementation assumes symptoms are conditionally independent given an illness category.

In reality, symptoms may be correlated.

### 9.4 Limited Candidate Generation

Bayesian reasoning only ranks eligible respiratory candidates already identified by forward chaining.

An illness category that is not inferred by the rule-based system cannot subsequently be introduced by Bayesian ranking.

### 9.5 Limited Evaluation

The system is evaluated using fictional scenarios and automated software tests rather than real patient records.

Passing all tests does not establish clinical validity, safety or diagnostic accuracy.

## 10. Future Improvements

Potential extensions include:

- Expanding the knowledge base.
- Supporting additional illness categories.
- Incorporating clinically validated probability estimates.
- Improving uncertainty representation.
- Investigating Bayesian networks to represent symptom dependencies.
- Developing a graphical user interface.
- Expanding evaluation datasets and scenarios.
- Providing more detailed explanations of probabilistic rankings.

## 11. Academic and Ethical Considerations

This project demonstrates knowledge representation, forward-chaining inference and probabilistic reasoning within an educational context.

It is not a clinically validated medical system. No real patient records are required for its fictional evaluation scenarios.

The system must not be used to make real-world medical decisions.

The team's AI assistance acknowledgement is provided in the [README](../README.md#11-ai-assistance-acknowledgement).

## 12. Conclusion

The CDSS demonstrates the integration of a structured knowledge base, multi-stage forward-chaining inference, conditional Bayesian ranking and rule-based explanations.

It distinguishes explicitly absent symptoms from unknown symptoms and allows overlapping illness categories to be retained and ranked where appropriate.

The eight fictional evaluation cases and 17 automated tests passed, supporting the intended educational reasoning behaviours.

The simplified rules, illustrative probability parameters and limited evaluation scope prevent the results from being interpreted as clinical evidence.

## 13. References

### Medical Knowledge Sources

- Health Service Executive (HSE). *Flu: Symptoms and diagnosis.*
- Health Service Executive (HSE). *Common cold.*
- Health Service Executive (HSE). *COVID-19: Symptoms overview.*
- Health Service Executive (HSE). *Diarrhoea and vomiting.*

### Lecture Material

TU Dublin (2026). *Knowledge-Driven AI, Topic 9: Reasoning under Uncertainty.* AINL3001 lecture slides.

Relevant slides:

- Slides 12-18: Probability rules and conditional probability.
- Slides 27-35: Bayes' theorem.
- Slides 45-46: Conditional probability tables.
- Slide 50: Conditional independence.
- Slides 58-61: Joint and posterior probability calculations.
- Slides 85-86: Reasoning under certainty and uncertainty.

The HSE sources inform the symptom relationships represented in the knowledge base.

The lecture material supports the theoretical approach to Bayesian reasoning.

The specific IF-THEN rules, equal priors and symptom likelihood values are simplified project-specific modelling decisions, not clinically validated parameters supplied by these sources.

---

**Developed for AINL3001 Knowledge-Driven Artificial Intelligence at TU Dublin.**