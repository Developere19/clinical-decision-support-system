import json
from pathlib import Path


def load_knowledge_base():
    project_root = Path(__file__).resolve().parents[2]
    file_path = project_root / "data" / "knowledge_base.json"

    with open(file_path, "r", encoding="utf-8") as file:
        knowledge_base = json.load(file)

    return knowledge_base


if __name__ == "__main__":
    knowledge_base = load_knowledge_base()

    print("Symptoms:", knowledge_base["symptoms"])
    print("Intermediate concepts:", knowledge_base["intermediate_concepts"])
    print("Illness categories:", knowledge_base["illness_categories"])
    print("Rules:", knowledge_base["rules"])