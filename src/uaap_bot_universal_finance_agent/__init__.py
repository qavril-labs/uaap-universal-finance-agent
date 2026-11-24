"""Universal Finance Agent: a UAAP bot, packaged on its own. Installing it registers it with the UAAP kernel."""

from uaap.bots.catalog import BotSpec

SPEC = BotSpec(
    id="universal-finance-agent",
    name="Universal Finance Agent",
    version="0.1.0",
    kind="agent",
    module="uaap_bot_universal_finance_agent.agent",
    class_name="UniversalFinanceAgent",
    needs_model=True,
    needs_inbox=False,
    summary="Ledger questions; drafts journal entries and reversals for approval.",
)
