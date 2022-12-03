import pathlib

file_name = "01.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    nums = file.readlines()

nums = [int(num.strip()) for num in nums]

target = 2020
for num in nums:
    desired = target - num
    if desired in nums:
        print(f"Found it - {num} -> {desired}")
        print(desired * num)
    