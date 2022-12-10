from data_read import read_file

instructions = read_file("10.txt")

x = 1
cycle = 0
state = []

for inst in instructions:
    inst = inst.strip().split()
    try:
        inst[1] = int(inst[1])
    except IndexError:
        pass
    if inst[0] == "noop":
        state.append(x)
    elif inst[0] == "addx":
        state.append(x)
        state.append(x)
        x += inst[1]

state.append(x)

crt_data = [[" " for _ in range(40)] for _ in range(6)]

for idx in range(0, len(state) - 1, 40):
    for jdx in range(40):
        current = idx + jdx
        if jdx - 1 <= state[current] <= jdx + 1:
            crt_data[int(idx/40)][jdx] = "#"

for row in crt_data:
    print("".join(row))