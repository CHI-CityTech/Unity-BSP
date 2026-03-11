# LIDAR Capture → CAD → Unity: Research & Recommended Workflow

Status: draft

Purpose
-
This document surveys practical methods to capture indoor environments using LIDAR, process point-clouds into usable CAD or mesh assets, and import them into Unity with minimal manual intervention. The goal is a repeatable pipeline that preserves scale, coordinate alignment, and sufficient geometric fidelity for the CHI/BBS blended-and-balanced research experiments.

Key goals
-
- Minimize manual re-entry of measurements and manual tracing.
- Preserve scale and real-world coordinates through the pipeline.
- Produce assets importable to Unity (FBX/GLTF recommended) with clear provenance and QA checkpoints.
- Enable automation for repeated scans and reproducible experiments.

Capture planning
-
- Device selection: mobile LIDAR scanners, handheld LiDAR (phone/tablet), terrestrial scanners (Leica, Faro), and structured-light scanners have trade-offs in range, resolution, and processing needs. For room-scale capture, a terrestrial or handheld unit with meter-scale range and sub-centimeter accuracy is recommended.
- Coverage: plan scan positions to avoid occlusions; capture overlapping scans with 30–60% overlap for reliable registration.
- Metadata: record device, timestamp, coordinate system, and any control survey points (measured targets) used for registration.

Mobile (iPhone/iPad) LIDAR apps — practical options to pilot
-
For quick room-scale capture and rapid prototyping, modern iPhone and iPad devices with LiDAR sensors are convenient. The following apps are commonly used and worth piloting for LG-38 captures; evaluate each for export formats, scale fidelity, and metadata preservation.

- Polycam — versatile mobile LiDAR + photogrammetry app. Exports meshes and point clouds (OBJ, PLY, GLB/GLTF, FBX in paid tiers). Good for room-scale meshes and quick capture; test scale accuracy and export pipeline.
- Scaniverse — mobile capture app that produces meshes and point clouds (PLY/OBJ). Simple workflow and free tier; useful as a comparison to Polycam.
- 3d Scanner App (Laan Labs) — offers LiDAR capture and export options; supports mesh and point-cloud exports.
- Canvas (Occipital) — focused on interior scanning and producing floorplans/measurements; useful if you need Revit/IFC-friendly outputs via their services or exports.
- RoomScan LiDAR / Magicplan — mobile apps optimized for producing measured floorplans, less for detailed meshes; useful for rapid plan capture and control measurements.
- Matterport Capture — high-quality capture workflow with cloud processing and commercial export options; good for polished deliverables but requires account and may incur costs.

Pilot guidance: start with `Polycam` and `Scaniverse` for mesh/point-cloud exports plus one floorplan-oriented app (e.g., `RoomScan LiDAR`) to cross-check distances and room layout. For each app record export format, measured scale checks, and any required post-processing steps.

Point cloud data formats and storage
-
- Preferred raw formats: E57 for scanned datasets, LAS/LAZ for LiDAR point clouds, and vendor RAW (where available). Keep original files in `docs/originals/scans/` for archival.
- Use compressed formats (LAZ) for transfer efficiency; include metadata sidecar (JSON) describing device and capture parameters.

Preprocessing and registration
-
- Tools: PDAL (CLI), CloudCompare (GUI + CLI), and Open3D are useful for filtering, downsampling, and registration. PDAL can perform large-batch processing with pipelines.
- Steps:
  1. Noise filtering (statistical outlier removal).
  2. Downsample by voxel grid (preserve enough points for geometry restoration).
  3. Register overlapping scans: coarse alignment via ICP or target-based control points; refine with global registration.
  4. Merge into single, georeferenced point cloud.

Surface reconstruction (point cloud → mesh)
-
- Mesh generation options:
  - Poisson surface reconstruction (good for watertight models).
  - Ball-pivoting or screened-Poisson for non-watertight surfaces.
  - Delaunay/alpha shapes for constrained meshing.
- Tools: MeshLab, CloudCompare, Open3D, and commercial tools (RealityCapture, Autodesk ReCap) support these operations.
- Considerations:
  - Clean holes around scan edges, but avoid over-smoothing features needed for measurement.
  - Preserve scale and coordinate origin (store transforms/metadata).

Translation to CAD (BIM/CAD-friendly output)
-
- Objectives: produce geometry or vectorized representations that CAD tools accept (DWG, DXF, IFC) for downstream design or measurement.
- Approaches:
  - Scan-to-BIM: semi-automated workflows (e.g., Autodesk ReCap + Revit) extract planar surfaces, walls, and structural elements into parametric CAD/BIM models. This is useful when the requirement is editable CAD geometry.
  - Mesh→CAD: convert meshes to CAD primitives (planes, extrusions) via tools or scripts (Rhino/Grasshopper, Blender add-ons) when full BIM is not required.
  - Export neutral formats for Unity: FBX and glTF are typically used for mesh import; FBX preserves transforms and is widely supported by Unity.
- Practical recommendation: for rapid import into Unity, prioritize high-quality, cleaned meshes exported as FBX or glTF. If a downstream CAD/BIM authoring step is required, perform scan-to-BIM using ReCap/Revit or Rhino workflows.

Retopology, decimation, and LOD generation
-
- Raw meshes from scans are dense; retopology or decimation reduces vertex count while preserving form. Tools: Blender (decimate, remesh), Instant Meshes, or commercial retopology tools.
- Generate multiple LODs to support runtime performance in Unity (e.g., high for offline rendering, med/low for runtime scenes).

UVs, materials, and texture capture
-
- If visual fidelity is needed, capture synchronized photographs for photogrammetry texture baking or use tools that transfer color from point clouds to meshes.
- Bake textures and generate UVs in Blender or specialized photogrammetry tools; embed textures when exporting FBX/glTF.

Importing into Unity
-
- Preferred import formats: FBX (Unity-friendly), glTF (modern, PBR-friendly). FBX is common for Unity pipelines; glTF is recommended if you want compact PBR-compliant assets.
- Unity import considerations:
  - Unit scale: maintain meters as canonical unit; ensure exporters and importers agree on units.
  - Coordinate system: convert source axes (e.g., Z-up vs Y-up) so Unity's axes match (Unity uses Y-up by default). Record any transforms applied.
  - Pivot and origin: place scene origin meaningfully (e.g., physical survey control point) to ease alignment with other assets.
  - LOD groups and colliders: prepare simplified colliders and LOD groups prior to import or configure them after import.

Automation and minimizing manual steps
-
- Use PDAL and CloudCompare CLI for large-batch preprocessing: filtering, registration, and merging can be scripted.
- Create a Blender automation script (Python) or use MeshLab server for converting a cleaned point cloud to a decimated mesh with UVs and FBX export.
- Example automated pipeline (high-level):
  1. Ingest raw scans (E57/LAS) into PDAL pipeline for filtering and downsampling.
  2. Run CloudCompare batch for registration and merge into a single point cloud.
  3. Run a scripted Open3D/Blender process to reconstruct mesh, decimate, bake textures, and export FBX with consistent naming and metadata.
  4. Place exported FBX into Unity project `Assets/Scans/<slug>/`, import with predefined asset settings (scale, materials, collider generation), and run an editor script to create LODs and configure scene origin.

Quality assurance and validation
-
- Checkpoints:
  - Verify scale against known control measurements.
  - Confirm coordinate alignment with survey points or building plans.
  - Validate geometry integrity (no flipped normals, acceptable hole sizes).
  - Spot-check visual fidelity and LOD performance in Unity.

Risks and mitigations
-
- Large point clouds and high-density meshes can blow memory budgets; mitigate with aggressive but controlled decimation and streaming/occlusion culling in Unity.
- Automatic scan-to-CAD conversion is imperfect; reserve manual editing for critical engineered components.

Tooling summary (open-source & commercial)
-
- Open-source: PDAL, CloudCompare, MeshLab, Open3D, Blender
- Commercial: Autodesk ReCap, Revit (scan-to-BIM), RealityCapture, 3DReshaper

Recommendations (concise)
-
1. Standardize capture procedures and metadata collection (devices, control points, coordinate references).
2. Use PDAL + CloudCompare CLI scripted pipelines for repeatable preprocessing and registration.
3. For Unity-focused deliverables, produce cleaned meshes and export FBX/glTF with baked textures and LODs; reserve full BIM conversion for projects that need editable CAD.
4. Automate mesh reconstruction and export using Blender or Open3D scripts to avoid manual GUI work.
5. Include QA steps (scale, origin, visual checks) and store provenance metadata alongside delivered assets.

Sample minimal command snippets (illustrative)
-
PDAL pipeline (filter + voxel downsample):

```bash
pdal pipeline downsample-pipeline.json  # pipeline describes read, filters.outlier, filters.voxelgrid, write
```

CloudCompare CLI registration (example):

```bash
CloudCompare -O scan1.las -O scan2.las -ICP  # coarse then refine
```

Blender (headless) script to import mesh, decimate, and export FBX:

```bash
blender --background --python tools/mesh_process.py -- --input merged.ply --output export.fbx
```

Next steps
-
- Pilot the pipeline with one LG-38 scan: run capture, process with PDAL/CloudCompare, generate mesh and export FBX, then import into Unity and validate scale and alignment.
- Create automation scripts (PDAL pipelines, CloudCompare batch commands, Blender exporter) and store them in `tools/` for reproducibility.
- Document a short checklist and capture form to standardize future scans.

References and further reading
-
- PDAL: https://pdal.io/
- CloudCompare: https://cloudcompare.org/
- Open3D: http://www.open3d.org/
- Blender Python scripting: https://docs.blender.org/api/current/
- Autodesk ReCap / Revit scan-to-BIM docs
