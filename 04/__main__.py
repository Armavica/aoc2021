import numpy as np
import fileinput as fi


def score(grid, numbers):
    """
    Returns the score of the grid if it is won, None otherwise.
    """
    unmarked = np.array([[x not in numbers for x in line] for line in grid])
    if 0 in unmarked.sum(axis=0) or 0 in unmarked.sum(axis=1):
        return numbers[-1] * grid[unmarked].sum()


def first(grids, numbers):
    for n in range(len(numbers)):
        for grid in grids:
            if s := score(grid, numbers[:n]):
                return s


def last(grids, numbers):
    for n in range(len(numbers)):
        if all(score(grid, numbers[:n]) is not None for grid in grids):
            for grid in grids:
                if score(grid, numbers[:n-1]) is None:
                    return score(grid, numbers[:n])


lines = fi.input()

numbers = [int(x) for x in next(lines).split(',')]

grids = []
while True:
    try:
        # empty line
        next(lines)
    except StopIteration:
        break
    grids.append(np.array([[int(x) for x in next(lines).split()] for _ in range(5)]))

print(first(grids, numbers))
print(last(grids, numbers))
