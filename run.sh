#!/bin/bash
# Convenience wrapper for users who do *not* wish to use the NodeJS CLI.
# It guarantees that the local Python virtual-environment exists,
# then runs `main.py` to remove the background from the provided image.

set -euo pipefail

# ── Locate project root ──────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# ── Ensure virtual-env is ready ─────────────────────────────────────────────
if [[ ! -d ".venv" ]]; then
  echo "[logistica-ribt] .venv not found – running install.sh ..."
  bash install.sh
fi

VENV_PY=".venv/bin/python"
if [[ ! -x "$VENV_PY" ]]; then
  echo "[logistica-ribt] Python executable missing inside .venv!"
  exit 1
fi

# ── Validate CLI argument ───────────────────────────────────────────────────
if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <image_path>"
  exit 1
fi

# ── Run main.py ─────────────────────────────────────────────────────────────
"$VENV_PY" main.py "$1"
