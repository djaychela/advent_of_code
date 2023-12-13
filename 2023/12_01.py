from data_read import read_file

springs_raw = read_file("12.txt")

def check_group(springs, groups):
    current = 0
    seen = []
    for c in springs:
        if c == ".":
            if current > 0:
                seen.append(current)
            current = 0
        elif c == "#":
            current += 1
    if current > 0:
       seen.append(current) 
    return seen == groups
    
def check_spring(springs, groups, i):
    if i == len(springs):
        return check_group(springs, groups)
    if springs[i] == "?":
        return (check_spring(springs[:i] + "#" + springs[i+1:], groups, i + 1) +
                check_spring(springs[:i] + "." + springs[i+1:], groups, i + 1))
    else:
        return check_spring(springs, groups, i+1)
    
answer = 0

for line in springs_raw:
    springs, groups = line.split()
    groups = map(int, groups.split(","))
    score = check_spring(springs, list(groups), 0)
    answer += score

print(answer)