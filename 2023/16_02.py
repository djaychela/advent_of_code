from data_read import read_file
from collections import defaultdict

mirror_grid_raw = read_file("16.txt")

mirror_grid = []
loc = [0,0]

directions = ((0,1), (1,0), (0,-1), (-1,0))

height = len(mirror_grid_raw)
width = len(mirror_grid_raw[0].strip())

for line in mirror_grid_raw:
    current_line = [c for c in line.strip()]
    mirror_grid.append(current_line)

def display_grid(grid, locations):
    # print(f"{locations=}")
    print("")
    for ydx,line in enumerate(grid):
        current_line = []
        for xdx, char in enumerate(line):
            if (ydx, xdx) in locations.keys():
                current_line.append("#")
            else:
                current_line.append(char)
        current_line.append(" : ")
        current_line += line
        print("".join(current_line))

def follow_beam(switched_on, cur_loc, direction):
    while (height > cur_loc[0] >= 0) and (width > cur_loc[1] >= 0) and direction not in switched_on[cur_loc]:
        switched_on[cur_loc].append(direction)
        cur_grid_cell = mirror_grid[cur_loc[0]][cur_loc[1]]
        # print(f"{cur_loc=}: {cur_grid_cell=}")
        if cur_grid_cell == "\\":
            # mirror \
            mirror = { 0:1, 1:0, 2:3, 3:2 }
            direction = mirror[direction]
        elif cur_grid_cell == "/":
            # mirror /
            mirror = { 0:3, 3:0, 2:1, 1:2 }
            direction = mirror[direction]
        elif cur_grid_cell == "|" and direction in [0, 2]:
            # print("Splitting|... - dir 1")
            follow_beam(switched_on, (cur_loc[0] + 1, cur_loc[1]), 1)
            # print("Splitting|... - dir 3")
            # follow_beam(switched_on, (cur_loc[0] - 1, cur_loc[1]), 3)
            direction = 3
        elif cur_grid_cell == "-" and direction in [1, 3]:
            # print(f"Splitting-... - dir 0 - {cur_loc[0], cur_loc[1] + 1}")
            follow_beam(switched_on, (cur_loc[0], cur_loc[1] + 1), 0)
            # print(f"Splitting-... - dir 2 - {cur_loc[0], cur_loc[1] - 1}")
            # follow_beam(switched_on, (cur_loc[0], cur_loc[1] - 1), 2)
            direction = 2
        cur_loc = (cur_loc[0] + directions[direction][0], cur_loc[1] + directions[direction][1])
    # display_grid(mirror_grid, switched_on)
    return len(switched_on)

max_score = 0
for idx in range(width):
    switched_on = defaultdict(list)
    max_score = max(max_score, follow_beam(switched_on, (0,idx), 1))
for idx in range(width):
    switched_on = defaultdict(list)
    max_score = max(max_score, follow_beam(switched_on, (height ,idx), 3))

for idx in range(height):
    switched_on = defaultdict(list)
    max_score = max(max_score, follow_beam(switched_on, (idx,0), 0))
for idx in range(height):
    switched_on = defaultdict(list)
    max_score = max(max_score, follow_beam(switched_on, (idx,width), 2))
    
print(max_score)


