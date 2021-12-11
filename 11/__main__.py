import numpy as np
import fileinput as fi

def step(ls):
    ls += 1
    flashes = ls > 9
    while np.any(ls > 9):
        new_flashes = ls > 9
        ls[:-1, :-1] += new_flashes[1:, 1:]
        ls[:-1, :] += new_flashes[1:, :]
        ls[:-1, 1:] += new_flashes[1:, :-1]
        ls[:, :-1] += new_flashes[:, 1:]
        ls[:, 1:] += new_flashes[:, :-1]
        ls[1:, :-1] += new_flashes[:-1, 1:]
        ls[1:, :] += new_flashes[:-1, :]
        ls[1:, 1:] += new_flashes[:-1, :-1]
        flashes |= new_flashes
        ls[flashes] = 0


ls0 = np.array([[int(x) for x in line.rstrip()] for line in fi.input()])

ls = np.array(ls0)
nbflashes = 0
for _ in range(100):
    step(ls)
    nbflashes += np.sum(ls == 0)
print(nbflashes)

ls = np.array(ls0)
nb = 0
while len(set(ls.flatten())) > 1:
    step(ls)
    nb += 1
print(nb)
