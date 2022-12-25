from data_read import read_file

snafu_raw = read_file("25.txt")

print(snafu_raw)

sd_conversion = { "2" : 2, "1" : 1, "0": 0, "-": -1, "=": -2}
ds_conversion = { 0 : "0", 1 : "1", 2 : "2", 3 : "=", 4 : "-"}

currents = []

for snafu in snafu_raw:
    digit = 1
    current = 0
    nums = list(snafu.strip())[::-1]
    for num in nums:
        current += sd_conversion[num] * digit
        digit *= 5
    currents.append(current)

answer = sum(currents)

answer_list = []

while answer > 0:
    current_digit = answer % 5
    answer = answer // 5
    if current_digit > 2:
        answer += 1
    answer_list.append(ds_conversion[current_digit])

print("".join(answer_list[::-1]))