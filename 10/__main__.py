import fileinput as fi


def score(line):
    opening = {')': '(', ']': '[', '}': '{', '>': '<'}
    penalty = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []
    for c in line:
        if c in '([{<':
            if not stack or stack[-1][0] != 'c':
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
        else:
            if not stack or stack[-1][0] != opening[c]:
                return ('corrupted', penalty[c])
            else:
                if stack[-1][1] == 1:
                    del stack[len(stack)-1]
                else:
                    stack[-1][1] -= 1
    r = 0
    for c, n in stack[::-1]:
        for _ in range(n):
            r = 5 * r + '([{<'.index(c) + 1
    return ('incomplete', r)


scores = [score(line.rstrip()) for line in fi.input()]
print(sum(s for status, s in scores if status == 'corrupted'))

incomplete = sorted(s for status, s in scores if status == 'incomplete')
print(incomplete[len(incomplete)//2])
