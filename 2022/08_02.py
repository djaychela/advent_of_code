import numpy as np

from data_read import read_file

trees_data = read_file("08.txt")

trees = [[0 for _ in range(len(trees_data[0].strip()))] for _ in range(len(trees_data))]

for idx, line in enumerate(trees_data):
    for jdx, cell in enumerate(line.strip()):
        trees[idx][jdx] = cell

def check_scenic(i, j, trees):
    scenic = [0, 0, 0, 0]
    tree_height = trees[i][j]
    # check above i
    for idx in range(i-1, -1, -1):
        if trees[idx][j] < tree_height:
            scenic[0] += 1
        elif trees[idx][j] >= tree_height:
            scenic[0] += 1
            break
    # check below i
    for idx in range(i+1, len(trees)):
        if trees[idx][j] < tree_height:
            scenic[1] += 1
        elif trees[idx][j] >= tree_height:
            scenic[1] += 1
            break
    # check above j
    for jdx in range(j-1, -1, -1):
        if trees[i][jdx] < tree_height:
            scenic[2] += 1
        elif trees[i][jdx] >= tree_height:
            scenic[2] += 1
            break
    # check below j
    for jdx in range(j+1, len(trees[0])):
        if trees[i][jdx] < tree_height:
            scenic[3] += 1
        elif trees[i][jdx] >= tree_height:
            scenic[3] += 1
            break
    return np.prod(scenic)

best = 0

for idx in range(len(trees)):
    for jdx in range(len(trees[0])):
        scenic = check_scenic(idx, jdx, trees)
        print(f"{idx=}:{jdx=} - {trees[idx][jdx]} := {scenic}")
        best = max(best, scenic)

print(f"Best location score: {best}")

