import fileinput as fi


def score(line):
    opening = {')': '(', ']': '[', '}': '{', '>': '<'}
    penalty = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        elif not stack or stack.pop() != opening[c]:
            return ('corrupted', penalty[c])
    r = 0
    for c in stack[::-1]:
        r = 5 * r + '([{<'.index(c) + 1
    return ('incomplete', r)


scores = [score(line.rstrip()) for line in fi.input()]
print(sum(s for status, s in scores if status == 'corrupted'))

incomplete = sorted(s for status, s in scores if status == 'incomplete')
print(incomplete[len(incomplete)//2])
