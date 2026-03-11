# Docs: Word → Markdown conversion

Place `.docx` proposal files under `docs/originals/` and convert them to Markdown with the included script.

Layout (created by helper script):
- `docs/originals/` — store original `.docx` files
- `docs/proposals/` — converted Markdown files
- `docs/assets/<slug>/` — any images/media extracted from the `.docx`

Quick install (macOS):
```bash
# install pandoc
brew install pandoc
```

Convert a file (example):
```bash
# run from repository root
./scripts/convert_docx.sh docs/originals/my-proposal.docx
# or provide a slug/name
./scripts/convert_docx.sh docs/originals/my-proposal.docx my-proposal
```

Notes:
- The script uses `pandoc` and `--extract-media` to save images to `docs/assets/<slug>/`.
- If you prefer a pure-Python alternative, install `mammoth` (`pip install mammoth`) and I can add a fallback converter.
- The originals are copied into `docs/originals/` to preserve source files.
