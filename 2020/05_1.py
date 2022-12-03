import pathlib

file_name = "05.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    seat_ids = file.readlines()

highest = 0

for seat_id in seat_ids:
    row = int(seat_id[:7].replace("F", "0").replace("B", "1"), 2)
    seat = int(seat_id[7:].replace("L", "0").replace("R", "1"), 2)
    highest = max(highest, (row * 8) + seat)

print(highest)
