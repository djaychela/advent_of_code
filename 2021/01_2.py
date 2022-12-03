from data_read import read_file

numbers = read_file("01.txt")
nums = [int(num.strip()) for num in numbers]

increased = 0

for idx, num in enumerate(nums[3:]):
    if idx == 0:
        pass
    if num > nums[idx]:
        increased += 1

print(increased)