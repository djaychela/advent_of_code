from data_read import read_file
from pprint import pprint

import sys
sys.setrecursionlimit(5000)

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

loop_locations = []

while running:

    cur_loc[0] += direction_mappings[cur_dir][0]
    cur_loc[1] += direction_mappings[cur_dir][1]
    distance += 1
    loop_locations.append((cur_loc[0], cur_loc[1]))
    cur_loc_symbol = map_data[cur_loc[0]][cur_loc[1]]
    if cur_loc_symbol == "S":
        # back at start
        break
    cur_loc_data = pipe_mappings[cur_loc_symbol]
    new_dir = cur_loc_data[cur_dir]
    cur_dir = new_dir
    if cur_loc == start_location:
        running = False

score = 0

def count_to_left(y, x, map_data):
    wanted = ["|", "J", "L"]
    local_score = 0
    for xdx in range(x, -1, -1):
        cell_to_check = new_map_data[y+1][xdx]
        if y == 5 or y == 6 or y == 4:
             print(f"{cell_to_check=}")
        if cell_to_check in wanted:
            local_score +=1
    print(f"{y=},{x=},{local_score=}")
    return local_score % 2

# create empty new map with loop on it, larger to allow fill from edges

new_map_data = [[" " for _ in range(len(map_data[0]) + 2)]]

for ydx in range(len(map_data)):
    current_line = [" "]
    for xdx in range(len(map_data[0])):
        if (ydx, xdx) in loop_locations:
            current_line.append(map_data[ydx][xdx])
        else:
            current_line.append(" ")
    current_line.append(" ")
    new_map_data.append(current_line)

# replace start with actual pipe (offset due to new map) - found by visual inspection of my test data
new_map_data[start_location[0]+1][start_location[1]+1] = "J"

# flood fill outside loop

def flood_recursive(matrix):
	width = len(matrix)
	height = len(matrix[0])
	def fill(x,y):
		if matrix[x][y] != " ":
			return
		elif matrix[x][y] == "+":
			return
		else:
			matrix[x][y] = "+"
			neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
			for n in neighbors:
				if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
					fill(n[0],n[1])
	start_x = 0
	start_y = 0
	
	fill(start_x,start_y)
	return matrix

new_map_data = flood_recursive(new_map_data)

for ydx in range(len(map_data)):
    for xdx in range(len(map_data[0])):
        if (ydx, xdx) not in loop_locations and new_map_data[ydx + 1][xdx + 1] != "+":
            current_score = count_to_left(ydx, xdx, map_data)
            if current_score:
                new_map_data[ydx + 1][xdx + 1] = "#"
                score += 1


for idx, line in enumerate(new_map_data, -1):
    print(idx, "".join(line))
print(score)

# 3236 - too high
# 403 - too low
# 513 - too high
# 511 - Correct!!!