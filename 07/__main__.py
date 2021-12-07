import fileinput as fi

data = [int(x) for x in next(fi.input()).split(',')]

fuel = min(sum(abs(p-x) for x in data) for p in range(max(data)+1))
print(fuel)

fuel = min(sum((abs(p-x)*(abs(p-x)+1))//2 for x in data) for p in range(max(data)+1))
print(fuel)
