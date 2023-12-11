from data_read import read_file

map_raw = read_file("10.txt")

map_data = []

for line in map_raw:
    map_line = [c for c in line.strip()]
    map_data.append(map_line)

def find_start(map_data):
    for idx, line in enumerate(map_data):
        if "S" in line:
            return (idx, line.index("S"))
        
start_location = find_start(map_data)

# directions: N=0, E=1, S=2, W=3
direction_mappings = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

# mappings: new direction
pipe_mappings = {
    "-": {1: 1, 3: 3},
    "|": {0: 0, 2: 2},
    "L": {2: 1, 3: 0},
    "J": {1: 0, 2: 3},
    "7": {0: 3, 1: 2},
    "F": {0: 1, 3: 2}
}

running = True
cur_loc = [*start_location]
print(f"Start: {cur_loc=}")
# set to 0 for real data
cur_dir = 0
distance = 0

while running:
    print("****")
    print(f"{cur_dir=}")
    cur_loc[0] += direction_mappings[cur_dir][0]
    cur_loc[1] += direction_mappings[cur_dir][1]
    distance += 1
    print(f"{distance=}")
    print(f"{cur_loc=}")
    cur_loc_symbol = map_data[cur_loc[0]][cur_loc[1]]
    if cur_loc_symbol == "S":
        # back at start
        break
    print(f"{cur_loc_symbol=}")
    cur_loc_data = pipe_mappings[cur_loc_symbol]
    print(f"{cur_loc_data=}")
    new_dir = cur_loc_data[cur_dir]
    print(f"{new_dir=}")
    cur_dir = new_dir
    if cur_loc == start_location:
        running = False

print(distance)
print(distance / 2)