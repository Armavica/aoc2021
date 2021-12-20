import numpy as np
import fileinput as fi
from scipy.signal import convolve2d

inpt = fi.input()

rules = np.array([c == '#' for c in next(inpt).rstrip()], dtype=np.int_)
next(inpt)
grid = np.array([[c == '#' for c in line.rstrip()] for line in inpt], dtype=np.bool_)

kernel = np.array(2**np.arange(9).reshape((3, 3)))
fillvalue = 0
for i in range(50):
    grid = rules[convolve2d(grid, kernel, fillvalue=fillvalue)]
    fillvalue = rules[511 * fillvalue]
    if i == 1:
        print(np.sum(grid))
print(np.sum(grid))
