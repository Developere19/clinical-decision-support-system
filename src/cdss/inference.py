from knowledge_base import load_knowledge_base


def forward_chaining(present_facts, absent_facts, rules):
    known_facts = set(present_facts)
    absent_facts = set(absent_facts)
    fired_rules = []

    while True:
        new_fact_added = False

        for rule in rules:
            conditions = rule.get("conditions", [])
            absent_conditions = rule.get("absent_conditions", [])
            conclusion = rule["conclusion"]

            positive_conditions_met = all(
                condition in known_facts
                for condition in conditions
            )

            negative_conditions_met = all(
                condition in absent_facts
                for condition in absent_conditions
            )

            if positive_conditions_met and negative_conditions_met:
                if conclusion not in known_facts:
                    known_facts.add(conclusion)
                    fired_rules.append(rule["id"])
                    new_fact_added = True

        if not new_fact_added:
            break

    return known_facts, fired_rules


if __name__ == "__main__":
    knowledge_base = load_knowledge_base()

    present_facts = {
        "vomiting",
        "stomach_cramps"
    }

    absent_facts = set()

    known_facts, fired_rules = forward_chaining(
        present_facts,
        absent_facts,
        knowledge_base["rules"]
    )

    print("Present facts:", sorted(present_facts))
    print("Absent facts:", sorted(absent_facts))
    print("Final known facts:", sorted(known_facts))
    print("Rules fired:", fired_rules)