"""The bot meets the agent standard, and every edge case names a real test in this repository."""

from __future__ import annotations

import ast
from pathlib import Path

from uaap.agents.base import MANDATORY_ERROR_CODES, validate_card
from uaap.agents.guardrails import MANDATORY_GUARDRAILS
from uaap.testing.fakes import FakeCoreSaas, build_stack

from uaap_bot_universal_finance_agent.agent import UniversalFinanceAgent

TESTS_DIR = Path(__file__).resolve().parent


def _test_names() -> set[str]:
    names: set[str] = set()
    for path in TESTS_DIR.rglob("test_*.py"):
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef) and node.name.startswith("test_"):
                names.add(node.name)
    return names


def test_card_meets_the_standard() -> None:
    executor, _ = build_stack(FakeCoreSaas())
    assert validate_card(UniversalFinanceAgent.card, UniversalFinanceAgent.principal, executor.registry) == []
    assert UniversalFinanceAgent.card.guardrails >= MANDATORY_GUARDRAILS
    assert UniversalFinanceAgent.card.error_handling.keys() >= MANDATORY_ERROR_CODES
    assert "*" not in UniversalFinanceAgent.principal.grants


def test_every_edge_case_names_a_real_test() -> None:
    missing = sorted({e.test for e in UniversalFinanceAgent.card.edge_cases} - _test_names())
    assert missing == [], f"edge cases point at tests that do not exist: {missing}"
