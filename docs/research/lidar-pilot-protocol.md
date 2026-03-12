---
title: "LIDAR Pilot Protocol"
slug: "lidar-pilot"
status: "active"
owner: "Isaiah Martinez"
date: "2026-03-11"
tags: [lidar, capture, pointcloud, pilot]
version: 1.0
---

# LIDAR Pilot Protocol

Purpose
-
Define a repeatable, verifiable procedure for capturing LG-38 using mobile LiDAR (iPhone/iPad) and/or handheld/terrestrial scanners, processing point-clouds into meshes, and producing an FBX/glTF asset suitable for import into Unity. This protocol supports the LIDAR pilot activity in the Unity-BSP project.

Objectives
-
- Produce a cleaned, decimated mesh export (FBX or glTF) representing the LG-38 room shell suitable for import into Unity.
- Validate scale within ±1% of manual control measurements at 3 independent control points.
- Produce provenance metadata and a QA report documenting registration error, decimation ratios, and LOD sizes.

Dependencies
-
- Measurement & spatial fidelity protocol (control points and units)
- LIDAR capture apps or scanner hardware availability
- Processing tools: PDAL, CloudCompare, Blender (or Open3D)

Instruments / Apps
-
- Primary (pilot): iPhone/iPad with LiDAR — apps: Polycam, Scaniverse (test both)
- Secondary: desktop tools for processing — PDAL, CloudCompare, MeshLab, Blender
- Optional: terrestrial scanner (Faro/Leica) if higher-fidelity required

Capture plan
-
1. Pre-scan checklist
   - Clear major movable obstructions from primary scan areas where possible.
   - Place and measure three permanent control targets (A, B, C) with tape and record XYZ distances between them relative to a chosen reference corner.
   - Record device, app, operator, and environment notes in metadata file.

2. Scan procedure (mobile LiDAR)
   - Device settings: ensure latest app version, full battery, airplane mode on (optional), record high-quality export.
   - Walk perimeter and interior at steady speed; capture overlapping passes with ~40% overlap.
   - Capture photos where app supports texture/color acquisition.
   - Export raw scans in available formats (PLY/OBJ/GLB) and save to `docs/research/original-scans/<slug>/`.

3. Control measurements
   - Measure distances between control targets (A–B, B–C, A–C) and to two fixed room features (e.g., door jamb, stage corner) and save in metadata.

File naming & storage
-
- Store raw exports: `docs/research/original-scans/<slug>/<slug>-raw-YYYYMMDD.<ext>`
- Store merged pointclouds: `docs/research/pointclouds/<slug>/<slug>-merged.ply`
- Store final meshes: `docs/research/meshes/<slug>/<slug>-clean.fbx` and LODs `-lod1.fbx`, `-lod2.fbx`
- Store QA reports: `docs/research/qa/<slug>-qa.md`

Processing pipeline (recommended)
-
1. Preprocess & filter (PDAL or CloudCompare)
   - Remove obvious outliers and apply a voxel downsample (voxel size tuned per device, e.g., 0.01–0.05 m).
2. Register scans (if multiple) with ICP; use target-based alignment where control points exist.
3. Merge registered scans into a single pointcloud (PLY).
4. Surface reconstruction (Poisson or screened Poisson) in Open3D/CloudCompare/Blender.
5. Retopology / decimation: create LODs (high/medium/low) targeting polycounts appropriate for room-scale (e.g., high: 2–5M tris, med: 200–500k, low: 50–100k).
6. Bake textures (optional) and generate UVs.
7. Export FBX/glTF with unit set to meters and document coordinate-system transform.

Example CLI snippets (illustrative)
-
PDAL pipeline call (filter + voxel downsample):
```bash
pdal pipeline downsample-pipeline.json
```

CloudCompare registration (example):
```bash
CloudCompare -O scan1.ply -O scan2.ply -ICP
```

Blender headless export example:
```bash
blender --background --python tools/mesh_process.py -- --input merged.ply --output export.fbx
```

Validation & QA
-
- Scale check: measure distances between control points in the final mesh and compare to manual measurements; report percent error (target ≤ 1%).
- Registration error: report RMS of ICP alignment.
- Mesh integrity: check for flipped normals, non-manifold edges, and hole sizes; document fixes.
- Performance: measure triangle counts per LOD and estimate expected runtime memory footprint.

Acceptance criteria
-
- Final mesh imports into Unity with correct scale (±1%), correct orientation (Y-up), and no critical geometry failures.
- QA report present and stored in `docs/research/qa/`.

Provenance & metadata
-
- For each deliverable include metadata JSON with: `slug`, `source_files`, `device`, `app_version`, `operator`, `date`, `control_points`, and `processing_pipeline_versions`.

Safety, privacy & permissions
-
- Ensure capture does not record identifiable personal data. If photos include people, obtain consent or blur faces before publishing.

Results and notes
-
- Record findings, deviations, and recommended parameter changes in the QA report after the pilot.

Next steps
-
- Run pilot capture for LG-38 and populate `docs/research/original-scans/<slug>/` with raw exports.
- Execute the processing pipeline and produce `docs/research/meshes/<slug>/` and QA report.
- Decision point: promote to `docs/active/` and proceed to Unity import or revise capture protocol.
