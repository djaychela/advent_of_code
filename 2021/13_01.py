from data_read import read_file

origami = read_file("13.txt")

splitpoint = origami.index("\n")

dots = [[int(pos) for pos in dot.strip().split(",")] for dot in origami[:splitpoint]]
folds = [fold.strip().split()[2].split("=") for fold in origami[splitpoint + 1:]]

def horizontal_fold(dots, index, fold_location):
    dot = dots[index]
    dot[1] = fold_location - (dot[1] - fold_location)
    dots[index] = dot

def vertical_fold(dots, index, fold_location):
    dot = dots[index]
    dot[0] = fold_location - (dot[0] - fold_location)
    dots[index] = dot

def count_unique(dots):
    unique = []
    for dot in dots:
        if dot not in unique:
            unique.append(dot)
    return len(unique)

def image_output(dots):
    x_size = 0
    y_size = 0
    for dot in dots:
        x_size = max(x_size, dot[0])
        y_size = max(y_size, dot[1])
    image_grid = [[" " for x in range(x_size + 1) ] for y in range(y_size + 1)]
    for dot in dots:
        image_grid[dot[1]][dot[0]] = "*"
    for image in image_grid:
        print("".join(image))

for fdx, fold in enumerate(folds):
    fold_direction = fold[0]
    fold_location = int(fold[1])
    for idx, dot in enumerate(dots):
        if fold_direction == "x":
            if dot[0] > fold_location:
                vertical_fold(dots, idx, fold_location)
        if fold_direction == "y":
            if dot[1] > fold_location:
                horizontal_fold(dots, idx, fold_location)
    if fdx == 0:
        print(f"After First Fold: {count_unique(dots)} Dots")

image_output(dots)