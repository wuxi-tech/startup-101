# startup-101

## Ask Grok and GPT from Claude Code (PAL MCP)

This repo ships a project-level [PAL MCP Server](https://github.com/BeehiveInnovations/pal-mcp-server) setup, so Claude Code can consult Grok 4.7 and GPT-6.1 through one OpenRouter key and combine their answers with its own.

### Setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (PAL runs through `uvx`).
2. Put your OpenRouter key in your shell environment, for example in `~/.zshrc`:
   ```bash
   export OPENROUTER_API_KEY=sk-or-v1-...
   ```
   `.mcp.json` reads it as `${OPENROUTER_API_KEY}`, so the key never goes into the repo.
3. Start `claude` from the repo root and approve the `pal` server when asked. `/mcp` should list it as connected.

### Use

Ask Claude Code in plain words, for example:

- "Use pal consensus with grok and gpt: should we build X or Y first?"
- "Ask grok via pal to review this function."
- "Use pal listmodels" to see what's available.

`grok` and `gpt` are aliases for `x-ai/grok-4.7` and `openai/gpt-6.1-sol`.

### Files

- `.mcp.json`: starts PAL with `uvx`. It pins `mcp<2` because PAL 9.8.2 crashes on startup with `mcp` 2.x.
- `pal/openrouter_models.json`: the models PAL may use. It replaces PAL's built-in list, which stops at Grok 4 and GPT-5.2. To add or update a model, copy its ID from [openrouter.ai/models](https://openrouter.ai/models) into this file.
