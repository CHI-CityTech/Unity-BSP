# Unity-BSP — CHI Digital Twin Foundations

Scope
-
This repository contains foundational research, standards, and reference materials for constructing a Unity-based digital twin of CHI Studios (LG-38) and the BSPT stage. The work focuses on creating reproducible engineering practices for
- room-scale modeling, measurement and spatial fidelity, CAD-to-Unity translation,
- asset governance, lighting/material workflows, and basic mechanical articulation
	relevant to blended performance research.

Relation to broader initiatives (BBS / BRSP / BSP)
-
This repository is explicitly aligned with the Balanced Blended Space (BBS) research initiative and complements related CHI efforts such as BRSP and BSP. The Unity-BSP project creates a reproducible research environment for investigating spaces that are both "blended" (virtual and physical layers co-exist and interact) and "balanced" (designs that give equivalent experimental weight to both virtual and physical realities).

Research focus and goals:

- Define and validate engineering practices that preserve spatial and
	behavioral parity between physical and virtual representations.
- Establish measurable criteria for "balance" between virtual and
	physical layers (e.g., parity of interaction, perceptual equivalence,
	and functional interchangeability).
- Provide reproducible pipelines for measurement, CAD translation,
	asset governance, and lighting/material workflows that support BBS
	experiments.
- Serve as a shared platform for staged experiments that compare
	participant responses, system performance, and alignment strategies
	across virtual-only, physical-only, and blended conditions.

This repository is intended as the technical foundation for BBS-style
experiments: standardized inputs (floorplans, CAD exports, measurements),
repeatable conversion and import steps, and documented deliverables that
make results comparable across iterations and researchers.

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
