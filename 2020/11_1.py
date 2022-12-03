import pathlib
import copy

file_name = "11.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    seating = [list(seat_row.strip()) for seat_row in file.readlines()]

cols = len(seating[0])
rows = len(seating)
changes = True
runs = 1

def display_seating(seat_array):
    score = 0
    for row in seat_array:
        for seat in row:
            print(seat, end='')
            if seat == "#":
                score += 1
        print()
    return score

while changes:
    changes = False
    previous = copy.deepcopy(seating)
    for row in range(rows):
        for col in range(cols):
            if previous[row][col] != ".":
                occupied = 0
                for idx in range(-1, 2):
                    for jdx in range(-1, 2):
                        if 0 <= (row+idx) < rows:
                            if 0 <= (col+jdx) < cols:
                                    if previous[row+idx][col+jdx] == "#":
                                        if idx == 0 and jdx == 0:
                                            pass
                                        else:
                                            occupied += 1
                
                if previous[row][col] == "L" and occupied == 0:
                    seating[row][col] = "#"
                    changes = True
                if previous[row][col] == "#" and occupied >= 4:
                    seating[row][col] = "L"
                    changes = True
    score = display_seating(seating)
    print(f"Run {runs} complete. Score = {score}")
    runs += 1


