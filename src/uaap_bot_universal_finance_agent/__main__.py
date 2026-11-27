"""Serve this bot, and only this bot, as an MCP server over stdio: `python -m uaap_bot_universal_finance_agent`."""

import asyncio

from uaap.bots.mcp_server import serve

raise SystemExit(asyncio.run(serve(["universal-finance-agent"])))
