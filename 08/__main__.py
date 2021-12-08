import fileinput as fi
import itertools as it


def solve_manual(inpt):
    """
    Requires actually thinking about the problem (ughh).
    """
    one = [b for b in inpt if len(b) == 2][0]
    four = [b for b in inpt if len(b) == 4][0]
    seven = [b for b in inpt if len(b) == 3][0]
    eight = [b for b in inpt if len(b) == 7][0]
    nine = [b for b in inpt if len(b) == 6 and set(four) < set(b)][0]
    six = [b for b in inpt if len(b) == 6 and not set(one) < set(b)][0]
    zero = [b for b in inpt if len(b) == 6 and b not in [nine, six]][0]
    three = [b for b in inpt if len(b) == 5 and set(one) < set(b)][0]
    two = [b for b in inpt if len(b) == 5 and len(set(b)&set(four)) == 2][0]
    five = [b for b in inpt if len(b) == 5 and b not in [two, three]][0]
    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    assert set(numbers) == set(inpt)
    return numbers


def solve_fastest(inpt):
    """
    Same as manual solution, but optimized code (only loops twice through the input).
    """
    for b in inpt:
        if len(b) == 2:
            one = b
        elif len(b) == 3:
            seven = b
        elif len(b) == 4:
            four = b
        elif len(b) == 7:
            eight = b
    for b in inpt:
        if len(b) == 6:
            if set(four) < set(b):
                nine = b
            elif not set(one) < set(b):
                six = b
            else:
                zero = b
        elif len(b) == 5:
            if set(one) < set(b):
                three = b
            elif len(set(b) & set(four)) == 2:
                two = b
            else:
                five = b
    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    assert set(numbers) == set(inpt)
    return numbers


def solve_hybrid(inpt):
    """
    Only requires thinking about part 1.
    Makes 8 tries.
    """
    one = [b for b in inpt if len(b) == 2][0]
    four = [b for b in inpt if len(b) == 4][0]
    seven = [b for b in inpt if len(b) == 3][0]
    eight = [b for b in inpt if len(b) == 7][0]
    a = list(set(seven) - set(one))[0]
    n = 0
    for c, f in it.permutations(one):
        for b, d in it.permutations(set(four) - set(one)):
            for e, g in it.permutations(set(eight) - set([a, b, c, d, f])):
                numbers = [
                        [a, b, c, e, f, g], [c, f], [a, c, d, e, g], [a, c, d, f, g], [b, c, d, f],
                        [a, b, d, f, g], [a, b, d, e, f, g], [a, c, f], [a, b, c, d, e, f, g], [a, b, c, d, f, g]
                        ]
                numbers = [''.join(sorted(x)) for x in numbers]
                if set(numbers) == set(inpt):
                    return numbers


def solve_bruteforce(inpt):
    """
    Doesn't require thinking at all.
    Makes 5040 tries.
    """
    for a, b, c, d, e, f, g in it.permutations('abcdefg'):
        numbers = [
                [a, b, c, e, f, g], [c, f], [a, c, d, e, g], [a, c, d, f, g], [b, c, d, f],
                [a, b, d, f, g], [a, b, d, e, f, g], [a, c, f], [a, b, c, d, e, f, g], [a, b, c, d, f, g]
                ]
        numbers = [''.join(sorted(x)) for x in numbers]
        if set(numbers) == set(inpt):
            return numbers


s1 = 0
s2 = 0
for line in fi.input():
    inpt, outpt = [[''.join(sorted(n)) for n in x.split()] for x in line.split(' | ')]
    s1 += sum(len(a) in [2, 4, 3, 7] for a in outpt)
    numbers = solve_manual(inpt)
    #assert numbers == solve_fastest(inpt)
    #assert numbers == solve_hybrid(inpt)
    #assert numbers == solve_bruteforce(inpt)
    n = 0
    for a in outpt:
        n = 10 * n + numbers.index(a)
    s2 += n


assert s1 == 264
print(s1)
assert s2 == 1063760
print(s2)
