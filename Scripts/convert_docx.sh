#!/usr/bin/env bash
set -euo pipefail

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc is not installed. Install with 'brew install pandoc' or see docs/README.md."
  exit 1
fi

if [ $# -lt 1 ]; then
  echo "Usage: $0 <input.docx> [output-slug]"
  exit 1
fi

INPUT="$1"
if [ ! -f "$INPUT" ]; then
  echo "Error: input file not found: $INPUT"
  exit 1
fi

SLUG="${2:-$(basename "$INPUT" .docx | tr ' ' '-' | tr '[:upper:]' '[:lower:]')}"
ORIGINALS_DIR="docs/originals"
PROPOSALS_DIR="docs/proposals"
ASSETS_DIR="docs/assets/$SLUG"

mkdir -p "$ORIGINALS_DIR" "$PROPOSALS_DIR" "$ASSETS_DIR"
# copy original only if it's not already identical in the originals dir
DEST_ORIG="$ORIGINALS_DIR/$(basename "$INPUT")"
if [ ! -e "$DEST_ORIG" ] || ! cmp -s "$INPUT" "$DEST_ORIG"; then
  cp "$INPUT" "$DEST_ORIG"
fi

pandoc "$INPUT" -f docx -t gfm -s -o "$PROPOSALS_DIR/$SLUG.md" --extract-media="$ASSETS_DIR"

echo "Converted: $INPUT -> $PROPOSALS_DIR/$SLUG.md"
echo "Media (if any) extracted to: $ASSETS_DIR"
