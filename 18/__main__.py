import fileinput as fi
import functools as ft


def add(a, b):
    "Adds two pairs"
    return [a, b]


def findexplode(p, path):
    "Returns the location of the exploding pair if it exists"
    if isinstance(p, int):
        return None
    if len(path) == 4 and all(isinstance(x, int) for x in p):
        return path
    for i, x in enumerate(p):
        if pp := findexplode(x, path + [i]):
            return pp


def addleftmost(p, x):
    "Adds x to the leftmost simple number of p"
    if isinstance(p, int):
        return p + x
    return [addleftmost(p[0], x), p[1]]


def addrightmost(p, x):
    "Adds x to the rightmost simple number of p"
    if isinstance(p, int):
        return p + x
    return [p[0], addrightmost(p[1], x)]


def explode(p, path, lv, rv):
    "Explodes the pair (lv, rv) at the given location in p"
    if not path:
        return 0
    if path[0] == 1:
        return [
            p[0] if 1 in path[1:] else addrightmost(p[0], lv),
            explode(p[1], path[1:], lv, rv),
        ]
    if path[0] == 0:
        return [
            explode(p[0], path[1:], lv, rv),
            p[1] if 0 in path[1:] else addleftmost(p[1], rv),
        ]


def split(p):
    "Splits a pair if possible and returns the number and whether something split or not"
    if isinstance(p, int):
        if p >= 10:
            return ([p // 2, p - (p // 2)], True)
        return (p, False)
    a, b = p
    splita, didsplit = split(a)
    if didsplit:
        return ([splita, b], True)
    splitb, didsplit = split(b)
    return ([a, splitb], didsplit)


def reduce(p):
    "Reduces a number completely"
    while True:
        if path := findexplode(p, []):
            pair = p
            for x in path:
                pair = pair[x]
            p = explode(p, path, pair[0], pair[1])
            continue
        p, didsplit = split(p)
        if not didsplit:
            return p


def magnitude(p):
    "Computes the magnitude of a number"
    if isinstance(p, int):
        return p
    return 3 * magnitude(p[0]) + 2 * magnitude(p[1])


pairs = [eval(line) for line in fi.input()]
print(magnitude(ft.reduce(lambda a, b: reduce(add(a, b)), pairs)))
print(max(magnitude(reduce(add(a, b))) for a in pairs for b in pairs if a != b))
