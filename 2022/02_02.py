from data_read import read_file

rps = read_file("02.txt")

rps = [r.strip().split() for r in rps]

total_score = 0

# (1 for Rock - A, X, 2 for Paper - B, Y, and 3 for Scissors - C, Z)
# X = lose, Y = draw, and Z = win.

for round in rps:
    if round[0] == "A":
        # rock
        if round[1] == "X":
            score = 3 + 0
        elif round[1] == "Y":
            score = 1 + 3
        elif round[1] == "Z":
            score = 2 + 6
    elif round[0] == "B":
        # paper
        if round[1] == "X":
            score = 1 + 0 
        elif round[1] == "Y":
            score = 2 + 3
        elif round[1] == "Z":
            score = 3 + 6
    elif round[0] == "C":
        # scissors
        if round[1] == "X":
            score = 2 + 0 
        elif round[1] == "Y":
            score = 3 + 3
        elif round[1] == "Z":
            score = 1 + 6

    total_score += score

print(f"{total_score=}")