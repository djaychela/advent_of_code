import pathlib

file_name = "02.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    wrapping = [list(map(int, wrap.strip().split('x'))) for wrap  in file.readlines()]

total_area = 0
for wrap in wrapping:
    sides_a = 2 * wrap[0] * wrap[1]
    sides_b = 2 * wrap[1] * wrap[2]
    sides_c = 2 * wrap[0] * wrap[2]
    slack = min(sides_a, sides_b, sides_c) / 2
    total = sides_a + sides_b + sides_c + slack
    total_area += total

print(total_area)