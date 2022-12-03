import pathlib

file_name = "13.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    buses = [direction.strip() for direction in file.readlines()]

desired_time = int(buses[0])
bus_list = [int(bus) for bus in buses[1].split(",") if bus != "x"]

nearest = desired_time
bus_id = 0
for bus in bus_list:
    after = ((int(desired_time / bus) + 1) * bus) - desired_time
    if after < nearest:
        nearest = after
        bus_id = bus

print(nearest * bus_id)

