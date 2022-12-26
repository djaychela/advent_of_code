from data_read import read_file

import re
import string

map_raw = read_file("22.txt")


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
        instructions = re.split(r"(R|L)", line.strip())


for row_dx in range(map_max_rows):
    for col_dx in range(map_max_cols):
        try:
            data = map_data[row_dx][col_dx]
        except IndexError:
            map_data[row_dx].append(" ")
            

instructions = [
    int(instruction) if instruction[0] in string.digits else instruction
    for instruction in instructions
]

position = [0, map_x_limits[0][0] + 1]
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dir = 0


def check_position(new_position, dir):
    # [0-49][150] -> [149,100], [99] right > left
    # [50][100-149] -> [50-99], [99] down > left
    # [-1][100-149] -> 199 [0-49], up = up

    check_names = [
        "A>F",
        "A>D",
        "B>E",
        "B>C",
        "B>F",
        "C>B",
        "C>D",
        "D>C",
        "D>A",
        "E>B",
        "E>F",
        "F>A",
        "F>B",
        "F>E",
    ]
    checks = [
        [-1, -1, 50, 99, 3],  # A>F
        [0, 49, 49, 49, 2],  # A>D
        [0, 49, 150, 150, 0],  # B>E
        [50, 50, 100, 149, 1],  # B>C
        [-1, -1, 100, 149, 3],  # B>F
        [50, 99, 100, 100, 0],  # C>B
        [50, 99, 49, 49, 2],  # C>D
        [99, 99, 0, 49, 3],  # D>C
        [100, 149, -1, -1, 2],  # D>A
        [100, 149, 100, 100, 0],  # E>B
        [150, 150, 50, 99, 1],  # E>F
        [150, 199, -1, -1, 2],  # F>A
        [200, 200, 0, 49, 1],  # F>B
        [150, 199, 50, 50, 0],  # F>E
    ]
    # range,                swap,   offset, invert, alt_co, othercoord, dir_change
    # [[0, 49],[150, 150],  False,  100,    True,   0,      99,     2] B>E
    # [[50, 50],[100, 149], True,   -50,    False,  0,      99,     1] B>C
    # [[-1,-1], [100, 149], False,  -100,   False,  1,      199,    0] B>F
    actions = [
        [True,  100,    False,  0, 0, 0],  # A>F
        [False, 100,    True,   0, 0, 0],  # A>D
        [False, 100,    True,   0, 99, 2],  # B>E
        [True,  -50,    False,  0, 99, 2],  # B>C
        [False, -100,   False,  1, 199, 3],  # B>F
        [True,  50,     False,  1, 49, 3],  # C>B
        [True,  -50,    False,  1, 100, 1],  # C>D
        [True,  50,     False,  0, 50, 0],  # D>C
        [False, 0,      True,   0, 50, 0],  # D>A
        [False, 0,      True,   0, 149, 2],  # E>B
        [True,  100,    False,  0, 49, 2],  # E>F
        [True,  -100,   False,  1, 0, 1],  # F>A
        [False, 100,    False,  1, 0, 1],  # F>B
        [True,  -100,   False,  1, 149, 3],  # F>E
    ]
    for idx, check in enumerate(checks):
        if new_position[0] in range(check[0], check[1] + 1):
            if new_position[1] in range(check[2], check[3] + 1):
                if dir == check[4]:
                    print(f"{new_position} match found - check {check} - {check_names[idx]}")
                    if actions[idx][0]:
                        # swap coords
                        new_position = [new_position[1], new_position[0]]
                    # invert
                    if actions[idx][2]:
                        while new_position[actions[idx][3]] >= 50:
                            new_position[actions[idx][3]] -= 50
                        new_position[actions[idx][3]] = 49 - new_position[actions[idx][3]]
                    # add offset
                    new_position[actions[idx][3]] += actions[idx][1]
                    # alter other coord
                    new_position[int(not actions[idx][3])] = actions[idx][4]
                    # change direction
                    dir = actions[idx][5]
                    

    return new_position, dir


# for c, d in [[[-1, 50], 3],
#             [[-1,99], 3], # A>F
#             [[0, 49], 2], 
#             [[49,49], 2], # A>D
#             [[0, 150], 0],
#             [[49,150], 0], # B>E
#             [[50, 100], 1],
#             [[50, 149], 1], # B>C
#             [[-1, 100], 3],
#             [[-1, 149], 3], # B>F
#             [[50, 100], 0], 
#             [[99, 100], 0], # C>B
#             [[50, 49], 2],
#             [[99,49], 2], # C>D
#             [[99, 0], 3],
#             [[99, 49], 3], # D>C
#     ]:
#     print(c, d)
#     print(check_position(c, d))

# # exit()

for instruction in instructions:
    if isinstance(instruction, int):
        for steps in range(instruction):
            new_position = [position[0] + dirs[dir][0], position[1] + dirs[dir][1]]
            print(f"Checking {new_position}")
            new_position, new_dir = check_position(new_position, dir)
            print(f"{new_dir=} - {new_position=}")
            if map_data[new_position[0]][new_position[1]] == ".":
                position[0] = new_position[0]
                position[1] = new_position[1]
                dir = new_dir
                print(f"Moved forwards one space to {position} - {steps=}")
            else:
                print("Hit a wall!")
    else:
        if instruction == "R":
            dir += 1
        else:
            dir -= 1
        dir = dir % 4
        print(f"{instruction}: dir now {dir}")

print(position[0] + 1, position[1] + 1, dir)
print((position[0] + 1) * 1000 + (position[1] + 1) * 4 + dir)

# 117225 - too low
# 117296 - too low
# 144281 - too low
# 145065 - correct!!!