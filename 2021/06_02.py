from collections import Counter

from data_read import read_file

lanternfish = read_file("06.txt")

lanternfish = [int(fish) for fish in lanternfish[0].strip().split(",")]

counts = Counter(lanternfish)

days = 256

for day in range(days):
    previous = counts.copy()
    for idx in range(10):
        if idx != 6 and idx != 8:
            counts[idx] = previous[idx + 1]
        elif idx == 6:
            counts[idx] = previous[0] + previous[7]
        elif idx == 8:
            counts[idx] = previous[0]

    print(f"Day {day + 1} - Total: {sum(counts.values())}")





