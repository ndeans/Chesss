# Blender Chess Piece Scripts

Each script creates a single chess piece in the current Blender scene.

Usage (per piece):
1. Open Blender.
2. Open the Scripting workspace.
3. Open a script (e.g. `pawn.py`).
4. Press Run Script.

Optional export:
- Set `EXPORT_FBX_PATH` in the script to export as FBX.
- Example: `EXPORT_FBX_PATH = "//Exports/pawn.fbx"`

Notes:
- The script clears the scene before generating the piece.
- The piece is placed on the ground plane (Z = 0).
