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

def check_position(new_position, dir):
    # [0-49][150] -> [149,100], [99] right > left
    # [50][100-149] -> [50-99], [99] down > left
    # [-1][100-149] -> 199 [0-49], up = up
    # range,                swap,   offset, invert, alt_co, othercoord, dir_change
    # [[0, 49],[150, 150],  False,  100,    True,   0,      99,     2] B>E
    # [[50, 50],[100, 149], True,   -50,    False,  0,      99,     1] B>C
    # [[-1,-1], [100, 149], False,  -100,   False,  1,      199,    0] B>F
    # C>B
    # C>D
    # D>C
    # D>A
    # E>B
    # E>F
    # F>A
    # F>B
    # F>E
    check_names = ["B>E", "B>C", "B>F", "C>B", "C>D", "D>C", "D>A", "E>B", "E>F", "F>A", "F>B","F>E"]
    checks = [[0, 49, 150, 150], [50,50, 100, 149], [-1,-1, 100, 149]]
    actions = [[False, 100, True, 0, 99, 2], [True, -50, False, 0, 99, 1], [False, -100, False, 1, 199, 0]]
    for idx, check in enumerate(checks):
        if new_position[0] in range(check[0], check[1] + 1):
            if new_position[1] in range(check[2], check[3] + 1):
                print(f"match found - check {check}")
                if actions[idx][0]:
                    # swap coords
                    new_position = [new_position[1], new_position[0]]
                # invert
                if actions[idx][2]:
                    while new_position[actions[idx][3]] > 50:
                        new_position[actions[idx][3]] -= 50
                    new_position[actions[idx][3]] = 49 - new_position[actions[idx][3]]
                # add offset
                new_position[actions[idx][3]] += actions[idx][1]
                # alter other coord
                new_position[int(not actions[idx][3])] = actions[idx][4]
                # change direction
                dir += actions[idx][5]
                dir = dir % 4

    return new_position, dir

for c in [[0, 150], [49, 150], [-1, 100], [50, 149]]:
    print(c)
    print(check_position(c, dir))

exit()

for instruction in instructions:
    if isinstance(instruction, int):
        for _ in range(instruction):
            new_position = [position[0] + dirs[dir][0], position[1] + dirs[dir][1]]
            new_position = check_position(new_position)
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