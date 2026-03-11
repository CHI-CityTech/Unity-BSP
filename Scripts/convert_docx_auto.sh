#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <input.docx> [slug]"
  exit 1
fi

INPUT="$1"
SLUG="${2:-}"

if command -v pandoc >/dev/null 2>&1; then
  echo "Using pandoc for conversion"
  ./scripts/convert_docx.sh "$INPUT" "$SLUG"
else
  echo "pandoc not found; trying Python fallback"
  if command -v python3 >/dev/null 2>&1; then
    python3 scripts/convert_docx_mammoth.py "$INPUT" "$SLUG"
  else
    echo "Error: neither pandoc nor python3 available. Install pandoc or ensure python3 is on PATH."
    exit 1
  fi
fi
