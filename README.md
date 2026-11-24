# uaap-universal-finance-agent

**Universal Finance Agent** (agent bot, a model): Ledger questions; drafts journal entries and reversals for approval.

This bot runs on the UAAP kernel, [qavril-labs/uaap](https://github.com/qavril-labs/uaap). Installing this
package registers it with the kernel through the `uaap.bots` entry point, so the kernel's service, CLI and
MCP server pick it up.

```
pip install "uaap-universal-finance-agent @ git+https://github.com/qavril-labs/uaap-universal-finance-agent.git"
python -m uaap.bots describe universal-finance-agent
```

In code:

```python
from uaap.bots import BotHost
host = BotHost(tools=register_my_tools, model=my_model)
bot = host.build("universal-finance-agent")
```

Develop: `pip install -e ".[dev]"`, then `ruff check .` and `pytest`.
The test doubles come from the kernel (`uaap.testing`). The agent standard is in the kernel's docs;
`tests/test_conformance.py` checks this bot against it.
