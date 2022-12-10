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

strength_total = 0

for idx in range(19, len(state), 40):
    strength = (idx+1) * state[idx]
    strength_total += strength

print(f"Total Signal Strength: {strength_total}")
