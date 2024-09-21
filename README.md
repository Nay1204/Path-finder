# Path-finder with GUI Project

## Introduction

This project is a Python-based application that allows users to interactively find the shortest path between two points on a grid, avoiding obstacles. It utilizes the A* search algorithm for pathfinding and a graphical user interface (GUI) built with Tkinter.

## Features
Interactive Grid: Users can click on grid cells to set the start and end points.
Obstacle Placement: Users can create obstacles by clicking on grid cells.
Pathfinding: The A* algorithm finds the shortest path between the start and end points, avoiding obstacles.
Visual Feedback: The application visualizes the grid, obstacles, and path on the GUI.

## Implementation
The project is implemented using Python and the following libraries:
Tkinter: For creating the graphical user interface.
heapq: For maintaining the open set in the A* algorithm.

The project consists of four main files:
main.py: This file contains the main implementation of the GUI and calls the A* algorithm to find the shortest path.
node.py: This file defines the Node class, representing a node in the graph.
search.py: This file implements the A* search algorithm.
constants.py: This file contains constants for grid parameters and visualization properties.

## User Interaction
Start and End Points: Users can click on grid cells to set the start and end points.
Obstacles: Users can create obstacles by clicking on cells, except for the start and end points.
Pathfinding: Click the "Find Path" button to initiate the pathfinding process. The shortest path will be displayed in blue.

## Results
The application successfully allows users to select start and end points, add obstacles, and find the shortest path around the obstacles. The path is visualized in blue on the GUI.

## Conclusion
The "Shortest Path Finder with GUI" project provides an interactive and user-friendly way to explore pathfinding using the A* algorithm. It can serve as a foundation for more advanced pathfinding applications or educational tools.
