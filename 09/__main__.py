import numpy as np
import fileinput as fi

data = np.array([[int(x) for x in l.rstrip()] for l in fi.input()])

# boolean array saying whether the point is a local minimum
local_min = np.ones_like(data, dtype=np.bool_)
local_min[:, :-1] &= data[:, :-1] < data[:, 1:]
local_min[:, 1:] &= data[:, 1:] < data[:, :-1]
local_min[:-1, :] &= data[:-1, :] < data[1:, :]
local_min[1:, :] &= data[1:, :] < data[:-1, :]

parta = np.sum(data[local_min] + 1)
assert parta == 530
print(parta)

# for each point except 9s, computing a possible direction to go deeper
downstream = {}
for iline, line in enumerate(data):
    for icol, x in enumerate(line):
        if x == 9:
            continue
        elif iline > 0 and data[iline-1, icol] < x:
            downstream[(iline, icol)] = (iline-1, icol)
        elif iline < data.shape[0] - 1 and data[iline+1, icol] < x:
            downstream[(iline, icol)] = (iline+1, icol)
        elif icol > 0 and data[iline, icol-1] < x:
            downstream[(iline, icol)] = (iline, icol-1)
        elif icol < data.shape[1] - 1 and data[iline, icol+1] < x:
            downstream[(iline, icol)] = (iline, icol+1)

# the basins around the local minima start each with a size 1
sizes = {pos: 1 for pos in zip(*np.nonzero(local_min))}

# follow the slope and increment the size of the basin
for start in downstream:
    pos = downstream[start]
    while pos in downstream:
        pos = downstream[pos]
    sizes[pos] += 1

a, b, c = sorted(sizes.values())[-3:]
partb = a * b * c
assert partb == 1019494
print(partb)

