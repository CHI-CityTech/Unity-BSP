# Statement of Work (SoW)

## Development of a Mapped Virtual Twin of CHI Studios and BSPT Stage

This research develops a documented and scalable workflow for
constructing a geometrically accurate Unity-based digital twin of CHI
Studios (LG-38) and the BSPT stage, integrating modeling standards,
material pipelines, and CAD translation protocols. The project
establishes the technical and organizational infrastructure necessary to
support future blended performance research, virtual-physical
equivalence mapping, and expansion into self-aware room systems.

------------------------------------------------------------------------

## Project Overview

This project establishes a structured research and development
initiative to design, construct, and deploy a virtual environment in
Unity that spatially maps the CHI Studios physical space (LG-38) and the
BSPT stage configuration. The work is explicitly staged so that
foundational Unity capability, asset pipeline research, and asset
management systems are established before importing and integrating
external AutoCAD-derived set geometry.

The virtual environment will serve as a geometric and (later) behavioral
twin capable of supporting blended performance research, mediation
pathway testing, and future self-aware room (BABS) integration.

The project proceeds through the SRDMPA cycle: Speculate → Research →
Design → Make → Publish → Assess.

------------------------------------------------------------------------

# 1. SPECULATE

### Objectives

1.  Define the conceptual framework for a stage-specific digital twin
    within the Balanced Blended Space paradigm.
2.  Clarify the level of geometric fidelity required (structural shell
    vs. material fidelity vs. behavioral twin).
3.  Establish the intended role of the virtual layer (persistent twin,
    performance augmentation layer, or research testbed).

### Deliverables

- Concept brief: “CHI Studios Digital Twin – Conceptual Model v1.0”
- Identification of mapping levels (L1–L3 fidelity model)
- Initial mediation pathway diagram describing:
 
- Physical stage → AutoCAD geometry → Unity environment

------------------------------------------------------------------------

# 2. RESEARCH

### Objectives

1.  Establish a grounded on-ramp to Unity 3D for a student transitioning
    from 2D workflows.
2.  Investigate best-practice workflows for room-scale environment
    creation in Unity (LG-38) prior to set import.
3.  Define per-asset capability requirements (geometry, UVs, materials,
    maps, LODs, collisions, metadata, rigging where applicable).
4.  Design an asset management strategy that supports storage,
    versioning, reuse, and scalable collaboration.
5.  Investigate optimal AutoCAD → Unity conversion workflows for the
    later BSPT set integration.
6.  Evaluate unit conventions (mm, inches, meters), scaling consistency,
    and coordinate alignment.
7.  Benchmark Unity performance constraints for room-scale architecture
    and stage-scale add-ons.

### Research Workstreams

**R2.1 Unity 3D On-Ramp (2D → 3D Transition)**

- Identify core
conceptual gaps: world space vs screen space, transforms, coordinate
systems, cameras, lighting models, materials/shaders.
- Curate and test
learning resources (Unity Learn paths, documentation, targeted
tutorials).
- Produce a short internal guide: “2D-to-3D Transition Notes
for CHI Projects.”

**R2.2 Room Creation Best Practices (LG-38 as First Target)**

**R2.2.1 Internal vs External Modeling Workflow Analysis**

Research Question: What modeling workflow optimally balances fidelity,
performance, scalability, and pedagogical accessibility for CHI blended
environments?

Comparison Domains:

- Unity internal modeling (primitives / ProBuilder /
in-engine mesh tools)
- External DCC tools (e.g., Blender) → FBX/glTF →
Unity
- Hybrid workflow (external structural cleanup + Unity-side
blocking and iteration)

Evaluation Criteria:
- Geometric fidelity (dimensional accuracy,
topology quality)
- UV control and material readiness
- Lighting
response accuracy
- Runtime performance cost
- Iteration speed -
Pipeline stability (import/export friction)
- Reusability across
platforms
- Student onboarding complexity

Deliverable:
- Comparative workflow memo with recommended CHI modeling
standard

Following this comparative analysis, LG-38 will be constructed using the
selected or hybridized workflow as the first applied test case.

**R2.2.2 LG-38 Room Construction Strategy**

- Compare approaches:
- A) Model room in external DCC (Blender) → import
- B) Construct modular
room primitives in Unity (ProBuilder / primitives) → refine
- C) Hybrid:
CAD/measurement-based shell + Unity-side detailing
 - Determine measurement capture method (tape/laser measurements, existing
floorplans, or other references).
- Establish tolerance targets for
spatial fidelity.

**R2.3 Lighting Simulation Strategy (Room-Level)** (Room-Level)\*\* -
Investigate Unity lighting pipelines appropriate to the project
(URP/HDRP, baked vs realtime).
- Determine how to approximate LG-38
lighting: fixture placement proxies, color temperature approximations,
shadows, bake settings.
- Evaluate runtime cost implications and
required level of realism.

**R2.4 Materials/Texturing Strategy (Room-Level)**

This workstream explicitly explores multiple viable approaches to
approximating LG-38 surfaces (walls, floor, ceiling, doors, trim) in
Unity, including both bespoke capture and library-driven workflows. The
goal is not photorealism for its own sake, but an efficient,
reproducible best-practice pipeline that yields a convincing perceptual
match at room scale while respecting runtime constraints.

**R2.4.1 Approach A: Photo-Based Capture → Unity Material**

- Capture
surface reference photos (walls, floor, ceiling) with consistent
lighting and scale reference.
- Create tiling textures where appropriate
(cleanup seams, correct perspective, normalize color).
- Generate or
derive supporting maps as needed:
- Albedo/Base Color (diffuse)
- Normal
map (surface micro-relief)
- Roughness/Smoothness and Metallic (PBR
response)
- Ambient Occlusion (optional)
- Height/Displacement (only if
warranted; consider parallax/relief alternatives)
- Evaluate tools and
workflows for map generation (e.g., Substance 3D Sampler/Painter,
Materialize, Blender node workflows, or other acceptable open/free
tools).
- Document capture guidelines (distance, angle, lens distortion,
lighting neutrality) to make the process repeatable.

**R2.4.2 Approach B: “Close Match” Reference Images → Material
Adaptation**

- Identify existing imagery that closely resembles target
surfaces (painted drywall, acoustic ceiling tile, linoleum, concrete,
etc.).
- Adapt for Unity:
- Ensure tiling and consistent scale -
Color-correct to match LG-38 ambient appearance
- Derive/generate
normal/roughness as needed
- Track provenance and licensing for each
adapted source.

**R2.4.3 Approach C: Library/Procedural Materials (Preferred When
Viable)**

- Evaluate existing material libraries and pipelines,
including:
- Unity Asset Store materials (license scrutiny required) -
Poly Haven (CC0) materials
- Quixel Megascans (if license and account
access align)
- Adobe Substance materials (if available)
- Other vetted,
reusable libraries
- Compare library materials vs photo-based capture
on:
- visual match to LG-38
- setup effort
- runtime cost (texture
resolution, shader complexity)
- long-term maintainability

**R2.4.4 PBR and Render Pipeline Compatibility**

- Confirm the project
render pipeline (URP/HDRP) and define a consistent PBR workflow. -
Define texture packing conventions (e.g., metallic/smoothness/AO channel
packing if used) and Unity import settings.

**R2.4.5 “Good Enough” Criteria and Optimization Strategy**

- Define
acceptance criteria for room surfaces:
- perceptual match from typical
audience/participant viewpoints
- stable lighting response (no obvious
specular anomalies)
- texture resolution targets (e.g., 1K/2K/4K
guidelines) based on distance to camera
- Establish performance-oriented
policies:
- limit unique materials where possible
- reuse materials
across surfaces
- prefer tiling materials for large areas
- reserve
high-detail maps for focal surfaces only

**R2.4 Deliverables**

- Materials/Texturing Best-Practice Memo (LG-38),
including recommended default approach and fallback options
- A small
“LG-38 Material Kit” (walls/floor/ceiling) with documented provenance,
import settings, and map set conventions
- A repeatable checklist for
turning a reference photo or library material into a Unity-ready PBR
material

**R2.5 Asset Capability Requirements (Per Asset Specification)** Define
a checklist for any asset type:
- Naming + ID
- Units + scale -
Pivot/origin conventions
- Mesh topology guidelines
- UV requirements -
Material slots and texture set requirements
- Map types supported
(normal, bump, displacement, weight, etc.)
- LODs (if needed) -
Collision mesh rules
- Metadata (author, license, source, version) -
Rigging/morph targets (when applicable) (Per Asset Specification)\*\*
Define a checklist for any asset type:
- Naming + ID
- Units + scale -
Pivot/origin conventions
- Mesh topology guidelines
- UV requirements -
Material slots and texture set requirements
- Map types supported
(normal, bump, displacement, weight, etc.)
- LODs (if needed) -
Collision mesh rules
- Metadata (author, license, source, version) -
Rigging/morph targets (when applicable)

**R2.6 Asset Management System (Unity + Repo Governance)**

- Unity
project folder architecture (Assets/Art/Models, Materials, Textures,
Prefabs, Scenes, Scripts, Docs, etc.)
- Versioning strategy (Git + Git
LFS for binaries; naming and release tags)
- Prefab standards and
dependency management
- Third-party asset intake policy (licensing,
provenance, attribution)

**R2.7 AutoCAD → Unity Translation Pipeline (for Stage/Set Later)**

- Test export pipelines (AutoCAD → FBX; AutoCAD → DXF → Blender → FBX;
other robust paths).
- Identify typical failure modes (scale, normals,
triangulation, layers, naming).

### Deliverables

- Unity On-Ramp Guide: “Unity 3D Foundations for CHI (2D→3D)”
- Room Creation Best-Practice Memo (LG-38) with recommended approach
- Lighting Strategy Memo (LG-38)
- Materials/Texturing Strategy Memo (LG-38)
- Per-Asset Capability Specification Checklist v1.0
- Asset Management System Spec (Unity folder architecture + Git/LFS
  policy)
- AutoCAD-to-Unity Translation Pipeline (tested and documented)
- Performance benchmark summary

------------------------------------------------------------------------

# 3. DESIGN

### Objectives

1.  Design the Unity project architecture for the CHI Studios twin.
2.  Define folder structure and asset governance conventions.
3.  Draft the BSPT Stage Mapping Specification v1.0.
4.  Plan integration of imported TSlot configuration (from external
    AutoCAD draft).
5.  Define initial material and texture mapping standards.

### Structural Components

- CHI Studios base geometry environment
- BSPT stage placement zone
- Import staging area for TSlot configuration
- Placeholder lighting model

### Deliverables

- Unity Project Architecture Document
- BSPT Stage Mapping Specification v1.0
- Asset Naming and Folder Convention Guide
- Initial lighting strategy plan

------------------------------------------------------------------------

# 4. MAKE

### Phase 4A – Unity Foundations and Project Scaffolding

1.  Create the Unity project using the selected render pipeline
    (URP/HDRP) based on Research outputs.
2.  Implement the asset folder architecture and governance conventions.
3.  Configure Git + Git LFS (if used) and confirm reproducible
    checkout/build.
4.  Create baseline scenes and test harnesses (lighting test scene,
    material test scene).

### Phase 4B – LG-38 Room Digital Twin (Precursor Environment)

1.  Build the LG-38 room shell using the selected workflow (external
    DCC, Unity-side construction, or hybrid).
2.  Validate 1:1 spatial fidelity via measurement verification.
3.  Establish coordinate origin and axis alignment that corresponds to
    the physical room reference point.
4.  Apply baseline materials/textures to approximate the room surfaces.

### Phase 4C – LG-38 Lighting Approximation

1.  Implement a first-pass lighting rig approximating fixture positions
    and illumination behavior.
2.  Choose baked vs realtime approach per the Lighting Strategy Memo.
3.  Validate shadow behavior and runtime performance.

### Phase 4D – TSlot Import and Mapping (Set Prototype Inside LG-38)

1.  Import the AutoCAD-derived TSlot configuration after the room
    environment is stable.
2.  Clean geometry (if required) via Blender intermediary.
3.  Apply scaling correction.
4.  Apply placeholder materials and prefab structure.
5.  Validate placement, collisions, and alignment against the room
    coordinate system.

### Phase 4E – Skinning and Material Fidelity (Set-Level)

1.  Apply material approximations to match physical set components.
2.  Implement map usage where appropriate
    (normal/bump/displacement/weight).
3.  Test lighting response consistency between room and set.

### Phase 4F – Hinged Triptych Modeling (Stage Mechanics Prototype)

1.  Model hinged structural logic in Unity.
2.  Implement primitive articulated structures and correct pivot
    placement.
3.  Test rotation constraints and hinge ranges.
4.  Prepare system conventions for future rigged complexity.

### Deliverables

- Unity project scaffold with asset management conventions enforced
- Functional Unity environment of LG-38
- Lighting approximation implementation + tests
- Imported and scaled BSPT TSlot structure placed inside LG-38
- Hinged triptych articulation prototype
- Performance validation tests

------------------------------------------------------------------------

# 5. PUBLISH

### Objectives

1.  Document full workflow with reproducible steps.
2.  Publish mapping specifications to CHI repository.
3.  Produce visual documentation (screenshots, diagrams, spatial
    overlays).
4.  Prepare demonstration session for CHI collaborators.

### Deliverables

- GitHub documentation repository
- Technical white paper draft: “Stage-Specific Digital Twin for Blended
  Performance”
- Demonstration build of Unity environment

------------------------------------------------------------------------

# 6. ASSESS

### Evaluation Criteria

1.  Geometric accuracy (± tolerance threshold).
2.  Runtime performance stability.
3.  Import reproducibility.
4.  Structural scalability for future rigging.
5.  Alignment with BBS mediation principles.

### Future Expansion Path

- Integration with sensor data (BABS layer)
- Virtual character equivalence mapping
- Environmental morphing systems
- Lighting synchronization experiments

### Deliverables

- Assessment report
- Identified limitations and bottlenecks
- Roadmap for Phase II (Behavioral Twin Layer)

------------------------------------------------------------------------

# Timeline and Milestones (120-Hour Internship Plan)

The internship is structured around approximately 120 total hours. The
goal is not to complete the entire blended environment project, but to
establish a documented, reproducible foundation that future contributors
can extend.

------------------------------------------------------------------------

## Phase 1 – Orientation and Foundations (20 Hours)

**Objectives**
- Establish Unity project scaffold.
- Complete structured
2D → 3D transition review.
- Configure version control and folder
architecture.

**Milestones**
- Unity project created with selected render pipeline. -
Asset folder structure implemented.
- Git/Git LFS (if applicable)
operational.
- “Unity 3D Foundations for CHI (2D→3D)” draft completed.

**Deliverables**
- Functional Unity base project.
- On-ramp
documentation guide.

------------------------------------------------------------------------

## Phase 2 – Modeling Workflow Analysis (15 Hours)

**Objectives**
- Compare Unity internal modeling vs external DCC (e.g.,
Blender).
- Identify recommended modeling standard for CHI.

**Milestones**
- Prototype LG-38 wall section in Unity-only workflow. -
Prototype same section in Blender → Unity workflow.
- Document friction
points, scaling issues, and time cost.

**Deliverables**
- Comparative Workflow Memo.
- Recommended CHI Modeling
Standard.

------------------------------------------------------------------------

## Phase 3 – LG-38 Room Digital Twin (35 Hours)

**Objectives**
- Model LG-38 shell.
- Establish coordinate origin and
scaling accuracy.
- Implement initial materials and lighting.

**Milestones**
- LG-38 geometric shell completed (within defined
tolerance).
- Pivot/origin alignment validated.
- Base lighting
implemented (neutral blockout + refined pass).
- Material test surfaces
implemented (walls/floor/ceiling).

**Deliverables**
- Functional LG-38 Unity environment.
- Measurement
validation documentation.
- Lighting Strategy Memo.
- LG-38 Material Kit
(initial version).

------------------------------------------------------------------------

## Phase 4 – Texturing Research and Material Pipeline (20 Hours)

**Objectives**
- Evaluate photo-based, adapted-image, and library-based
workflows.
- Define PBR import standards.

**Milestones**
- At least one surface implemented using each method. -
Performance comparison documented.
- Import settings standardized.

**Deliverables**
- Materials/Texturing Best-Practice Memo.
- Repeatable
Texture Conversion Checklist.

------------------------------------------------------------------------

## Phase 5 – TSlot Import Pipeline Prototype (20 Hours)

**Objectives**
- Test AutoCAD → Unity translation workflow.
- Import
partial TSlot configuration.
- Validate scaling and alignment inside
LG-38.

**Milestones**
- CAD export pipeline tested.
- Cleaned geometry
successfully imported.
- Scaled and placed in LG-38 coordinate system.

**Deliverables**
- AutoCAD-to-Unity Translation Pipeline Document. -
Imported TSlot prototype scene.

------------------------------------------------------------------------

## Phase 6 – Hinged Triptych Prototype and Final Documentation (10 Hours)

**Objectives**
- Prototype hinged structure logic.
- Consolidate
documentation for future scalability.

**Milestones**
- Hinged pivot system functioning in Unity.
- All
documents reviewed and organized.

**Deliverables**
- Triptych hinge prototype scene.
- Consolidated
Documentation Package:
- Modeling Standard
- Asset Specification
Checklist
- Folder Architecture Guide
- Material Pipeline Guide
- CAD
Translation Guide

------------------------------------------------------------------------

# Summary

At the conclusion of 120 hours, the internship will produce:

1.  A documented Unity project scaffold.
2.  A validated LG-38 room digital twin.
3.  A defined modeling and asset governance standard.
4.  A tested CAD import pipeline prototype.
5.  A hinge articulation proof-of-concept.
6.  A comprehensive documentation package enabling future contributors
    to extend the system.

The emphasis is architectural groundwork and reproducibility rather than
full completion of the blended environment. This ensures that additional
team members can continue development within a clearly defined technical
and conceptual framework.
