# Specification for Chesss

## Overview
1. This project is to test AI capacity in game development using the Unity platform
2. As the producer, I want to coordinate the building of a chess game by AI agents.
3. Game Engine: Unity
4. development will take place on two machines, Tornado (Windows 10 + Unity Hub) and Vortex (Fedora 36 + Blender)

### GitHub Repository
1. I will create a repository on GitHub without a readme file.
2. On Tornado I will create a local directory and clone the GitHub repository.
3. On Vortex I will create a local directory and clone the GitHub repository.

### Board : Unity (Machine 1 Windows 10)
1. 8x8 grid chess board in 3D space. Ambient, gradient background, materials: marble in two shade of gray.
2. Each square is connected to an object named for it's position on the grid (use official chess conventions if possible).

### Pieces: Blender (Machine 2 Fedora 36)
1. standard chess peices, 24 in all. 16 in white and 16 in black.
2. looking for python scripts to run in blender to generate the peices.
3. these should be saved to an assets folder and pushed up to GitHub.
3. On Tornado these peices will be imported into Unity and associated with gamepiece objects.

### Start Game:
1. Unity will set all 24 peices on the board
2. Unity will swivel the board around 360 degrees at an angle to show off the board.




