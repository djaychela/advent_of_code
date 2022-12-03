import pathlib
from itertools import permutations, combinations

file_name = "10_test.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    adapters = [int(adapter.strip()) for adapter in file.readlines()]

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

routes = [0] * (adapters[-1] + 1)
routes[0] = 1

# count links
for idx in adapters:
    for b in range(1, 4):
        if (idx - b) in adapters:
            routes[idx] += routes[idx - b]

# 'view' graph           
for idx, route in enumerate(routes):
    if idx in adapters:
        print(f"{idx}: {route}")

print(f"Number of routes :{routes[-1]}")
