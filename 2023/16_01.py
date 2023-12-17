from data_read import read_file

# Failed first attempt.  Spent AGES on this and gave up as it was just getting too complex.

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
    locations = [(loc[0], loc[1]) for loc in locations]
    for ydx,line in enumerate(grid):
        current_line = []
        for xdx, char in enumerate(line):
            if (ydx, xdx) in locations:
                current_line.append("#")
            else:
                current_line.append(char)
        current_line.append(" : ")
        current_line += line
        print("".join(current_line))


def move_beam(location, direction):
    location[0] += directions[direction][0]
    location[1] += directions[direction][1]
    return location

def inside_grid(loc):
    inside = True
    if loc[0] < 0:
        inside = False
    elif loc[0] > height - 1:
        inside = False
    if loc[1] < 0:
        inside = False
    elif loc[1] > width - 1:
        inside = False
    return inside

def check_present(current_location, direction, visited):
    if (current_location[0], current_location[1], direction) in visited:
        return True
    return False

def store_location(loc, direction):
    global visited
    if inside_grid(loc):
        if (loc[0], loc[1], direction) not in visited:
            # print(f"Storing {loc=}, {direction=}")
            visited.append((loc[0], loc[1], direction))
            return False
        else:
            return True
    return True

def follow_beam(grid, loc, direction):
    print(f"FB: {loc=}, {direction=}")
    global visited
    if check_present(loc, direction,visited):
        return []
    finished = False
    while not finished:
        cur_loc = grid[loc[0]][loc[1]]
        if cur_loc == ".":
            # continue in current direction
            loc = move_beam(loc, direction)
        elif cur_loc == "\\":
            # mirror \
            mirror = { 0:1, 1:0, 2:3, 3:2 }
            direction = mirror[direction]
            loc = move_beam(loc, direction)

        elif cur_loc == "/":
            # mirror /
            mirror = { 0:3, 3:0, 2:1, 1:2 }
            direction = mirror[direction]
            loc = move_beam(loc, direction)

        elif cur_loc == "|":
            # beam splitter |
            if (loc[0], loc[1], direction) not in visited:
                # print(f"Storing Splitter {loc=}, {direction=}")
                visited.append((loc[0], loc[1], direction))
            if direction in [0, 2]:
                loc_1 = move_beam([loc[0], loc[1]], 1)
                loc_2 = move_beam([loc[0], loc[1]], 3)
                if not check_present(loc_1, direction, visited):
                    finished = store_location(loc_1, direction)
                    follow_beam(mirror_grid, loc_1, 1)
                else:
                    finished = True
                # print(f"loc_1: {visited=}")
                if not check_present(loc_2, direction, visited):
                    finished = store_location(loc_2, direction)
                    follow_beam(mirror_grid, loc_2, 3)
                else:
                    finished = True
                # print(f"loc_2: {visited=}")
                finished = True
            else:
                loc = move_beam(loc, direction)

        elif cur_loc == "-":
            # beam splitter -
            if (loc[0], loc[1], direction) not in visited:
                # print(f"Storing Splitter {loc=}, {direction=}")
                visited.append((loc[0], loc[1], direction))
            if direction in [1, 3]:
                loc_1 = move_beam([loc[0], loc[1]], 0)
                loc_2 = move_beam([loc[0], loc[1]], 2)
                if not check_present(loc_1, direction, visited):
                    print("Following - dir 0")
                    print(f"{loc_1=}")
                    finished = store_location(loc_1, direction)
                    follow_beam(mirror_grid, loc_1, 0)
                else:
                    finished = True
                # print(f"loc_1: {visited=}")
                if not check_present(loc_2, direction, visited):
                    print("Following - dir 2")
                    print(f"{loc_2=}")
                    finished = store_location(loc_2, direction)
                    follow_beam(mirror_grid, loc_2, 2)
                else:
                    print("Skipping - dir 2")
                    print(f"{loc_2=}")
                    finished = True
                # finished = True
            else:
                # TODO - fix movement so it happens here, not later?
                loc = move_beam(loc, direction)
                # pass
                # print(f"loc_2: {visited=}")
        finished = store_location(loc, direction)

        if not finished:
            finished = not(inside_grid(loc))
        # print(f"{finished=}")
        display_grid(mirror_grid, visited)
    return visited

visited = []

visited = follow_beam(mirror_grid, loc, 0)
visited.append((0,0,0))
display_grid(mirror_grid, visited)
# print(visited)
print(len(visited))
print(visited.count((0,0,0)))

