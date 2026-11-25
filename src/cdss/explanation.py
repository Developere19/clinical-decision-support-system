def explain_rules(fired_rules, rules):
    """
    Convert fired rule IDs into readable explanations.

    Parameters
    ----------
    fired_rules : list[str]
        Rule IDs returned by the forward-chaining engine.
    rules : list[dict]
        Rules loaded from knowledge_base.json.

    Returns
    -------
    list[str]
        Human-readable explanations in firing order.
    """
    rule_lookup = {rule["id"]: rule for rule in rules}
    explanations = []

    for rule_id in fired_rules:
        rule = rule_lookup.get(rule_id)

        if rule is None:
            explanations.append(
                f"{rule_id} fired, but the rule definition could not be found."
            )
            continue

        conditions = rule.get("conditions", [])
        absent_conditions = rule.get("absent_conditions", [])
        conclusion = rule["conclusion"]

        reasons = []

        if conditions:
            reasons.append(
                f"{' and '.join(conditions)} were present or derived"
            )

        if absent_conditions:
            if len(absent_conditions) == 1:
                reasons.append(
                    f"{absent_conditions[0]} was explicitly absent"
            )
            else:
                reasons.append(
                    f"{' and '.join(absent_conditions)} were explicitly absent"
            )
        reason_text = " and ".join(reasons)

        explanations.append(
            f"{rule_id} fired because {reason_text}, "
            f"so {conclusion} was inferred."
        )

    return explanations


def explain_result(result, rules):
    """
    Build a complete explanation object from integration.py output.
    """
    return {
        "candidate_categories": result["candidate_categories"],
        "fired_rules": result["fired_rules"],
        "reasoning": explain_rules(result["fired_rules"], rules)
    }
