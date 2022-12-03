import pathlib

file_name = "08.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    code = file.readlines()

memory = {}
registers = {}
program_counter = 0
executed = []
running = True
registers['acc'] = 0

for idx, opcode in enumerate(code):
    memory[idx] = opcode.strip()

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
    executed.append(program_counter)

print(registers)
