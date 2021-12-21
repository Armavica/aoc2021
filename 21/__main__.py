import numpy as np
from functools import cache


def part1(positions, diemax=100, target=1000):
    scores = [0, 0]
    die = 0
    while all(score < target for score in scores):
        roll = 0
        for _ in range(3):
            roll += die % diemax + 1
            die += 1
        positions[1 - die % 2] = (positions[1 - die % 2] + roll - 1) % 10 + 1
        scores[1 - die % 2] += positions[1 - die % 2]
    return min(scores) * die


@cache
def part2(pos, targets=(21, 21)):
    if targets[1] <= 0:
        return (0, 1)
    total = [0, 0]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                roll = a + b + c + 3
                p = ((pos[0] + roll - 1) % 10) + 1
                p1, p2 = part2((pos[1], p), targets=(targets[1], targets[0] - p))
                total[0] += p2
                total[1] += p1
    return total


pos = (7, 3)

print(part1(list(pos)))

print(max(part2(pos)))
