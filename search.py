from nodes import Node
import heapq
from rsc import *

def is_valid(node):
    return 0 <= node.x < GRID_WIDTH and 0 <= node.y < GRID_HEIGHT

def is_obstacle(node):
    return (node.x, node.y) in OBSTACLES

def heuristic(node, goal):
    return abs(node.x - goal[0]) + abs(node.y - goal[1])


def a_star(start, goal):
    open_set = []
    closed_set = set()

    start_node = Node(start[0], start[1])
    start_node.g = 0
    start_node.h = heuristic(start_node, goal)
    start_node.f = start_node.g + start_node.h

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if (current_node.x, current_node.y) == goal:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        closed_set.add((current_node.x, current_node.y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = Node(current_node.x + dx, current_node.y + dy)

            if not is_valid(neighbor) or is_obstacle(neighbor) or (neighbor.x, neighbor.y) in closed_set:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h
            neighbor.parent = current_node

            if neighbor not in open_set:
                heapq.heappush(open_set, neighbor)
                
    return None