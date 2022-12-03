import pathlib

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
        bval = f"{value:#038b}"[2:]
        output = [0] * 36
        for idx, bit in enumerate(str(bval)):
            if mask[idx] == '0':
                output[idx] = 0
            elif mask[idx] == '1':
                output[idx] = 1
            else:
                output[idx] = int(bval[idx])
        bout = int(''.join(map(str,output)),2)
        memory[address] = bout

print(sum(memory.values()))