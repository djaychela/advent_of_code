from data_read import read_file

cards = read_file("04.txt")

total_score = 0

for line in cards:
    score = 0
    winning, mine = line.split("|")
    winning = list(set(winning.split(":")[1].strip().split(" ")))
    winning = [x for x in winning if x !=""]
    mine = list(set(mine.strip().split(" ")))
    mine = [x for x in mine if x!=""]
    print(f"{winning=} : {mine=}")
    for number in mine:
        if number in winning:
            if score == 0:
                score = 1
            else:
                score *=2
        continue
    total_score += score
print(total_score)

#24499 too high
#1140 too low