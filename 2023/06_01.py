from data_read import read_file
from functools import reduce

races = read_file("06.txt")

t = map(int, [t for t in races[0].split(":")[1].strip().split(" ") if t !=""])
distance = map(int, [d for d in races[1].split(":")[1].strip().split(" ") if d !=""])

races = zip(t, distance)

wins = []

for t, d in races:
    winning_ways = 0
    for b in range(t + 1):
        covered = b * (t - b)
        if covered > d:
            winning_ways += 1
    print(f"{d=}, {winning_ways=}")
    wins.append(winning_ways)

total_score = reduce(lambda x, y: x * y, wins)

print(total_score)


    
