class Node:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.g = float('inf')
        self.h = 0
        self.f = 0
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f