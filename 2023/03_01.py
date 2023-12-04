from data_read import read_file

schematic = read_file("03.txt")

non_symbol = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = []

for ydx, line in enumerate(schematic):
    for xdx, cell in enumerate(line.strip()):
        if cell not in non_symbol:
            symbols.append((ydx, xdx))

def check_near(coords):
    # check if location is near a symbol coordinate
    for ydx in range(-1, 2):
        for xdx in range(-1, 2):
            y = coords[0] + ydx
            x = coords[1] + xdx
            if (y,x) in symbols:
                return True
    return False

valid_numbers = []

for ydx, line in enumerate(schematic):
    current_number = ""
    near_symbol = False
    for xdx, cell in enumerate(line.strip()):
        if cell in numbers:
            current_number += cell
            # print(f"checking for {current_number=}")
            if not near_symbol:
                near_symbol = check_near((ydx, xdx))
            # print(f"{near_symbol=}")
        elif cell not in numbers and len(current_number) > 0:
            # print(current_number)
            if near_symbol:
                valid_numbers.append(int(current_number))
            current_number = ""
            near_symbol = False
    if len(current_number) > 0:
        # end of line number
        # print(current_number)
        if near_symbol:
            valid_numbers.append(int(current_number))
            # end of number
        # find groups of numbers

print(sum(valid_numbers))