import fileinput as fi
from collections import defaultdict

graph = defaultdict(list)

for line in fi.input():
    a, b = line.rstrip().split('-')
    graph[a].append(b)
    graph[b].append(a)

def parta(pos, visited):
    if pos == 'end':
        return 1
    s = 0
    for x in graph[pos]:
        if x.isupper() or x not in visited:
            s += parta(x, visited + [x])
    return s

def partb(pos, visited, twice):
    if pos == 'end':
        return 1
    s = 0
    for x in graph[pos]:
        if x.isupper() or x not in visited:
            s += partb(x, visited + [x], twice)
        elif x in visited and not twice and x != 'start':
            s += partb(x, visited, True)
    return s

print(parta('start', ['start']))
print(partb('start', ['start'], False))

