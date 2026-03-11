# Unity-BSP — CHI Digital Twin Foundations

Scope
-
This repository contains foundational research, standards, and reference materials for constructing a Unity-based digital twin of CHI Studios (LG-38) and the BSPT stage. The work focuses on creating reproducible engineering practices for
- room-scale modeling, measurement and spatial fidelity, CAD-to-Unity translation,
- asset governance, lighting/material workflows, and basic mechanical articulation
	relevant to blended performance research.

Relation to broader initiatives
-
This project supports and integrates with CHI research initiatives including BRSP, BBS, and BSP by providing a documented pipeline for mapping physical spaces into Unity and by establishing engineering standards that enable reproducible blended-space experiments.

Repository contents (high-level)
-
- `docs/proposals/` — converted proposal and SoW documents (primary project text)
- `docs/originals/` — original source `.docx` files (archival)
- `docs/assets/` — extracted assets and media associated with converted docs
- `Scripts/` — helper scripts used during initial import and processing workflows
- `requirements.txt` — optional Python dependencies for local fallback tools

How to use this repository
-
- Read the documents in `docs/proposals/` to understand scope, deliverables,
	and task breakdowns.
- Use the per-document assets in `docs/assets/<slug>/` when assembling
	reference materials or visual documentation.
- Propose changes via GitHub: open an issue for major changes or submit a
	pull request for small edits to documentation.

Next recommended actions
-
- Standardize document metadata (YAML front-matter) and create `docs/index.md`
	linking all proposals for discoverability.
- Add lightweight templates to make future proposals consistent and addressable.

Contact
-
For project coordination, contact the supervising faculty listed inside the
project proposals or open an issue in this repository.

The repository that has the Unity Project extension
