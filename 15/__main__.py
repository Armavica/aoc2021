import math
import numpy as np
import fileinput as fi
import heapq

def neighbors(pos, grid):
    x, y = pos
    if x > 0:
        yield (x-1, y)
    if x < grid.shape[0] - 1:
        yield (x+1, y)
    if y > 0:
        yield (x, y-1)
    if y < grid.shape[1] - 1:
        yield (x, y+1)

def solve(grid):
    border = [(0, (0, 0))]
    length_so_far = {(0, 0): 0}
    while border:
        length, (x, y) = heapq.heappop(border)
        if (x+1, y+1) == grid.shape:
            return length
        for neighbor in neighbors((x, y), grid):
            new_length = length + grid[neighbor]
            if new_length < length_so_far.get(neighbor, math.inf):
                heapq.heappush(border, (new_length, neighbor))
                length_so_far[neighbor] = new_length


grid = np.array([[int(x) for x in line.rstrip()] for line in fi.input()])

print(solve(grid))

grid = np.concatenate([((grid + i - 1) % 9) + 1 for i in range(5)], axis=0)
grid = np.concatenate([((grid + i - 1) % 9) + 1 for i in range(5)], axis=1)

print(solve(grid))
