from data_read import read_file

trees_data = read_file("08.txt")

trees = [[0 for _ in range(len(trees_data[0].strip()))] for _ in range(len(trees_data))]

for idx, line in enumerate(trees_data):
    for jdx, cell in enumerate(line.strip()):
        trees[idx][jdx] = cell

def check_visible(i, j, trees):
    visible = [True, True, True, True]
    tree_height = trees[i][j]
    # check above i
    for idx in range(i-1, -1, -1):
        if trees[idx][j] >= tree_height:
            visible[0] = False
    # check below i
    for idx in range(i+1, len(trees)):
        if trees[idx][j] >= tree_height:
            visible[1] = False
    # check above j
    for jdx in range(j-1, -1, -1):
        if trees[i][jdx] >= tree_height:
            visible[2] = False
    # check below j
    for jdx in range(j+1, len(trees[0])):
        if trees[i][jdx] >= tree_height:
            visible[3] = False
    return any(visible)

total = 0

for idx in range(len(trees)):
    for jdx in range(len(trees[0])):
        visible = check_visible(idx, jdx, trees)
        print(f"{idx=}:{jdx=} - {trees[idx][jdx]} := {visible}")
        total += visible

print(f"Trees Visible from outside grid: {total}")