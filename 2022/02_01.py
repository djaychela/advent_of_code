from data_read import read_file

rps = read_file("02.txt")

rps = [r.strip().split() for r in rps]

total_score = 0

for round in rps:
    if round[0] == "A":
        if round[1] == "X":
            score = 3
        elif round[1] == "Y":
            score = 6
        elif round[1] == "Z":
            score = 0
    elif round[0] == "B":
        if round[1] == "X":
            score = 0
        elif round[1] == "Y":
            score = 3
        elif round[1] == "Z":
            score = 6
    elif round[0] == "C":
        if round[1] == "X":
            score = 6
        elif round[1] == "Y":
            score = 0
        elif round[1] == "Z":
            score = 3
    if round[1] == "X":
        score += 1
    elif round[1] == "Y":
        score += 2
    elif round[1] == "Z":
        score += 3

    total_score += score
        
    # print(round, score, total_score)

print(f"{total_score=}")