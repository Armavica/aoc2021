import fileinput as fi

def fold(points, instruction):
    z = int(instruction[13:])
    if instruction[11] == 'x':
        return set((z - abs(x - z), y) for x, y in points)
    elif instruction[11] == 'y':
        return set((x, z - abs(y - z)) for x, y in points)


inpt = fi.input()

points = []
for line in inpt:
    l = line.rstrip()
    if not l:
        break
    x, y = [int(x) for x in l.split(',')]
    points.append((x, y))


for iline, line in enumerate(inpt):
    points = fold(points, line)
    if iline == 0:
        print(len(points))


xs = [x for x, _ in points]
ys = [y for _, y in points]
for y in range(min(ys), max(ys) + 1):
    for x in range(min(xs), max(xs) + 1):
        print(' #'[int((x, y) in points)], end='')
    print()
