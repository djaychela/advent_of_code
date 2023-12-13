from data_read import read_file
import numpy as np

ash_raw = read_file("13.txt")

current_ashes = []

def find_mirror(ashes):
    # find initial mirroring points
    mirrors = []
    prev_row = ""
    for idx, row in enumerate(ashes):
        if row == prev_row:
            mirrors.append(idx)
        prev_row = row
    if len(mirrors) == 0:
        return None
    # print(f"{mirrors=}")
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
            # print(f"{idx=}, {mirror=}, {mirror_idx=}")
            # print(f"{ashes[idx]=}, {ashes[mirror_idx]=}")
            if ashes[idx] != ashes[mirror_idx]:
                is_mirror = False
        if is_mirror:
            return mirror
    return None

    
def find_horizontal_mirror(ashes):
    return find_mirror(ashes)

def find_vertical_mirror(ashes):
    rotated = list(zip(*ashes[::-1]))
    return find_mirror(rotated)


def find_all_mirrors(ashes):
    vertical = find_vertical_mirror(ashes)
    horizontal = find_horizontal_mirror(ashes)
    if vertical is not None:
        return vertical
    elif horizontal is not None:
        return 100 * horizontal
    return None

score = 0
for line in ash_raw:
    if line == "\n":
        score += find_all_mirrors(current_ashes)
        current_ashes = []
    else:
        current_ashes.append(line.strip())

print(score)

# 31374 - too low
# 37718 - correct! (missed out stopping negative indexes on mirror check!)