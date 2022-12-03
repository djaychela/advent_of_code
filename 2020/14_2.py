import pathlib 
import itertools

file_name = "14.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    program = [prog.strip() for prog in file.readlines()]

memory = {}
mask = ""

for inst in program:
    opcode, value = inst.split(" = ")

    if opcode == "mask":
        mask = value

    if opcode[:3] == "mem":
        address = int(opcode.split("[")[1][:-1])
        value = int(value)
        bval = f"{address:#038b}"[2:]
        floating = ['0'] * 36
        output = ['0'] * 36
        for idx, bit in enumerate(str(bval)):
            if mask[idx] == '0':
                output[idx] = int(bval[idx])
            elif mask[idx] == '1':
                output[idx] = 1
            else:
                floating[idx] = 'X'
        bout = int(''.join(map(str,output)),2)
        x_num = floating.count('X')
        bin_poss = list(itertools.product([0, 1], repeat=x_num))
        x_idx = [idx for idx, x in enumerate(floating) if x == "X"]
        output_add = []
        for poss in bin_poss:
            current_output = ['0'] * 36
            bin_idx = 0
            for idx, char in enumerate(output):
                if idx in x_idx:
                    current_output[idx] = poss[bin_idx]
                    bin_idx += 1
                else:
                    current_output[idx] = output[idx]
            output_add.append(int("".join(map(str, current_output)),2))
        for output in output_add:
            memory[output] = value

print(sum(memory.values()))