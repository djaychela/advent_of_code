from data_read import read_file
from functools import reduce

races = read_file("06.txt")

t = int("".join([t for t in races[0].split(":")[1].strip().split(" ") if t !=""]))
d = int("".join([d for d in races[1].split(":")[1].strip().split(" ") if d !=""]))

wins = []

winning_ways = 0
for b in range(t + 1):
    covered = b * (t - b)
    if covered > d:
        winning_ways += 1
print(f"{d=}, {winning_ways=}")
wins.append(winning_ways)

total_score = reduce(lambda x, y: x * y, wins)

print(total_score)
