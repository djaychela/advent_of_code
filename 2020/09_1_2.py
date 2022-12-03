import pathlib
from itertools import permutations

file_name = "09.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    xmas = [int(xma.strip()) for xma in file.readlines()]


preamble = 25
for idx in range(preamble, len(xmas)):
    current = xmas[idx]
    possibles = list(permutations(xmas[idx-preamble:idx], 2))
    sums = [sum(possible) for possible in possibles]
    if current not in sums:
        target = current
        print(f"Target: {current}")
        break
        

for length in range(2, len(xmas)):
    for idx in range(len(xmas)):
        nums = xmas[idx:idx+length]
        a = sum(nums)
        if a == target:
            print(f"Sequence: {nums}")
            print(f"Weakness: {min(nums) + max(nums)}")
            



