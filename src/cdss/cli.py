from integration import run_cdss
from knowledge_base import load_knowledge_base



def parse_symptoms(raw_text):
    """
    Convert comma-separated input into a set of normalized symptom names.
    Example:
        "fever, sore throat" -> {"fever", "sore_throat"}
    """
    symptoms = set()

    for item in raw_text.split(","):
        symptom = item.strip().lower().replace(" ", "_")

        if symptom:
            symptoms.add(symptom)

    return symptoms


def validate_user_symptoms(symptoms, allowed_symptoms):
    """
    Split symptoms into valid and invalid entries.
    """
    allowed = set(allowed_symptoms)

    valid = {symptom for symptom in symptoms if symptom in allowed}
    invalid = {symptom for symptom in symptoms if symptom not in allowed}

    return valid, invalid


def main():
    knowledge_base = load_knowledge_base()
    allowed_symptoms = knowledge_base["symptoms"]

    print("Clinical Decision Support System")
    print("Educational prototype only. This is not medical advice.\n")

    print("Available symptoms:")
    print(", ".join(sorted(allowed_symptoms)))

    present_input = input(
        "\nEnter PRESENT symptoms separated by commas: "
    )

    absent_input = input(
        "Enter explicitly ABSENT symptoms separated by commas "
        "(or press Enter): "
    )

    present_facts = parse_symptoms(present_input)
    absent_facts = parse_symptoms(absent_input)

    valid_present, invalid_present = validate_user_symptoms(
        present_facts,
        allowed_symptoms
    )

    valid_absent, invalid_absent = validate_user_symptoms(
        absent_facts,
        allowed_symptoms
    )

    invalid = sorted(invalid_present | invalid_absent)

    if invalid:
        print("\nUnknown symptoms ignored:")
        print(", ".join(invalid))

    contradiction = valid_present.intersection(valid_absent)

    if contradiction:
        print(
            "\nError: the following symptoms were entered as both "
            "present and absent:"
        )
        print(", ".join(sorted(contradiction)))
        return

    result = run_cdss(
        present_facts=valid_present,
        absent_facts=valid_absent
    )

    

    print("\nCandidate categories:")

    if result["candidate_categories"]:
        for category in result["candidate_categories"]:
            print("-", category)
    else:
        print("- No category could be inferred from the supplied facts.")

    print("\nBayesian ranking:")

    if result["bayesian_ranking"]:
        for position, item in enumerate(
            result["bayesian_ranking"],
            start=1
        ):
            print(
                f"{position}. {item['category']} "
                f"(relative score: {item['relative_score']})"
            )
    else:
        print("- Bayesian ranking not required.")

    print("\nReasoning:")

    if result["reasoning"]:
        for line in result["reasoning"]:
            print("-", line)
    else:
        print("- No rules fired.")

    print(
        "\nEducational prototype only. "
        "Do not use this output as a medical diagnosis."
    )


if __name__ == "__main__":
    main()