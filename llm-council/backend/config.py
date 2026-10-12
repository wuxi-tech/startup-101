"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def _model_list(value: str) -> list:
    """Parse a comma-separated list of model identifiers."""
    return [m.strip() for m in value.split(",") if m.strip()]


# Council members - list of OpenRouter model identifiers.
# Override in .env with COUNCIL_MODELS=model-a,model-b,... when a model is retired.
COUNCIL_MODELS = _model_list(os.getenv(
    "COUNCIL_MODELS",
    "openai/gpt-6.1-sol,anthropic/claude-sonnet-5.5,x-ai/grok-4.7",
))

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = os.getenv("CHAIRMAN_MODEL", "anthropic/claude-opus-5.5")

# Small, cheap model used only to title conversations
TITLE_MODEL = os.getenv("TITLE_MODEL", "anthropic/claude-haiku-5.5")

# How many earlier messages (user + council answers) to send with a follow-up
MAX_HISTORY_MESSAGES = int(os.getenv("MAX_HISTORY_MESSAGES", "10"))

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
