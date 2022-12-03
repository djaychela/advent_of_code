import os

path = os.path.join(os.getcwd(), 'data', 'input_2a.txt')
with open(path, 'r') as f:
    data = f.readlines()

puzzle_input = list(map(int, data[0].split(',')))

print(puzzle_input)
puzzle_input[1] = 12
puzzle_input[2] = 2

idx = 0
while idx < len(puzzle_input)-1:
    opcode = puzzle_input[idx]
    a = puzzle_input[idx + 1]
    b = puzzle_input[idx + 2]
    c = puzzle_input[idx + 3]
    if opcode == 1:
        r = puzzle_input[a] + puzzle_input[b]
    elif opcode == 2:
        r = puzzle_input[a] * puzzle_input[b]
    elif opcode == 99:
        break
    print(f"Altered {puzzle_input[c]} to {r}")
    puzzle_input[c] = r
    
    idx += 4

print(puzzle_input)