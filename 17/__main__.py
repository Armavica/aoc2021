import math

xmin, xmax = 94, 151
ymin, ymax = -156, -103


def maxy(vx, vy):
    """
    Returns the highest y value reached before entering the zone,
    or None if we never enter the zone.
    """
    maxy = 0
    x, y = 0, 0
    while y >= ymin:
        maxy = max(maxy, y)
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return maxy
        x, y = (x + vx, y + vy)
        vx -= vx / abs(vx) if vx != 0 else 0
        vy -= 1


def allspeeds(xmin, xmax, ymin, ymax):
    """
    Iterator over all initial speeds that lead to entering the zone,
    with the highest value of y reached before entering the zone.
    """
    vxmin = int(math.ceil(((1 + 8 * xmin) ** 0.5 - 1) / 2)) if xmin >= 0 else xmin
    vxmax = int(math.floor((1 - (1 - 8 * xmax) ** 0.5) / 2)) if xmax < 0 else xmax
    vymin = ymin
    vymax = max(ymin, -ymin - 1)
    print(f"{vxmin} <= vx <= {vxmax}")
    print(f"{vymin} <= vy <= {vymax}")
    for vx in range(vxmin, vxmax + 1):
        for vy in range(vymin, vymax + 1):
            if (ytop := maxy(vx, vy)) is not None:
                yield (vx, vy), ytop


valid = dict(allspeeds(xmin, xmax, ymin, ymax))

print(max(valid.values()))
print(len(valid))
