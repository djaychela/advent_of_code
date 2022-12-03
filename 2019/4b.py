import re

puzzle_input = "246540-787419"

start, finish = map(int, puzzle_input.split("-"))

total = 0
for j in range(start, finish + 1):
    ok = True
    double = False
    triple = False

    # check increasing
    digits = list(str(j))
    digit_string = str(j)
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            ok = False
            break

    # check double (and not triple)
    present = set(digits)
    for p in present:
        match_2 = f"{p}{p}"
        match_3 = f"{p}{p}{p}"
        if re.search(match_2, digit_string):
            if not re.search(match_3, digit_string):
                double = True

    if ok and double:
        total += 1

print(total)
