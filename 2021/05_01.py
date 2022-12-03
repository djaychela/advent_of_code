from data_read import read_file

locations = {}

lines = read_file("05_test.txt")

def create_line_coords(start, end):
    x_start = min(start[0], end[0])
    x_end = max(start[0], end[0])
    y_start = min(start[1], end[1])
    y_end = max(start[1], end[1])
    for x in range(x_start, x_end + 1):
        for y in range(y_start, y_end + 1):
            try:
                test = locations[x]
            except KeyError:
                locations[x] = {}
            try:
                locations[x][y] += 1
            except KeyError:
                locations[x][y] = 1

def display_grid(location_dict, x_size, y_size):
    dangerous = 0
    for x in range(x_size + 1):
        current_line = ""
        for y in range(y_size + 1):
            try:
                current_line += str(location_dict[x][y])
                if location_dict[x][y] >= 2:
                    dangerous += 1
            except KeyError:
                current_line += "."
        print(current_line)
    print(f"Dangerous spots: {dangerous}")

max_x = 0
max_y = 0

for line in lines:
    coords = line.strip().split(" -> ")
    first = [int(coord) for coord in coords[0].split(",")]
    second = [int(coord) for coord in coords[1].split(",")]
    # check if horizontal or vertical
    max_x = max(max_x, first[0], second[0])
    max_y = max(max_y, first[1], second[1])
    if first[0] == second[0] or first[1] == second[1]:
        print(f"Using {first}, {second}")
        create_line_coords(first, second)
    # print(locations)
    # cont = input("Waiting....")

print(locations)
display_grid(locations, max_x, max_y)