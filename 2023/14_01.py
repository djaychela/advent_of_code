from data_read import read_file

rocks = read_file("14.txt")

rounded = []
cube = []

height = len(rocks)
width = len(rocks[0].strip())

for ydx, line in enumerate(rocks):
    for xdx, c in enumerate(line):
        if c == "O":
            rounded.append([ydx, xdx])
        elif c == "#":
            cube.append([ydx, xdx])

finished = False

def print_rocks():
    for h in range(height):
        line = []
        for w in range(width):
            char = "."
            if [h, w] in rounded:
                char = "O"
            elif [h, w] in cube:
                char = "#"
            line.append(char)
        print("".join(line))


while not finished:
    moved = False
    for idx, r in enumerate(rounded):
        new_r = [r[0]-1, r[1]]
        if new_r[0] == -1:
            continue
        movable = True
        for c in cube:
            if c == new_r:
                movable = False
        for r_2 in rounded:
            if r_2 == r:
                continue
            elif r_2 == new_r:
                movable = False
        # print(f"{movable=}")
        if movable:
            print(f"Changing {rounded[idx]} for {new_r=}")
            rounded[idx] = new_r
            moved = True
    print("**** ****")
    # print_rocks()
    print(f"{moved=}")
    if not moved:
        finished = True

score = 0

for r in rounded:
    score += height - r[0]

print(score)
# print_rocks()              