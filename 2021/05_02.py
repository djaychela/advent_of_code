from data_read import read_file

locations = {}

lines = read_file("05.txt")

def create_line_coords(start, end):
    x_start = min(start[0], end[0])
    x_end = max(start[0], end[0])
    y_start = min(start[1], end[1])
    y_end = max(start[1], end[1])
    if x_start == x_end or y_start == y_end:
        # horizontal or vertical
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
    else:
        # diagonal
        if start[0] > end[0]:
            start[0], end[0] = end[0], start[0]
            start[1], end[1] = end[1], start[1]
        x_delta = int((end[0] - start[0]) / abs(end[0] - start[0]))
        y_delta = int((end[1] - start[1]) / abs(end[1] - start[1]))

        x = start[0]
        y = start[1]
        while x <= end[0]:
            try:
                test = locations[x]
            except KeyError:
                locations[x] = {}
            try:
                locations[x][y] += 1
            except KeyError:
                locations[x][y] = 1
            x += x_delta
            y += y_delta
    
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
    max_x = max(max_x, first[0], second[0])
    max_y = max(max_y, first[1], second[1])
    create_line_coords(first, second)

print(locations)
display_grid(locations, max_x, max_y)