from data_read import read_file

instructions = read_file("02.txt")

print(instructions)

instructions = [(inst.strip().split()[0],int(inst.strip().split()[1])) for inst in instructions]

horizontal = 0
depth = 0
aim = 0

for instruction in instructions:
    match instruction[0]:
        case "forward":
            horizontal += instruction[1]
            depth += aim * instruction[1]
        case "down":
            aim += instruction[1]
        case "up":
            aim -= instruction[1]

print(f"{horizontal = }")
print(f"{depth = }")

print(f"Answer = {horizontal * depth }")

