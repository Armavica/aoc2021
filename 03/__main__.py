import numpy as np
from aoc2021 import lines

data = lines('s')
data = np.array([[x == '1' for x in line] for line in data])

nmeas, nbits = data.shape

na = 2 * data.sum(axis=0) >= nmeas
a = int(''.join('01'[int(x)] for x in na), 2)
b = int(''.join('10'[int(x)] for x in na), 2)
print(a * b)

# oxygen

d = data
for i in range(nbits):
    col = d[:, i]
    if 2 * col.sum() >= col.size:
        d = d[col == 1]
    else:
        d = d[col == 0]
oxy = int(''.join('01'[int(x)] for x in d[0]), 2)

# CO2

d = data
for i in range(nbits):
    col = d[:, i]
    if 2 * col.sum() >= col.size:
        d = d[col == 0]
    else:
        d = d[col == 1]
    if d.shape[0] == 1:
        break
co2 = int(''.join('01'[int(x)] for x in d[0]), 2)

print(oxy * co2)

