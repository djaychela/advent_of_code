from data_read import read_file

import re

crates = read_file("05.txt")

state = [[] for i in range(0, len(crates[0]), 4)]

instructions = []
mode = 0
for line in crates:
    if line == "\n":
        mode = 1
        continue
    if mode == 0:
        if line.count("["):
            new_line = line.strip("\n")
            new_line = [line[i+1] for i in range(0, len(new_line), 4)]
            for idx, entry in enumerate(new_line):
                if entry != " ":
                    state[idx].append(entry)
    else:
        new_line = re.split(r'move|from|to| ', line.strip())
        new_line = [int(num) for num in new_line if num]
        instructions.append(new_line)

for inst in instructions:
    for idx in range(inst[0]):
        print(f"moving from {inst[1]} to {inst[2]}")
        state[inst[2]-1].insert(0,state[inst[1]-1][0])
        state[inst[1]-1].pop(0)

answer = "".join([stack[0] for stack in state])
print(answer)