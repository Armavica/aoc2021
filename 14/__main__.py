import fileinput as fi
from collections import Counter

inpt = fi.input()
pattern = next(inpt).rstrip()
next(inpt)
rules = dict(line.rstrip().split(' -> ') for line in inpt)

def step(s, rules):
    """
    Slow version, takes and returns a string.
    """
    return s[0] + ''.join(rules[a + b] + b for a, b in zip(s, s[1:]))

def stepfast(pairs, rules):
    """
    Fast version, takes and returns a counter of consecutive pairs.
    """
    c = Counter()
    for a, b in pairs:
        c[a + rules[a + b]] += pairs[a + b]
        c[rules[a + b] + b] += pairs[a + b]
    return c
        
def count(pairs):
    """
    Counts single element occurrences from a counter of consecutive pairs.
    """
    c = Counter()
    # Sum over the first element of each pair
    for k, v in pairs.items():
        c[k[0]] += v
    # And add the last element of the pattern, which is not the first in any pair
    c[pattern[-1]] += 1
    return c

pairs = Counter(a + b for a, b in zip(pattern, pattern[1:]))

for i in range(40):
    pairs = stepfast(pairs, rules)
    if i in [9, 39]:
        c = count(pairs)
        print(max(c.values()) - min(c.values()))
