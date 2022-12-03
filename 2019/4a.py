puzzle_input = "246540-787419"

start, finish = map(int, puzzle_input.split('-'))

total = 0
for j in range(start, finish + 1):
    ok = True
    double = False
    # check increasing
    digits = list(str(j))
    for i in range(len(digits)-1):
        if digits[i] > digits [i+1]:
            ok = False
            break
    # check double
    for i in range(len(digits)-1):
        if digits[i] == digits[i+1]:
            double = True
    if ok and double:
        print(j)
        total += 1

print(total)
