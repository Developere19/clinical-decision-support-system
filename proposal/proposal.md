# Clinical Decision Support System (CDSS)
## AINL3001 – Knowledge-Driven Artificial Intelligence
**TU Dublin | BSc Data Science and Artificial Intelligence**

### 1. Team Information

**Group Name:** Group A

| Name | Student Number | GitHub Username |
|---|---|---|
| Hamza Zeeshan | C24333116 | Developere19 |
| Mohammed Younis | C24372973 | Mohammedyounis18 |


### 2. Problem Description

Identifying possible illnesses based on symptoms can be challenging because many common medical conditions share similar symptoms. For example, fever, cough and fatigue may occur in several respiratory illnesses. This makes it difficult to distinguish between conditions using symptoms alone.

Our project aims to develop a rule-based Clinical Decision Support System (CDSS) using Python. The system will allow users to select symptoms through a command-line interface and receive information about possible common illness categories based on predefined rules.

The system will focus on a limited selection of common illnesses, such as influenza-like illness, common cold-like illness and other respiratory symptom patterns. Its purpose is to demonstrate how artificial intelligence can represent medical knowledge and apply logical reasoning to support decision-making.

The application will be an educational prototype rather than a clinically validated diagnostic tool. It will not provide definitive diagnoses, prescribe medication or replace professional medical advice. The system will use fictional patient examples for development and testing.

### 3. Proposed AI Approach

The project will use knowledge-driven artificial intelligence, focusing on rule-based reasoning, knowledge representation and forward chaining.

**Knowledge Representation**

Medical knowledge will be represented using IF–THEN rules stored in Python data structures. Each rule will describe a relationship between a combination of symptoms and a possible illness category.

For example:

- IF fever AND cough AND fatigue are present, THEN identify a flu-like symptom pattern.
- IF sneezing AND runny nose are present, THEN identify a common cold-like symptom pattern.

These initial examples are illustrative. The final rules will be reviewed against credible medical information sources and documented within the project.

**Rule-Based Reasoning**

An inference engine will compare the symptoms entered by the user against the rules stored in the knowledge base. When the conditions of a rule are satisfied, the system will generate a corresponding conclusion.

**Forward Chaining**

The system will use forward chaining, starting with known facts provided by the user and applying matching rules to derive conclusions. This allows the application to demonstrate how an AI system moves from input information to a reasoned output.

**Bayesian Reasoning**

The system will also explore reasoning under uncertainty using Bayes' theorem. It will use illustrative prior probabilities and symptom likelihoods to update estimates for possible illness categories. This will allow us to compare probabilistic reasoning with rule-based reasoning and demonstrate how additional evidence can influence conclusions.

**Explanation Mechanism**

The system will display which rules were activated and which symptoms contributed to each conclusion. This will make its reasoning transparent and understandable.

Where multiple rules match, the system will display the relevant possible categories rather than assume that one condition has been confirmed.

### 4. System Design

The system will be implemented in Python using a modular architecture consisting of four main components.

**1. User Interface**

A command-line interface will allow users to select symptoms from a predefined list. Input validation will prevent unsupported selections and handle missing information.

**2. Knowledge Base**

The knowledge base will contain structured IF–THEN rules representing relationships between symptoms and possible illness categories. The rules will be stored separately from the main program logic to support future updates.

**3. Inference Engine**

The inference engine will evaluate the user's symptoms against the knowledge base using forward chaining. It will identify satisfied rules, record the reasoning process and handle cases where multiple or no rules match.

**4. Results and Explanation Module**

The system will display possible illness categories, the symptoms responsible for each match and an explanation of the activated rules. It will also clearly communicate that the output is not a medical diagnosis.

The project will follow an AIMA-inspired design approach. The state will represent the user's selected symptoms and derived facts. Actions will involve applying applicable inference rules. The goal condition will be reached when no further conclusions can be derived from the available rules.

The system will be evaluated using fictional test cases covering successful matches, overlapping symptoms, missing information and cases where no rule applies. Automated tests will check whether the expected rules and conclusions are produced.

### 5. Planned Contributions

The project will be developed collaboratively, with responsibilities allocated among group members.

| Team Member | Planned Responsibilities |
|---|---|
| Hamza Zeeshan | GitHub repository management, knowledge base development, IF–THEN rule representation, and system integration |
| Mohammed Younis | Forward-chaining inference engine, Python command-line interface, and automated testing |


All group members will contribute to the system design, testing, documentation and final presentation.
