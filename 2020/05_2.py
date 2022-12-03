import pathlib

file_name = "05.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    seat_ids = file.readlines()

highest = 0
seats = 7
rows = 106

seating_plan = [[0 for _ in range(seats)] for _ in range(rows)]


for seat_id in seat_ids:
    row = int(seat_id[:7].replace("F", "0").replace("B", "1"), 2)
    seat = int(seat_id[7:].replace("L", "0").replace("R", "1"), 2)
    seating_plan[row - 1][seat - 1] = 1

for i in range(rows):
    for j in range(seats):
        if seating_plan[i][j] == 0:
            print(f"seat free at id {(i + 1) * 8 + j + 1}")
