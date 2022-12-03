from data_read import read_file

numbers = read_file("01.txt")
nums = [int(num.strip()) for num in numbers]

increased = 0
previous = nums[0]

for idx, num in enumerate(nums):
    if idx == 0:
        pass
    if num > previous:
        increased += 1
    previous = num

print(increased)