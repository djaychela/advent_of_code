import pathlib

file_name = "08.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    code = file.readlines()

final_instruction = len(code)
memory = {}


modification_needed = True
memory_locations = range(len(code))

for memory_location in memory_locations:
    running = True
    program_counter = 0
    registers = {}
    executed = []
    registers["acc"] = 0

    for idx, opcode in enumerate(code):
        memory[idx] = opcode.strip()

    # modify memory
    opcode, argument = memory[memory_location].split()
    if opcode == "nop":
        opcode = "jmp"
    if opcode == "jmp":
        opcode = "nop"
    else:
        continue
    memory[memory_location] = f"{opcode} {argument}"

    while running:
        opcode, argument = memory[program_counter].split()
        argument = int(argument)
        pc_increment = 1

        if opcode == "acc":
            registers["acc"] += argument
        if opcode == "jmp":
            pc_increment = argument

        program_counter += pc_increment
        if program_counter in executed:
            running = False
        if program_counter == final_instruction:
            modification_needed = False
            running = False
        executed.append(program_counter)

    if not modification_needed and program_counter == final_instruction:
        print(memory_location, program_counter, registers, modification_needed)
