from aoc2021 import lines
from collections import defaultdict

xys = []
for line in lines():
    xy1, xy2 = line.rstrip().split(' -> ')
    xys.append([int(x) for x in xy1.split(',') + xy2.split(',')])

points = defaultdict(int)
for x1, y1, x2, y2 in xys:
    if x1 == x2:
        for i in range(abs(y1 - y2) + 1):
            points[x1, min(y1, y2) + i] += 1
    elif y1 == y2:
        for i in range(abs(x1 - x2) + 1):
            points[min(x1, x2) + i, y1] += 1
    elif abs(x1 - x2) == abs(y1 - y2):
        for i in range(abs(x1 - x2) + 1):
            dx = [-1, 1][int(x1 < x2)]
            dy = [-1, 1][int(y1 < y2)]
            points[x1 + dx * i, y1 + dy * i] += 1

n = sum(v > 1 for v in points.values())
print(n)

