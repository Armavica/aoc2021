import numpy as np
from aoc2021 import lines

commands = lines('si')

h = 0
d = 0
for (op, n) in commands:
    if op == 'forward':
        h += n
    elif op == 'down':
        d += n
    elif op == 'up':
        d -= n
assert h * d == 2187380
print(h * d)

aim = 0
h = 0
d = 0
for (op, n) in commands:
    if op == 'forward':
        h += n
        d += aim * n
    elif op == 'down':
        aim += n
    elif op == 'up':
        aim -= n
assert h * d == 2086357770
print(h * d)
