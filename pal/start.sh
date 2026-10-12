#!/usr/bin/env bash
# Starts the PAL MCP server through uvx. Used by .mcp.json and the SessionStart hook.
here="$(cd "$(dirname "$0")" && pwd)"
export OPENROUTER_MODELS_CONFIG_PATH="$here/openrouter_models.json"

# Some sandboxes (e.g. Claude Code cloud sessions) list PyPI in NO_PROXY but can only
# reach it through HTTPS_PROXY, so uvx fails with a DNS error. Route PyPI through the proxy.
if [ -n "${HTTPS_PROXY:-${https_proxy:-}}" ]; then
  for v in NO_PROXY no_proxy; do
    [ -n "${!v:-}" ] && export "$v=$(printf '%s' "${!v}" | tr ',' '\n' | grep -vxE 'pypi\.org|files\.pythonhosted\.org' | paste -sd, -)"
  done
fi

for p in $(command -v uvx 2>/dev/null) "$HOME/.local/bin/uvx" /opt/homebrew/bin/uvx /usr/local/bin/uvx; do
  [ -x "$p" ] && exec "$p" --with "mcp<2" --from git+https://github.com/BeehiveInnovations/pal-mcp-server.git pal-mcp-server "$@"
done
echo 'uvx not found: install uv from https://docs.astral.sh/uv/' >&2
exit 1
