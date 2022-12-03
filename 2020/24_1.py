import pathlib

file_name = "24.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    tiles = [tile.strip() for tile in file.readlines()]

dirs = {
    "e": (2, 0),
    "w": (-2, 0),
    "ne": (1, 1),
    "nw": (-1, 1),
    "se": (1, -1),
    "sw": (-1, -1),
}

faces = []
unique_list = []

for line in tiles:
    current_location = [0,0]
    # print(line)
    while len(line) >= 1:
        
        if line[0] in ["e","w"]:
            # print(f"{line[0]} => 1")
            instruction = line[0]
            line = line[1:]
        else:
            # print(f"{line[0:2]} => 2")
            instruction = line[0:2]
            line = line[2:]
        current_location[0] += dirs[instruction][0]
        current_location[1] += dirs[instruction][1]

    faces.append(current_location)

    if current_location not in unique_list:
        unique_list.append(current_location)


# count numbers
black = 0
for unique in unique_list:
    if faces.count(unique) % 2 != 0:
        black +=1
    print(f"{unique}: {faces.count(unique)}")
print(f"Black: {black}")

