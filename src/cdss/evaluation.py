from integration import run_cdss


EVALUATION_CASES = [
    {
        "name": "Influenza-like multi-stage case",
        "present": {"fever", "fatigue", "cough", "sore_throat"},
        "absent": set(),
        "expected_candidates": {"influenza_like"},
    },
    {
        "name": "Common cold-like case",
        "present": {"blocked_nose", "sneezing", "sore_throat"},
        "absent": set(),
        "expected_candidates": {"common_cold_like"},
    },
    {
        "name": "COVID-like multi-stage case",
        "present": {
            "cough",
            "fatigue",
            "shortness_of_breath",
            "loss_of_smell",
        },
        "absent": set(),
        "expected_candidates": {"covid_like"},
    },
    {
        "name": "Allergy-like case",
        "present": {"blocked_nose", "itchy_nose", "runny_nose"},
        "absent": set(),
        "expected_candidates": {"allergy_like"},
    },
    {
        "name": "Strep-throat-like case with cough absent",
        "present": {"sore_throat", "fever", "swollen_neck_glands"},
        "absent": {"cough"},
        "expected_candidates": {"strep_throat_like"},
    },
    {
        "name": "Gastroenteritis-like case",
        "present": {"diarrhoea", "stomach_cramps"},
        "absent": set(),
        "expected_candidates": {"gastroenteritis_like"},
    },
    {
        "name": "Respiratory overlap case",
        "present": {
            "fever",
            "fatigue",
            "cough",
            "sore_throat",
            "loss_of_smell",
            "runny_nose",
            "sneezing",
        },
        "absent": set(),
        "expected_candidates": {
            "influenza_like",
            "common_cold_like",
            "covid_like",
        },
    },
    {
        "name": "Insufficient information case",
        "present": {"headache"},
        "absent": set(),
        "expected_candidates": set(),
    },
]


def evaluate_case(case):
    result = run_cdss(
        present_facts=case["present"],
        absent_facts=case["absent"]
    )

    actual = set(result["candidate_categories"])
    expected = set(case["expected_candidates"])

    return {
        "name": case["name"],
        "passed": actual == expected,
        "expected": sorted(expected),
        "actual": sorted(actual),
        "rules_fired": result["fired_rules"],
    }


def run_evaluation():
    results = [
        evaluate_case(case)
        for case in EVALUATION_CASES
    ]

    passed = sum(result["passed"] for result in results)

    print(f"Passed {passed}/{len(results)} evaluation cases.\n")

    for result in results:
        status = "PASS" if result["passed"] else "FAIL"

        print(f"[{status}] {result['name']}")
        print("Expected:", result["expected"])
        print("Actual:", result["actual"])
        print("Rules fired:", result["rules_fired"])
        print()

    return results


if __name__ == "__main__":
    run_evaluation()
