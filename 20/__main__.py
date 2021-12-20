import numpy as np
import fileinput as fi
from scipy.signal import convolve2d

inpt = fi.input()

rules = np.array([c == '#' for c in next(inpt).rstrip()], dtype=np.int_)
next(inpt)

grid = []
for line in inpt:
    line = line.rstrip()
    grid.append([[0, 1][c == '#'] for c in line])
grid = np.array(grid, dtype=np.bool_)

def step(grid, fillvalue):
    con = convolve2d(grid, np.array(2**np.arange(9).reshape((3, 3))), fillvalue=fillvalue)
    return rules[con]

fillvalue = 0
for i in range(50):
    grid = step(grid, fillvalue)
    fillvalue = rules[511 * fillvalue]
    if i == 1:
        print(np.sum(grid))
print(np.sum(grid))
