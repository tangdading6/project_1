#!/usr/bin/env bash
set -euo pipefail

UV_VERSION=0.13.1
export UV_NO_MODIFY_PATH=1

current=""
if [[ -x "${HOME}/.local/bin/uv" ]]; then
  current="$("${HOME}/.local/bin/uv" --version | awk '{print $2}')"
fi

if [[ "${current}" != "${UV_VERSION}" ]]; then
  curl -LsSf "https://astral.sh/uv/${UV_VERSION}/install.sh" | sh
fi

sudo ln -sfn "${HOME}/.local/bin/uv" /usr/local/bin/uv
sudo ln -sfn "${HOME}/.local/bin/uvx" /usr/local/bin/uvx

uv python install 3.12
uv sync --frozen
