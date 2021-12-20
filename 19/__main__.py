import numpy as np
import fileinput as fi
import itertools as it
from collections import Counter

scanners = []
for line in fi.input():
    if line.startswith("---"):
        scanner = []
    elif not line.rstrip():
        scanners.append(np.array(scanner))
    else:
        scanner.append([int(x) for x in line.rstrip().split(",")])
scanners.append(np.array(scanner))


def findpos(truth, scanner):
    axes = np.concatenate([np.eye(3, dtype=np.int_), -np.eye(3, dtype=np.int_)])
    for x in axes:
        for y in axes:
            if np.dot(x, y) != 0:
                continue
            rot = np.vstack([x, y, np.cross(x, y)])
            beacons_rel = scanner @ rot
            offsets = Counter(tuple(a - b) for a in truth for b in beacons_rel)
            offset, n = offsets.most_common(1)[0]
            if n >= 12:
                return (rot, offset)


truth = set(tuple(beacon) for beacon in scanners[0])
scanners = scanners[1:]

offsets = [(0, 0, 0)]
while scanners:
    print(len(scanners))
    scanner = scanners.pop(0)
    if rot_off := findpos(truth, scanner):
        rot, offset = rot_off
        offsets.append(offset)
        for beacon in scanner @ rot + offset:
            truth.add(tuple(beacon))
    else:
        scanners.append(scanner)


print(len(truth))
print(max(sum(abs(aa - bb) for aa, bb in zip(a, b)) for a in offsets for b in offsets))
