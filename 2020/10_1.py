import pathlib

file_name = "10.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    adapters = [int(adapter.strip()) for adapter in file.readlines()]

adapters.sort()

current = 0
differences = {1:0, 3:0}
for adapter in adapters:
    difference = adapter - current
    differences[difference] += 1
    current = adapter
differences[3] += 1
print(differences)
print(differences[1] * differences[3])
