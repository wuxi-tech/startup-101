# LLM Council

![llmcouncil](header.jpg)

> Our copy of [karpathy/llm-council](https://github.com/karpathy/llm-council), adapted for startup-101. Changes from the original:
>
> - The council is GPT-6.1, Claude Sonnet 5.5 and Grok 4.7, with Claude Opus 5.5 as Chairman. Models can be swapped in `.env` without touching code.
> - Follow-up questions: the input box stays open after an answer, and each follow-up sends the earlier conversation (your questions and the Chairman's answers) to every stage.
>
> Karpathy's original description follows.

The idea of this repo is that instead of asking a question to your favorite LLM provider (e.g. OpenAI GPT 5.1, Google Gemini 3.0 Pro, Anthropic Claude Sonnet 4.5, xAI Grok 4, eg.c), you can group them into your "LLM Council". This repo is a simple, local web app that essentially looks like ChatGPT except it uses OpenRouter to send your query to multiple LLMs, it then asks them to review and rank each other's work, and finally a Chairman LLM produces the final response.

In a bit more detail, here is what happens when you submit a query:

1. **Stage 1: First opinions**. The user query is given to all LLMs individually, and the responses are collected. The individual responses are shown in a "tab view", so that the user can inspect them all one by one.
2. **Stage 2: Review**. Each individual LLM is given the responses of the other LLMs. Under the hood, the LLM identities are anonymized so that the LLM can't play favorites when judging their outputs. The LLM is asked to rank them in accuracy and insight.
3. **Stage 3: Final response**. The designated Chairman of the LLM Council takes all of the model's responses and compiles them into a single final answer that is presented to the user.

## Vibe Code Alert

This project was 99% vibe coded as a fun Saturday hack because I wanted to explore and evaluate a number of LLMs side by side in the process of [reading books together with LLMs](https://x.com/karpathy/status/1990577951671509438). It's nice and useful to see multiple responses side by side, and also the cross-opinions of all LLMs on each other's outputs. I'm not going to support it in any way, it's provided here as is for other people's inspiration and I don't intend to improve it. Code is ephemeral now and libraries are over, ask your LLM to change it in whatever way you like.

## Setup

### 1. Install Dependencies

The project uses [uv](https://docs.astral.sh/uv/) for project management.

**Backend:**
```bash
uv sync
```

**Frontend:**
```bash
cd frontend
npm install
cd ..
```

### 2. Configure API Key

Copy `.env.example` to `.env` in the project root and fill in your key:

```bash
OPENROUTER_API_KEY=sk-or-v1-...
```

`.env` is git-ignored, so the key never gets committed.

Get your API key at [openrouter.ai](https://openrouter.ai/). Make sure to purchase the credits you need, or sign up for automatic top up.

### 3. Configure Models (Optional)

Set any of these in `.env` to change the council (the defaults live in `backend/config.py`). Model names are [OpenRouter model IDs](https://openrouter.ai/models).

```bash
COUNCIL_MODELS=openai/gpt-6.1-sol,anthropic/claude-sonnet-5.5,x-ai/grok-4.7
CHAIRMAN_MODEL=anthropic/claude-opus-5.5
TITLE_MODEL=anthropic/claude-haiku-5.5
MAX_HISTORY_MESSAGES=10   # earlier messages sent with each follow-up
```

If OpenRouter retires a model, that model's answers will be missing and the backend logs an error for it; update the ID here.

## Running the Application

**Option 1: Use the start script**
```bash
./start.sh
```

**Option 2: Run manually**

Terminal 1 (Backend):
```bash
uv run python -m backend.main
```

Terminal 2 (Frontend):
```bash
cd frontend
npm run dev
```

Then open http://localhost:5173 in your browser.

## Tech Stack

- **Backend:** FastAPI (Python 3.10+), async httpx, OpenRouter API
- **Frontend:** React + Vite, react-markdown for rendering
- **Storage:** JSON files in `data/conversations/`
- **Package Management:** uv for Python, npm for JavaScript
