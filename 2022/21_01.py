from data_read import read_file

monkeys_raw = read_file("21.txt")

print(monkeys_raw)

monkey_dict = dict()

for monkey in monkeys_raw:
    monkey_name = monkey.split(":")[0]
    monkey_instruction = monkey.split(":")[1].strip()
    try:
        monkey_instruction = int(monkey_instruction)
    except ValueError:
        monkey_instruction = monkey_instruction.split()
        
    monkey_dict[monkey_name] = monkey_instruction

changed = True
while changed:
    changed = False
    for monkey_name, monkey_instruction in monkey_dict.items():
        if isinstance(monkey_instruction, (int, float)):
            continue
        else:
            first_inst = monkey_dict[monkey_instruction[0]]
            second_inst = monkey_dict[monkey_instruction[2]]
            if isinstance(first_inst, (int, float)) and isinstance(second_inst, (int, float)):
                new_value = eval(f"{first_inst} {monkey_instruction[1]} {second_inst}")
                monkey_dict[monkey_name] = new_value
                changed = True

    # print(monkey_dict)

print(monkey_dict["root"])