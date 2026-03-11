# Unity-BSP — CHI Digital Twin Foundations

This repository contains the Unity-based foundations and documentation for the CHI Studios (LG-38) digital twin and associated BSPT stage research.

Quick start:

- Converted proposals and SoWs: `docs/proposals/`
- Original `.docx` sources: `docs/originals/`
- Extracted media from conversions: `docs/assets/<slug>/`
- Conversion tools: `scripts/convert_docx.sh`, `scripts/convert_docx_auto.sh`, `scripts/convert_docx_mammoth.py`

Convert a `.docx` to Markdown (recommended):

```bash
# using pandoc (recommended)
brew install pandoc
./scripts/convert_docx.sh docs/originals/your-file.docx

# or automatic chooser (uses pandoc if present, otherwise Python fallback)
./scripts/convert_docx_auto.sh docs/originals/your-file.docx
```

If you use the Python fallback, install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Where to start:

- Read the converted proposals in `docs/proposals/`.
- Review `docs/README.md` for conversion specifics.

If you'd like, I can tidy the Markdown further (add YAML front-matter, convert numbered items to proper ordered lists, or create `docs/index.md`).
# Unity-BSP
The repository that has the Unity Project extension
