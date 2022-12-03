from data_read import read_file

navigation = read_file("10.txt")

navigation = [nav.strip() for nav in navigation]


def solve(s):
    stack = []
    brackets = {'}': '{',')': '(',']': '[', '>': '<'}
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for c in s:
        if c in '}])>':
            if not stack or stack[-1] != brackets[c]:
                return scores[c]
            stack.pop()
        else:
            stack.append(c)
    return 0

scores = [solve(nav) for nav in navigation]

print(f"Total Score: {sum(scores)}")