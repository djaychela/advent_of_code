from data_read import read_file

schematic = read_file("03.txt")

non_symbol = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = []

for ydx, line in enumerate(schematic):
    for xdx, cell in enumerate(line.strip()):
        if cell == "*":
            print(f"{ydx=}, {xdx=}, {cell}")
            symbols.append((ydx, xdx))

print(symbols)

def check_near(coords):
    # check if location is near a symbol coordinate
    for ydx in range(-1, 2):
        for xdx in range(-1, 2):
            y = coords[0] + ydx
            x = coords[1] + xdx
            if (y,x) in symbols:
                return True, (y, x)
    return False, (-1, -1)

valid_numbers = []

for ydx, line in enumerate(schematic):
    current_number = ""
    near_symbol = False
    for xdx, cell in enumerate(line.strip()):
        if cell in numbers:
            current_number += cell
            if not near_symbol:
                near_symbol, gear_coords = check_near((ydx, xdx))
        elif cell not in numbers and len(current_number) > 0:
            if near_symbol:
                valid_numbers.append((int(current_number), gear_coords))
            current_number = ""
            near_symbol = False
    if len(current_number) > 0:
        # end of line number
        if near_symbol:
            valid_numbers.append((int(current_number), gear_coords))

print(valid_numbers)
total = 0
# find matching pairs in valid numbers
for idx, number in enumerate(valid_numbers):
    for jdx, num_2 in enumerate(valid_numbers):
        if number[1] == num_2[1] and idx != jdx:
            total += number[0] * num_2[0]

print(int(total / 2))
