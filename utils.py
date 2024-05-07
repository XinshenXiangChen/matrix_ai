from enum import Enum
import math

class Dir(Enum):
    UP = [0, -1]
    DOWN = [0, 1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]
    STOP = [0, 0]
        

def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 

def euclidean_dist(a, b):
    return math.dist(a, b)
