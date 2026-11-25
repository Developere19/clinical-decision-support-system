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