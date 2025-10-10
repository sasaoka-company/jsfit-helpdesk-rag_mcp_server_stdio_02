import os
import sys

# ensure project root is on sys.path
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Add src directory to path
SRC_DIR = os.path.join(ROOT, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from src.rag_core import search
from src.config import DEFAULT_TOP_K


def test_search_returns_list_and_max_top_k():
    """Smoke test: search() returns a list of strings with length <= DEFAULT_TOP_K."""
    # use a simple prompt; behavior depends on data in docs/
    result = search("テスト")
    assert isinstance(result, list)
    assert all(isinstance(r, str) for r in result)
    assert len(result) <= DEFAULT_TOP_K
