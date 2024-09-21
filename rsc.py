import random

GRID_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20
DELAY_MS = 50
OBSTACLE_PROBABILITY = 0.2 
START = None
GOAL = None 

OBSTACLES = []
for x in range(GRID_WIDTH):
    for y in range(GRID_HEIGHT):
        if random.random() < OBSTACLE_PROBABILITY and (x, y) != START and (x, y) != GOAL:
            OBSTACLES.append((x, y))

COLOR_START = "green"
COLOR_GOAL = "red"
COLOR_EMPTY = "white"
COLOR_OBSTACLE = "gray"
COLOR_PATH = "blue"
