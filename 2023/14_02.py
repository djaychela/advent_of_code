from data_read import read_file
from copy import copy

rocks = read_file("14.txt")

cycle_target = 1000000000

rounded = []
cube = []

height = len(rocks)
width = len(rocks[0].strip())

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for ydx, line in enumerate(rocks):
    for xdx, c in enumerate(line):
        if c == "O":
            rounded.append([ydx, xdx])
        elif c == "#":
            cube.append([ydx, xdx])


def print_rocks(round_rocks):
    for h in range(height):
        line = []
        for w in range(width):
            char = "."
            if [h, w] in round_rocks:
                char = "O"
            elif [h, w] in cube:
                char = "#"
            line.append(char)
        print("".join(line))


def roll_rocks(rounded, direction):
    finished = False
    while not finished:
        moved = False
        for idx, r in enumerate(rounded):
            new_r = [r[0] + direction[0], r[1] + direction[1]]
            # check if off any edge
            if new_r[0] == -1:
                continue
            if new_r[0] == height:
                continue
            if new_r[1] == -1:
                continue
            if new_r[1] == width:
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
                # print(f"Changing {rounded[idx]} for {new_r=}")
                rounded[idx] = new_r
                moved = True
        if not moved:
            finished = True

    return rounded

# loop round directions, storing scores as we go...

scores = []
finished = False
direction = 0
run = 1
round_copy = copy(rounded)
rock_store = dict()

while not finished:
    for d in dirs:
        round_copy = roll_rocks(round_copy, d)

    score = 0

    for r in round_copy:
        score += height - r[0]
    
    # print_rocks(round_copy)
    print(f"Round {run} Finished.  Score = {score}")

    # store this set of rocks
    rock_tuple = tuple([tuple(x) for x in sorted(round_copy, key=lambda v: (v[0], v[1]))])
    if rock_tuple in rock_store.values():
        print("PATTERN ACTUALLY FOUND!!!")
        instance_1 = list(rock_store.values()).index(rock_tuple) + 1
        instance_2 = run
        finished = True
        
        # [list(my_dict.values()).index(100)]
    rock_store[run] = rock_tuple

    scores.append(score)
    
    run += 1

loop_length = instance_2 - instance_1

print(f"{instance_1=}, {instance_2=} : {loop_length=}")

full_rounds = cycle_target // loop_length

print(full_rounds)
score_index = (instance_1 + ((cycle_target - instance_1)  % loop_length) - 1)
print(scores[score_index])

# 95078 - not right answer
# 94876 - correct (after many changes!)