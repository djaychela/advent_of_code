from data_read import read_file

navigation = read_file("10.txt")

navigation = [nav.strip() for nav in navigation]


def solve(s):
    stack = []
    brackets = {'}': '{',')': '(',']': '[', '>': '<'}
    brackets_rev = {v:k for k,v in brackets.items()}
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    for c in s:
        if c in '}])>':
            if not stack or stack[-1] != brackets[c]:
                return None
            stack.pop()
        else:
            stack.append(c)
    stack_rev = [brackets_rev[st] for st in stack[::-1]]
    score = 0
    for st in stack_rev:
        score *= 5
        score += scores[st]
    return score

scores = sorted([solve(nav) for nav in navigation if solve(nav)])
print(f"Middle Score: {scores[int((len(scores) -1) / 2)]}")
