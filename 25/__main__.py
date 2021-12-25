import fileinput as fi
import numpy as np

grid = np.array([list(line.rstrip()) for line in fi.input()])


def step(grid):
    grid = np.array(grid)
    mask = (grid == ".") & (np.roll(grid, 1, axis=1) == ">")
    grid[mask] = ">"
    grid[np.roll(mask, -1, axis=1)] = "."
    mask = (grid == ".") & (np.roll(grid, 1, axis=0) == "v")
    grid[mask] = "v"
    grid[np.roll(mask, -1, axis=0)] = "."
    return grid


n = 0
newgrid = np.array(grid)
while n == 0 or not np.array_equal(grid, newgrid):
    grid = newgrid
    newgrid = step(grid)
    n += 1

print(n)
