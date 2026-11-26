import json
from pathlib import Path


RESPIRATORY_CATEGORIES = {
    "influenza_like",
    "covid_like",
    "common_cold_like"
}


def load_bayesian_config():
    project_root = Path(__file__).resolve().parents[2]
    file_path = project_root / "data" / "bayesian_config.json"

    with open(file_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config


def calculate_bayesian_score(
    category,
    present_facts,
    absent_facts,
    config
):
    prior = config["priors"][category]

    likelihoods = config[
        "symptom_likelihoods"
    ][category]

    score = prior

    # Evidence for symptoms reported as present
    for symptom in present_facts:
        if symptom in likelihoods:
            score *= likelihoods[symptom]

    # Evidence for symptoms explicitly reported as absent
    for symptom in absent_facts:
        if symptom in likelihoods:
            score *= 1 - likelihoods[symptom]

    return score


def rank_respiratory_candidates(
    candidate_categories,
    present_facts,
    absent_facts
):
    respiratory_candidates = [
        category
        for category in candidate_categories
        if category in RESPIRATORY_CATEGORIES
    ]

    # Bayesian ranking is only used when the rule system
    # produces multiple respiratory candidates.
    if len(respiratory_candidates) < 2:
        return []

    config = load_bayesian_config()

    raw_scores = {}

    for category in respiratory_candidates:
        raw_scores[category] = calculate_bayesian_score(
            category,
            present_facts,
            absent_facts,
            config
        )

    total_score = sum(raw_scores.values())

    if total_score == 0:
        return []

    ranking = []

    for category, score in raw_scores.items():
        ranking.append({
            "category": category,
            "relative_score": round(
                score / total_score,
                4
            )
        })

    ranking.sort(
        key=lambda item: item["relative_score"],
        reverse=True
    )

    return ranking


if __name__ == "__main__":
    candidate_categories = [
        "common_cold_like",
        "covid_like",
        "influenza_like"
    ]

    present_facts = {
        "fever",
        "fatigue",
        "cough",
        "sore_throat",
        "loss_of_smell",
        "runny_nose",
        "sneezing"
    }

    absent_facts = set()

    ranking = rank_respiratory_candidates(
        candidate_categories,
        present_facts,
        absent_facts
    )

    print("Bayesian ranking:")

    for item in ranking:
        print(
            item["category"],
            item["relative_score"]
        )