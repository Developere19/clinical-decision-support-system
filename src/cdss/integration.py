from knowledge_base import load_knowledge_base
from inference import forward_chaining
from explanation import explain_result
from bayes import rank_respiratory_candidates


def run_cdss(present_facts, absent_facts):
    knowledge_base = load_knowledge_base()

    known_facts, fired_rules = forward_chaining(
        present_facts,
        absent_facts,
        knowledge_base["rules"]
    )

    illness_categories = set(
        knowledge_base["illness_categories"]
    )

    candidate_categories = sorted(
        known_facts.intersection(illness_categories)
    )

    bayesian_ranking = rank_respiratory_candidates(
        candidate_categories,
        present_facts,
        absent_facts
    )

    result = {
        "present_facts": sorted(present_facts),
        "absent_facts": sorted(absent_facts),
        "known_facts": sorted(known_facts),
        "fired_rules": fired_rules,
        "candidate_categories": candidate_categories,
        "bayesian_ranking": bayesian_ranking
    }

    explanation = explain_result(
        result,
        knowledge_base["rules"]
    )

    result["reasoning"] = explanation["reasoning"]

    return result


if __name__ == "__main__":
    result = run_cdss(
        present_facts={
            "fever",
            "fatigue",
            "cough",
            "sore_throat",
            "loss_of_smell",
            "runny_nose",
            "sneezing"
        },
        absent_facts=set()
    )

    print("Present facts:", result["present_facts"])
    print("Absent facts:", result["absent_facts"])
    print(
        "Candidate categories:",
        result["candidate_categories"]
    )
    print("Rules fired:", result["fired_rules"])

    print("\nBayesian ranking:")

    if result["bayesian_ranking"]:
        for item in result["bayesian_ranking"]:
            print(
                item["category"],
                item["relative_score"]
            )
    else:
        print(
            "Bayesian ranking not required."
        )

    print("\nReasoning:")

    for explanation in result["reasoning"]:
        print("-", explanation)