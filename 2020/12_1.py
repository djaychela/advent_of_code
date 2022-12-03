import pathlib

file_name = "12.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    directions = [direction.strip() for direction in file.readlines()]

card = ["W", "N", "E", "S"]
dirs = [[1,0], [0,1], [-1, 0], [0, -1]]
dir_index = 2
position = [0, 0]
for direction in directions:
    command = direction[0]
    length = int(direction[1:])
    if command == "F":
        for i in range(length):
            position[0] += dirs[dir_index][0]
            position[1] += dirs[dir_index][1]
    if command in card:
        move = dirs[card.index(command)]
        for i in range(length):
            position[0] += move[0]
            position[1] += move[1]
    if command in ["R", "L"]:
        index_change = length // 90
        if command == "R":
            dir_index += index_change
        else:
            dir_index -= index_change
        dir_index %= 4
    print(position)

print(abs(position[0]) + abs(position[1]))
