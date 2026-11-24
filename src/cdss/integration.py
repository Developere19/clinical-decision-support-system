from knowledge_base import load_knowledge_base
from inference import forward_chaining


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

    return {
        "present_facts": sorted(present_facts),
        "absent_facts": sorted(absent_facts),
        "known_facts": sorted(known_facts),
        "fired_rules": fired_rules,
        "candidate_categories": candidate_categories
    }


if __name__ == "__main__":
    result = run_cdss(
        present_facts={
            "sore_throat",
            "fever",
            "swollen_neck_glands"
        },
        absent_facts={
            "cough"
        }
    )

    print("Present facts:", result["present_facts"])
    print("Absent facts:", result["absent_facts"])
    print("Candidate categories:", result["candidate_categories"])
    print("Rules fired:", result["fired_rules"])