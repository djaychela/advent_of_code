from data_read import read_file
import numpy as np
from copy import copy

ash_raw = read_file("13.txt")

# load into arrays
# split at line

current_ashes = []

def find_mirror(ashes, score):
    # find initial mirroring points
    mirrors = []
    prev_row = ""
    for idx, row in enumerate(ashes):
        if row == prev_row and idx != score:
            mirrors.append(idx)
        prev_row = row
    if len(mirrors) == 0:
        return None
    # examine each
    # start at mirror row
    # check outers until out of bounds
    limit = len(ashes)
    for mirror in mirrors:
        is_mirror = True
        for idx in range(mirror, limit):
            mirror_idx = mirror - 1 - (idx-mirror)
            if mirror_idx < 0:
                break
            if ashes[idx] != ashes[mirror_idx]:
                is_mirror = False
        if is_mirror:
            return mirror
    return None

    
def find_horizontal_mirror(ashes, original_score):
    return find_mirror(ashes, int(original_score / 100))

def find_vertical_mirror(ashes, original_score):
    rotated = list(zip(*ashes[::-1]))
    return find_mirror(rotated, original_score % 100)


def find_all_mirrors(ashes, original_score):
    vertical = find_vertical_mirror(ashes, original_score)
    horizontal = find_horizontal_mirror(ashes, original_score)
    if vertical is not None and vertical != original_score:
        return vertical
    elif horizontal is not None and horizontal * 100 != original_score:
        return 100 * horizontal
    return None

# store original solution first
# change one from . to # or vice versa, retest for each?
# then check for all possible changes
# if new score, change the score, otherwise score the old one.

def unsmudge_ashes(ashes, y, x):
    current_cell = ashes[y][x]
    if current_cell == ".":
        ashes[y] = ashes[y][:x] + "#" + ashes[y][x+1:]
    elif current_cell == "#":
        ashes[y] = ashes[y][:x] + "." + ashes[y][x+1:]
    else:
        assert False
    return ashes

def print_ashes(ashes):
    for idx, line in enumerate(ashes, 1):
        print(f"{idx:02d} : {line}")

score = 0
for line in ash_raw:
    if line == "\n":
        original_score = find_all_mirrors(current_ashes, 0)
        print(f"{original_score=}")
        # change each one and re-score
        # break out of loop if new score occurs
        done = False
        for ydx in range(len(current_ashes)):
            for xdx in range(len(current_ashes[1])):
                smudged_ashes = unsmudge_ashes(copy(current_ashes), ydx, xdx)
                new_score = find_all_mirrors(smudged_ashes, original_score)
                if new_score is not None:
                    print("new score found!!!")
                    print(f"{new_score=}")
                    done = True
                    original_score = new_score
                    break
            if done:
                break
        score += original_score
        current_ashes = []
    else:
        current_ashes.append(line.strip())

print(score)

# 31552 - too low
# 40995 - correct (original mirror detection was returning previous value when it was the first one of multiple mirrors)
