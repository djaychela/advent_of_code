from data_read import read_file

rock_raw = read_file("14.txt")

rock_lines = []
min_x = 10000
max_x = -10000
min_y = 10000
max_y = -10000
for line in rock_raw:
    line_str = line.strip().split(" -> ")
    current_line = []
    for st in line_str:
        x = int(st.split(",")[0])
        y = int(st.split(",")[1])
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        line_num = [x, y]
        current_line.append(line_num)
    rock_lines.append(current_line)

print(f"{min_x=} {max_x=} {min_y=} {max_y=}")

def print_grid(grid):
    for line in grid:
        print("".join(line))

# create grid
grid = [["." for _ in range(min_x - 2, max_x + 1)] for _ in range(-1 , max_y + 1)]

# draw lines
for rock_line in rock_lines:
    for idx in range(0, len(rock_line) - 1):
        # print(f"{rock_line[idx]=}")
        if rock_line[idx][0] == rock_line[idx + 1][0]:
            # vertical line
            if rock_line[idx][1] < rock_line[idx+1][1]:
                coords = [[rock_line[idx][0], x] for x in range(rock_line[idx][1], rock_line[idx + 1][1] + 1)]
            else:
                coords = [[rock_line[idx][0], x] for x in range(rock_line[idx + 1][1], rock_line[idx][1] + 1)]
        else:
            # horizontal line
            if rock_line[idx][0] < rock_line[idx+1][0]:
                coords = [[y, rock_line[idx][1]] for y in range(rock_line[idx][0], rock_line[idx + 1][0] + 1)]
            else:
                coords = [[y, rock_line[idx][1]] for y in range(rock_line[idx + 1][0], rock_line[idx][0] + 1)]

        for coord in coords:
            grid[coord[1]][coord[0] - min_x + 1] = "#"

def add_grain(grid):
    # drop sand
    c_loc = [500, 0]
    # check below
    falling = True
    while falling:
        # check below
        try:
            if grid[c_loc[1]+1][c_loc[0] - min_x + 1] == ".":
                c_loc[1] += 1
            # check below and left
            elif grid[c_loc[1]+1][c_loc[0] - min_x] == ".":
                c_loc[1] += 1
                c_loc[0] -= 1
            # check below and right
            elif grid[c_loc[1]+1][c_loc[0] - min_x + 2] == ".":
                c_loc[1] += 1
                c_loc[0] += 1
            else:
                falling = False
        except IndexError:
            return False
    return c_loc

total_grains = 0
while True:
    grain = add_grain(grid)
    if grain:
        grid[grain[1]][grain[0] - min_x + 1] = "O"
        total_grains += 1
    else:
        # leaving grid
        break
    print()
print_grid(grid)
print(f"{total_grains=}")