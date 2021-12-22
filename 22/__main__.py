import fileinput as fi
import itertools as it
from math import prod


def included(boxa, boxb):
    "Returns whether boxb is included in boxa"
    return all(da[0] <= db[0] and db[1] <= da[1] for da, db in zip(boxa, boxb))


def intersect(boxa, boxb):
    "Returns whether the intersection of boxa and boxb is non-zero"
    return all(da[1] >= db[0] and da[0] <= db[1] for da, db in zip(boxa, boxb))


class Tree:
    def __init__(self, box, activated=False):
        self.nodes = []
        self.coords = box
        self.state = activated

    def split(self, box):
        assert not self.nodes
        ranges = []
        for boxd, coordsd in zip(box, self.coords):
            if coordsd[0] < boxd[0] <= coordsd[1]:
                ranges.append([(coordsd[0], boxd[0] - 1), (boxd[0], coordsd[1])])
            elif coordsd[0] <= boxd[1] < coordsd[1]:
                ranges.append([(coordsd[0], boxd[1]), (boxd[1] + 1, coordsd[1])])
            else:
                ranges.append([coordsd])
        self.nodes = [Tree(b, activated=self.state) for b in it.product(*ranges)]

    def addbox(self, box, activate):
        if not intersect(box, self.coords):
            return
        if included(box, self.coords):
            self.nodes = []
            self.state = activate
            return
        if not self.nodes:
            self.split(box)
        for tree in self.nodes:
            tree.addbox(box, activate)

    def count(self):
        if self.state and not self.nodes:
            dims = [dim[1] - dim[0] + 1 for dim in self.coords]
            return prod(dims)
        return sum(tree.count() for tree in self.nodes)


l = 1000000
smalltree = Tree(((-50, 50),) * 3)
largetree = Tree(((-l, l),) * 3)
for line in fi.input():
    onoff, xx, yy, zz = line.rstrip().split("=")
    onoff = onoff.split()[0]
    xrange = [int(x) for x in xx[:-2].split("..")]
    yrange = [int(x) for x in yy[:-2].split("..")]
    zrange = [int(x) for x in zz.split("..")]
    smalltree.addbox((xrange, yrange, zrange), onoff == "on")
    largetree.addbox((xrange, yrange, zrange), onoff == "on")
print(smalltree.count())
print(largetree.count())
