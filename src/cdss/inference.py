from knowledge_base import load_knowledge_base


def forward_chaining(initial_facts, rules):
    known_facts = set(initial_facts)
    fired_rules = []

    while True:
        new_fact_added = False

        for rule in rules:
            conditions = rule["conditions"]
            conclusion = rule["conclusion"]

            if all(condition in known_facts for condition in conditions):
                if conclusion not in known_facts:
                    known_facts.add(conclusion)
                    fired_rules.append(rule["id"])
                    new_fact_added = True

        if not new_fact_added:
            break

    return known_facts, fired_rules


if __name__ == "__main__":
    knowledge_base = load_knowledge_base()

    initial_facts = {
        "fever",
        "body_aches",
        "cough",
        "sore_throat"
    }

    known_facts, fired_rules = forward_chaining(
        initial_facts,
        knowledge_base["rules"]
    )

    print("Initial facts:", sorted(initial_facts))
    print("Final known facts:", sorted(known_facts))
    print("Rules fired:", fired_rules)