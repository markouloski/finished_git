from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32

A = False
matrix_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, A, A, A, A, A, 2, A, A, A, A, A, A, A, A, A, A, 4, A, A, A, A, A, 1],
    [1, A, 2, 2, A, A, A, A, A, 2, 2, 2, A, A, A, 3, A, A, A, A, 4, A, A, 1],
    [1, A, A, A, A, A, A, A, A, A, A, 2, 2, A, A, A, 3, A, A, A, A, A, A, 1],
    [1, A, 2, 2, A, A, A, A, A, A, A, A, 2, A, 4, A, A, 3, A, A, A, 4, A, 1],
    [1, A, A, A, A, A, 4, A, A, 2, 2, A, 2, A, A, A, A, A, A, 4, A, A, A, 1],
    [1, A, 3, A, A, A, 2, A, A, 2, A, A, 2, A, A, A, 4, A, A, A, A, 4, A, 1],
    [1, A, A, 3, A, A, 2, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, 1],
    [1, A, 3, A, A, A, A, A, A, A, 3, A, A, 3, 3, A, A, A, A, 3, 3, A, A, 1],
    [1, A, 3, A, A, A, 3, 3, A, 3, A, A, A, 3, 3, A, A, A, A, 2, 3, A, A, 1],
    [1, A, A, A, A, 3, A, 3, A, A, 3, A, A, A, A, A, A, A, A, A, A, A, A, 1],
    [1, A, 4, A, 3, A, A, A, A, 3, A, A, 2, A, A, A, A, A, A, A, A, 2, A, 1],
    [1, A, A, A, A, A, 4, A, A, A, A, A, 2, 2, A, A, A, A, A, A, 2, 2, A, 1],
    [1, A, A, 4, A, A, A, A, 4, A, A, A, A, 2, 2, 2, 2, 2, 2, 2, 2, A, A, 1],
    [1, A, A, A, A, A, A, A, A, A, 4, A, A, A, A, A, A, A, A, A, A, A, A, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
mini_map = set()
collision_walls = []
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char:
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
            elif char == 3:
                world_map[(i * TILE, j * TILE)] = 3
            elif char == 4:
                world_map[(i * TILE, j * TILE)] = 4