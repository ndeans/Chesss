Here’s a concrete, end-to-end workflow and task breakdown across both
  machines. I’ve kept it practical and aligned to your spec, with minimal
  assumptions.

  Proposed Repo Layout

  - Unity/Chesss/ (Unity project root)
  - Assets/Models/ChessPieces/ (imported Blender exports)
  - Assets/Materials/Board/ (marble materials)
  - Assets/Scenes/ (main scene)
  - Blender/ (Blender source files and scripts)

  Machine 1: Tornado (Windows 10 + Unity Hub)

  1. Repo setup
      1. Create GitHub repo (no README as specified).
      2. Clone to Tornado.
  2. Unity project creation
      1. Create Unity project inside Unity/Chesss/.
      2. Commit initial Unity project structure.
  3. Board creation
      1. Build 8x8 grid in 3D.
      2. Name squares using A1–H8 (chess convention).
      3. Apply two marble materials (light/dark gray).
      4. Set ambient, gradient background (Skybox or camera background).
  4. Scene setup
      1. Add camera and lighting for showcase.
      2. Ensure board origin and scale are consistent for piece placement.
  5. Piece import
      1. Import FBX/GLB from Assets/Models/ChessPieces/.
      2. Create prefabs for each piece type.
      3. Place 24 pieces at standard starting positions.
  6. Board rotation
      1. Script a 360-degree swivel (e.g., rotating a parent GameObject).

  Machine 2: Vortex (Fedora 36 + Blender)

  1. Repo setup
      1. Clone the same GitHub repo.
  2. Blender assets
      1. Write Python scripts to generate 6 piece types.
      2. Duplicate for white/black variants.
      3. Export each piece as .fbx (Unity-friendly).
      4. Save exports to Blender/Exports/ and copy into Unity path:
         Unity/Chesss/Assets/Models/ChessPieces/.
  3. Commit
      1. Commit Blender files + scripts + exports to GitHub.

  Suggested Milestones

  1. Day 1: Repo setup + Unity project structure + board grid naming.
  2. Day 2: Blender script outputs all 6 piece types.
  3. Day 3: Unity import + prefabs + placement + rotation.
  4. Day 4: Visual polish (materials, lighting, camera).
