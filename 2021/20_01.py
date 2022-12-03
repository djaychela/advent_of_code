from data_read import read_file

image_enhance = read_file("20.txt")

image_enhance = [scanner.strip() for scanner in image_enhance]

algo = image_enhance[0]

image = image_enhance[2:]

def get_pixel_values(grid, x, y):
    values = []
    for idx in range(x-1, x+2):
        for jdx in range(y-1, y+2):
            if [idx, jdx] in grid:
                values.append("1")
            else:
                values.append("0")
    binary = "".join(values)
    return int(binary, 2)

def convert_grid(image):
    grid = []
    for idx in range(len(image)):
        for jdx in range(len(image[0])):
            if image[idx][jdx] == "#":
                grid.append([idx, jdx])
    return grid

def find_next_scan_size(grid, padding):
    y_values = [entry[1] for entry in grid]
    x_values = [entry[0] for entry in grid]
    min_x = min(x_values)
    max_x = max(x_values)
    min_y = min(y_values)
    max_y = max(y_values)
    return min_x - padding, max_x + padding + 1, min_y - padding,  max_y + padding + 1

def fill_extra_spaces(grid, padding = 3):
    x_1, x_2, y_1, y_2 = find_next_scan_size(grid, 0)
    print(f"Padding: {x_1=}, {x_2=}, {y_1=}, {y_2=}")
    for x in range(x_1, x_2):
        for y in range(y_1 - padding, y_1):
            grid.append([x, y])
        for y in range(y_2, y_2 + padding):
            grid.append([x, y])
    for y in range(y_1 - padding, y_2 + padding):
        for x in range(x_1 - padding, x_1):
            grid.append([x, y])
        for x in range(x_2, x_2 + padding):
            grid.append([x, y])
    return grid

def clear_extra_spaces(grid, padding = 3):
    x_1, x_2, y_1, y_2 = find_next_scan_size(grid, 0)
    x_1 += padding
    x_2 -= padding
    y_1 += padding
    y_2 -= padding
    print(f"Clearing: {x_1=}, {x_2=}, {y_1=}, {y_2=}")
    def clear_entry(x, y):
        try:
            grid.remove([x, y])
        except ValueError:
            pass
    for x in range(x_1, x_2):
        for y in range(y_1 - padding, y_1):
            clear_entry(x, y)
        for y in range(y_2, y_2 + padding):
            clear_entry(x, y)
    for y in range(y_1 - padding, y_2 + padding):
        for x in range(x_1 - padding, x_1):
            clear_entry(x, y)
        for x in range(x_2, x_2 + padding):
            clear_entry(x, y)
    return grid
    

def display_grid(grid):
    x_1, x_2, y_1, y_2 = find_next_scan_size(grid, 3)
    image_grid = [["." for _ in range(y_1, y_2)] for _ in range(x_1, x_2)]
    for pixel in grid:
        image_grid[pixel[0] - x_1][pixel[1] - y_1] = "#"
    output_grid = [["".join(image_line)] for image_line in image_grid]
    for output in output_grid:
        print(output)

grid = convert_grid(image)

display_grid(grid)

for runs in range(1, 51):
    x_1, x_2, y_1, y_2 = find_next_scan_size(grid, 3)
    print(f"Run: {runs} -> Scanning: {x_1=}, {x_2=}, {y_1=}, {y_2=}")
    new_grid = []
    for x in range(x_1, x_2):
        for y in range(y_1, y_2):
            kernel = get_pixel_values(grid, x, y)
            lookup = algo[kernel]
            # print(f"{x=}, {y=}:  {kernel}->{lookup}")
            if lookup == "#":
                new_grid.append([x, y])
    # display_grid(new_grid)
    if runs % 2 != 0:
        new_grid = fill_extra_spaces(new_grid, 5)
    elif runs != 0:
        new_grid = clear_extra_spaces(new_grid, 5)
    display_grid(new_grid)
    grid = new_grid.copy()
    print(f"Number of Pixels: {len(grid)}")
