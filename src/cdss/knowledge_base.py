import json
from pathlib import Path


def load_knowledge_base():
    project_root = Path(__file__).resolve().parents[2]
    file_path = project_root / "data" / "knowledge_base.json"

    with open(file_path, "r", encoding="utf-8") as file:
        knowledge_base = json.load(file)

    return knowledge_base


def validate_knowledge_base(knowledge_base):
    symptoms = set(knowledge_base["symptoms"])
    intermediate_concepts = set(knowledge_base["intermediate_concepts"])
    illness_categories = set(knowledge_base["illness_categories"])
    rules = knowledge_base["rules"]

    valid_facts = (
        symptoms
        | intermediate_concepts
        | illness_categories
    )

    errors = []

    # Check for duplicate rule IDs
    rule_ids = [rule["id"] for rule in rules]

    if len(rule_ids) != len(set(rule_ids)):
        errors.append("Duplicate rule IDs found.")

    # Check every rule
    for rule in rules:
        rule_id = rule["id"]

        conditions = rule.get("conditions", [])
        absent_conditions = rule.get("absent_conditions", [])
        conclusion = rule["conclusion"]

        for condition in conditions:
            if condition not in valid_facts:
                errors.append(
                    f"{rule_id}: Unknown condition '{condition}'"
                )

        for condition in absent_conditions:
            if condition not in symptoms:
                errors.append(
                    f"{rule_id}: Unknown absent symptom '{condition}'"
                )

        if conclusion not in valid_facts:
            errors.append(
                f"{rule_id}: Unknown conclusion '{conclusion}'"
            )

    return errors



if __name__ == "__main__":
    knowledge_base = load_knowledge_base()

    errors = validate_knowledge_base(knowledge_base)

    if errors:
        print("Knowledge base validation failed:")

        for error in errors:
            print("-", error)

    else:
        print("Knowledge base validation passed.")
        print("Symptoms:", len(knowledge_base["symptoms"]))
        print(
            "Intermediate concepts:",
            len(knowledge_base["intermediate_concepts"])
        )
        print(
            "Illness categories:",
            len(knowledge_base["illness_categories"])
        )
        print("Rules:", len(knowledge_base["rules"]))