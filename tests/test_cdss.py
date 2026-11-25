import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CDSS_PATH = PROJECT_ROOT / "src" / "cdss"

if str(CDSS_PATH) not in sys.path:
   sys.path.insert(0, str(CDSS_PATH))

from knowledge_base import load_knowledge_base, validate_knowledge_base
from integration import run_cdss
from explanation import explain_rules


def test_knowledge_base_validation():
   knowledge_base = load_knowledge_base()

   errors = validate_knowledge_base(knowledge_base)

   assert errors == []

def test_influenza_like_inference():
   result = run_cdss(
       present_facts={
           "fever",
           "fatigue",
           "cough",
           "sore_throat"
       },
       absent_facts=set()
   )

   assert "influenza_like" in result["candidate_categories"]


def test_common_cold_like_inference():
   result = run_cdss(
       present_facts={
           "blocked_nose",
           "sneezing",
           "sore_throat"
       },
       absent_facts=set()
   )

   assert "common_cold_like" in result["candidate_categories"]


def test_covid_like_inference():
   result = run_cdss(
       present_facts={
           "cough",
           "fatigue",
           "shortness_of_breath",
           "loss_of_smell"
       },
       absent_facts=set()
   )

   assert "covid_like" in result["candidate_categories"]


def test_allergy_like_inference():
   result = run_cdss(
       present_facts={
           "blocked_nose",
           "itchy_nose",
           "runny_nose"
       },
       absent_facts=set()
   )

   assert "allergy_like" in result["candidate_categories"]


def test_strep_throat_like_inference():
   result = run_cdss(
       present_facts={
           "sore_throat",
           "fever",
           "swollen_neck_glands"
       },
       absent_facts={"cough"}
   )

   assert "strep_throat_like" in result["candidate_categories"]


def test_gastroenteritis_like_inference():
   result = run_cdss(
       present_facts={
           "diarrhoea",
           "stomach_cramps"
       },
       absent_facts=set()
   )

   assert "gastroenteritis_like" in result["candidate_categories"]

def test_strep_requires_cough_absent():
   present = {
       "sore_throat",
       "fever",
       "swollen_neck_glands"
   }

   unknown_result = run_cdss(
       present_facts=present,
       absent_facts=set()
   )

   absent_result = run_cdss(
       present_facts=present,
       absent_facts={"cough"}
   )

   assert "strep_throat_like" not in unknown_result[
       "candidate_categories"
   ]

   assert "strep_throat_like" in absent_result[
       "candidate_categories"
   ]


def test_overlap_returns_multiple_candidates():
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

   assert set(result["candidate_categories"]) == {
       "common_cold_like",
       "covid_like",
       "influenza_like"
   }


def test_insufficient_information_returns_no_candidate():
   result = run_cdss(
       present_facts={"headache"},
       absent_facts=set()
   )

   assert result["candidate_categories"] == []

def test_explanation_contains_fired_rule_ids():
   knowledge_base = load_knowledge_base()

   explanations = explain_rules(
       ["R14", "R32", "R16"],
       knowledge_base["rules"]
   )

   assert len(explanations) == 3
   assert explanations[0].startswith("R14")
   assert explanations[1].startswith("R32")
   assert explanations[2].startswith("R16")


def test_explanation_handles_absent_symptom_wording():
   knowledge_base = load_knowledge_base()

   explanations = explain_rules(
       ["R16"],
       knowledge_base["rules"]
   )

   assert "cough was explicitly absent" in explanations[0]
