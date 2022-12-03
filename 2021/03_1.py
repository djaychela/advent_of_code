from data_read import read_file

binary = read_file("03.txt")

digits = []

for bin in binary:
    for idx, digit in enumerate(bin.strip()):
        try:
            digits[idx].append(int(digit))
        except IndexError:
            digits.append([int(digit)])

gamma = ""
epsilon = ""
for digit in digits:
    
    zeros = digit.count(0)
    ones = digit.count(1)
    if zeros > ones:
        gamma += "0"
        epsilon += "1"
    elif ones > zeros:
        gamma += "1"
        epsilon += "0"

gamma_d = int(gamma, 2)
epsilon_d = int(epsilon, 2)

print(f" {gamma = } -> {gamma_d = }")
print(f" {epsilon = } -> {epsilon_d = }")
print(f"{gamma_d * epsilon_d}")
    