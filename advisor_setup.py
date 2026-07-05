"""Shared setup for the Finance Advisor notebook.

Importing these from a module (instead of relying on values defined in other
notebook cells) means every cell can be run on its own — even right after a
kernel restart — without hitting `NameError: name 'Runner'/'finance_advisor'
is not defined`. A file import always resolves; cross-cell state does not.
"""

from dotenv import load_dotenv
from agents import Agent

# Load OPENAI_API_KEY from the project-root .env as a side effect of import.
load_dotenv()

QUERY_1 = "I spent $120 on groceries, $40 on Uber, and $60 on restaurants this week."
QUERY_2 = (
    "My weekly budget is $250. Based on everything I told you so far, "
    "where can I cut spending next week?"
)

INSTRUCTIONS = (
    "You are a personal finance advisor. When the user reports spending, "
    "break it down by category, total it up, and give clear, practical budget "
    "advice. Be concise and specific with dollar amounts. If asked about a "
    "budget, compare spending against it and suggest concrete places to cut. "
    "If you don't have prior spending data in the current message, say so "
    "clearly rather than guessing."
)


def build_advisor() -> Agent:
    """Return a fresh Finance Advisor agent (gpt-5-mini)."""
    return Agent(name="Finance Advisor", model="gpt-5-mini", instructions=INSTRUCTIONS)
