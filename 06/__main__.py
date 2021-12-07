import fileinput as fi

ls = [int(x) for x in next(fi.input()).split(',')]


def step(ls):
    ls = ls + [0] * (9 - len(ls))
    ls[7] += ls[0]
    return ls[1:] + ls[:1]


counter = [0] * 9
for x in ls:
    counter[x] += 1

for i in range(256):
    if i == 80:
        print(sum(counter))
    counter = step(counter)

print(sum(counter))
