from data_read import read_file

import re
import string

map_raw = read_file("22.txt")

print(map_raw)

map_data = []
map_x_limits = []
map_max_cols = 0
map_max_rows = 0

for line in map_raw:
    if "." in line:
        map_max_cols = max(map_max_cols, len(line.strip("\n")))
        # map line
        start = -1
        end = 0
        current_line = []
        for idx, cell in enumerate(line):
            if cell == " ":
                start = idx
                current_line.append(cell)
            elif cell == "\n":
                end = idx
            else:
                current_line.append(cell)
        map_data.append(current_line)
        map_x_limits.append((start, end))
        map_max_rows += 1
        
            
    elif line == "\n":
        continue
    else:
        instructions = re.split(r"(R|L)",line.strip())



for row_dx in range(map_max_rows):
    for col_dx in range(map_max_cols):
        try:
            data = map_data[row_dx][col_dx]
        except IndexError:
            map_data[row_dx].append(" ")
            # print(f"added space at {row_dx}, {col_dx}")
# print(map_data)
# print(map_limits)
# print(instructions)

instructions = [int(instruction) if instruction[0] in string.digits else instruction for instruction in instructions]

position = [0, map_x_limits[0][0] + 1]
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dir = 0

def check_position(new_position):
    if new_position[1] >= map_max_cols:
        new_position[1] = 0
    if new_position[1] < 0:
        new_position[1] = map_max_cols - 1
    if new_position[0] >= map_max_rows:
        new_position[0] = 0
    elif new_position[0] < 0:
        new_position[0] = map_max_rows - 1
    return new_position

for instruction in instructions:
    if isinstance(instruction, int):
        for _ in range(instruction):
            new_position = [position[0] + dirs[dir][0], position[1] + dirs[dir][1]]
            new_position = check_position(new_position)
            if map_data[new_position[0]][new_position[1]] == " ":
                # gone off map, need to loop around in whatever direction
                # if it finds a block, then keep the original position
                while map_data[new_position[0]][new_position[1]] == " ":
                    new_position = [new_position[0] + dirs[dir][0], new_position[1] + dirs[dir][1]]
                    new_position = check_position(new_position)
                    print(f"teleport to {new_position}")
                    # exit()/
            if map_data[new_position[0]][new_position[1]] == ".":
                position[0] = new_position[0]
                position[1] = new_position[1]
                print(f"Moved forwards one space to {position}")
            else:
                print("Hit a wall!")
    else:
        if instruction == "R":
            dir +=1
        else:
            dir -=1
        dir = dir % 4
        print(f"{instruction}: dir now {dir}")

print(position[0] + 1, position[1] + 1,  dir)
print((position[0] + 1) *1000 + (position[1] + 1) * 4 +  dir)