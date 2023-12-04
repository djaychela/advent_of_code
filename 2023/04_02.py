from data_read import read_file
from collections import defaultdict

cards = read_file("04.txt")

total_score = 0

winning_dict = defaultdict(int)

for game, line in enumerate(cards, 1):
    lines_won = 0
    winning, mine = line.split("|")
    winning = list(set(winning.split(":")[1].strip().split(" ")))
    winning = [x for x in winning if x !=""]
    mine = list(set(mine.strip().split(" ")))
    mine = [x for x in mine if x!=""]
    
    for number in mine:
        if number in winning:
            if lines_won == 0:
                lines_won = 1
            else:
                lines_won +=1
    if lines_won != 0:    
        print(f"Win on game {game}")
    winning_dict[game] += 1

    for idx in range(game + 1, game + lines_won + 1):
        for repeat in range(1, winning_dict[game] + 1):
            # print(f"adding game {idx}")
            winning_dict[idx] += 1

print(winning_dict)
print(sum(winning_dict.values()))
