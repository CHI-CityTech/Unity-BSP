# Research Task List

## Isaiah Martinez – Spring 2026 Internship (CHI Digital Twin Foundations)

This document enumerates the discrete research tasks required to fulfill
the approved 120-hour Statement of Work. Tasks are grouped by technical
domain and reflect the investigative, engineering, and documentation
responsibilities of the internship.

------------------------------------------------------------------------

# 1. Unity Foundations Research

1.1 Review Unity coordinate systems, transforms, scale units, and
world-space conventions.

1.2 Evaluate render pipeline options (URP vs HDRP) relative to project goals.

1.3 Document recommended Unity project configuration standards for CHI.

1.4 Identify best practices for scene organization and prefab structuring.

Deliverable: Unity Project Configuration Memo.

------------------------------------------------------------------------

# 2. Modeling Workflow Investigation

2.1 Compare Unity-native modeling tools (primitives, ProBuilder) with
external DCC workflows (e.g., Blender → FBX → Unity).

2.2 Identify advantages and limitations of each workflow in terms of:

- Scale control
- Topology cleanliness
- UV control
- Iteration speed
- Pipeline friction

2.3 Prototype a small architectural section in both workflows.

2.4 Recommend a modeling standard for CHI projects.

Deliverable: Modeling Workflow Comparison Memo.

------------------------------------------------------------------------

# 3. Measurement and Spatial Fidelity Research (LG-38)

3.1 Determine measurement acquisition method (existing plans vs physical
measurement).

3.2 Establish unit standard (meters as Unity canonical unit).

3.3 Define tolerance threshold for dimensional accuracy.

3.4 Validate coordinate origin strategy (physical-to-virtual alignment logic).

Deliverable: Scale and Coordinate Validation Document.

------------------------------------------------------------------------

# 4. Room Modeling Best Practices

4.1 Evaluate modular vs monolithic geometry strategies for architectural
modeling.

4.2 Define pivot placement conventions for room components.

4.3 Determine collision strategy (mesh collider vs primitive collider).

4.4 Benchmark polygon density appropriate for room-scale environment.

Deliverable: LG-38 Modeling Standards Summary.

------------------------------------------------------------------------

# 5. Lighting Research

5.1 Compare baked vs realtime lighting strategies.

5.2 Investigate shadow quality vs performance trade-offs.

5.3 Approximate physical light sources of LG-38 using proxy lighting.

5.4 Define lighting validation criteria (stability, realism, runtime cost).

Deliverable: Lighting Strategy Memo.

------------------------------------------------------------------------

# 6. Materials and Texturing Research

6.1 Compare photo-based texture capture vs library materials.

6.2 Evaluate PBR map requirements (albedo, normal, roughness/smoothness,
metallic, AO).

6.3 Define texture resolution guidelines for room-scale surfaces.

6.4 Establish import settings standards in Unity.

6.5 Document licensing and provenance requirements for third-party assets.

Deliverable: Materials and Texturing Best-Practice Guide.

------------------------------------------------------------------------

# 7. Asset Governance and Management Research

7.1 Define Unity folder architecture for CHI.

7.2 Establish asset naming conventions and ID structure.

7.3 Define prefab standards and dependency rules.

7.4 Evaluate Git and Git LFS requirements for binary asset storage.

7.5 Document intake policy for third-party models and textures.

Deliverable: Asset Governance and Repository Architecture Guide.

------------------------------------------------------------------------

# 8. CAD-to-Unity Translation Research

8.1 Test AutoCAD export formats (e.g., FBX, DXF).

8.2 Evaluate Blender as intermediary cleanup tool.

8.3 Identify common translation errors (scale mismatch, flipped normals,
triangulation issues).

8.4 Validate scaling and alignment inside LG-38.

8.5 Document reproducible translation protocol.

Deliverable: AutoCAD-to-Unity Translation Protocol Document.

------------------------------------------------------------------------

# 9. Mechanical Articulation Research

9.1 Investigate pivot placement logic for hinged structures.

9.2 Define rotation constraint implementation strategy.

9.3 Validate hinge articulation in Unity.

9.4 Document mechanical representation standards for stage components.

Deliverable: Hinged Triptych Prototype Notes.

------------------------------------------------------------------------

# 10. Documentation and Handoff Research

10.1 Organize all documentation into structured repository format.

10.2 Produce workflow diagrams for modeling and CAD translation.

10.3 Identify unresolved technical risks.

10.4 Draft Phase II continuation roadmap.

Deliverable: Consolidated Technical Documentation Package.

------------------------------------------------------------------------

# Success Condition

The research component of the internship is successful if each domain
above results in a documented, reproducible engineering standard that
can be adopted by subsequent CHI contributors without re-deriving
foundational decisions.
