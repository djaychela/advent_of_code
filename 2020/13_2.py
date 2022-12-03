import pathlib
import math


def get_lcm(n1, n2):
    gcd = math.gcd(n1, n2)
    return (n1 * n2) / gcd


file_name = "13.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    buses = [direction.strip() for direction in file.readlines()]

bus_time_list = [int(bus) if bus != "x" else 0 for bus in buses[1].split(",")]
increment = bus_time_list[0]
start_time = increment

solved = False
sfi = 1

while not solved:
    this_run_ok = True
    if bus_time_list[sfi] != 0:
        current_value = start_time + sfi
        if current_value / bus_time_list[sfi] == current_value // bus_time_list[sfi]:
            print(f"Solved for {sfi}: start_time :{start_time}")
            increment = int(get_lcm(bus_time_list[sfi], increment))
            sfi += 1
            if sfi >= len(bus_time_list):
                solved = True
            try:
                while bus_time_list[sfi] == 0:
                    sfi += 1
            except IndexError:
                solved = True

    else:
        while bus_time_list[sfi] == 0:
            sfi += 1

    start_time += increment
