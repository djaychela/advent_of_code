import os

path = os.path.join(os.getcwd(), 'data', 'input_2a.txt')
with open(path, 'r') as f:
    data = f.readlines()

puzzle_input_source = list(map(int, data[0].split(',')))
target = 19690720

# print(puzzle_input)
for i in range(100):
    for j in range(100):
        puzzle_input = puzzle_input_source.copy()
        puzzle_input[1] = i
        puzzle_input[2] = j

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
            # print(f"Altered {puzzle_input[c]} to {r}")
            puzzle_input[c] = r
            
            idx += 4

        if puzzle_input[0] == 19690720:
            print(f"Values found - {(100*i) + j}")