import pathlib

file_name = "01.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    nums = file.readlines()

nums = [int(num.strip()) for num in nums]

target = 2020

# narrow down list a bit

maximum = max(nums)
minimum = min(nums)
nums = [num for num in nums if target - maximum <= num <= target - minimum]

solved = False

for idx in range(len(nums)):
    for jdx in range(len(nums)):
        for kdx in range(len(nums)):
            if idx == jdx or idx == kdx or jdx == kdx:
                continue
            if nums[idx] + nums[jdx] + nums[kdx] == target:
                solved = True
                print(f"{nums[idx]} + {nums[jdx]} + {nums[kdx]}")
                print(f"{nums[idx] * nums[jdx] * nums[kdx]}")
                break
        if solved:
            break
    if solved:
        break
