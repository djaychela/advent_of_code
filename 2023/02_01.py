from data_read import read_file

cubes = read_file("02.txt")

limits = {"red": 12, "green": 13, "blue": 14}
total = 0

for idx, cube in enumerate(cubes, start=1):
    games = cube.split(";")
    game_ok = True
    for game in games:
        game = game.strip()
        if ":" in game:
            game = game.split(":")[1].strip()
        # check game
        for colour in game.split(","):
            score, colour = colour.strip().split(" ")
            # print(f"{score=}, {colour=}")
            if limits[colour] < int(score):
                print(f"{idx=}: {score=}, {colour=} - over!")
                game_ok = False
        # split on ","
        # identify colour
        # count
    if game_ok:
        total += idx
        print(f"adding {idx}")
print(total)