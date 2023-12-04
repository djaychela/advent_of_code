from data_read import read_file

cubes = read_file("02.txt")

limits = {"red": 12, "green": 13, "blue": 14}
total = 0

for idx, cube in enumerate(cubes, start=1):
    games = cube.split(";")
    totals = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        game = game.strip()
        if ":" in game:
            game = game.split(":")[1].strip()
        # check game
        for colour in game.split(","):
            score, colour = colour.strip().split(" ")
            if totals[colour] < int(score):
                totals[colour] = int(score)
    power = totals["red"] * totals["green"] * totals["blue"]
    print(f"{idx=}, {power=}")
    total += power
print(total)