import fileinput as fi

ls = [int(x) for x in next(fi.input()).split(',')]


def step(ls):
    new = ls[0]
    nls = ls[1:]
    nls += [0] * (9 - len(nls))
    nls[6] += new
    nls[8] += new
    return nls


counter = [0] * 9
for x in ls:
    counter[x] += 1

for i in range(256):
    if i == 80:
        print(sum(counter))
    counter = step(counter)

print(sum(counter))
