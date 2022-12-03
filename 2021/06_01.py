from data_read import read_file

lanternfish = read_file("06_test_2.txt")

lanternfish = [int(fish) for fish in lanternfish[0].strip().split(",")]

print(lanternfish)

day = 0

while day < 18:
    initial_length = len(lanternfish)
    for idx in range(initial_length):
        lanternfish[idx] -= 1
        if lanternfish[idx] == -1:
            lanternfish[idx] = 6
            lanternfish.append(8)
            added = True
    day += 1
    print(f"After {day:02} days: {len(lanternfish)} fish. - {lanternfish}")

print(f"Number of fish: {len(lanternfish)}")
