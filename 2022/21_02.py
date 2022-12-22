from data_read import read_file

from copy import deepcopy

monkeys_raw = read_file("21.txt")

monkey_dict = dict()

for monkey in monkeys_raw:
    monkey_name = monkey.split(":")[0]
    monkey_instruction = monkey.split(":")[1].strip()
    try:
        monkey_instruction = int(monkey_instruction)
    except ValueError:
        monkey_instruction = monkey_instruction.split()
        
    monkey_dict[monkey_name] = monkey_instruction

min_value = 0
max_value = 30000000000000

complete = False

while not complete:
    
    current_test = (min_value + max_value) // 2

    monkey_dict_copy = deepcopy(monkey_dict)

    monkey_dict_copy["humn"] = current_test 

    changed = True
    while changed:
        changed = False
        for monkey_name, monkey_instruction in monkey_dict_copy.items():
            # print(monkey_instruction)
            if isinstance(monkey_instruction, (int, float)):
                continue
            elif monkey_name != "root":
                first_inst = monkey_dict_copy[monkey_instruction[0]]
                second_inst = monkey_dict_copy[monkey_instruction[2]]
                if isinstance(first_inst, (int, float)) and isinstance(second_inst, (int, float)):
                    new_value = eval(f"{first_inst} {monkey_instruction[1]} {second_inst}")
                    monkey_dict_copy[monkey_name] = new_value
                    changed = True

    first = monkey_dict_copy["root"][0]
    second = monkey_dict_copy["root"][2]
    print(f"Testing: {current_test} : {monkey_dict_copy[first]} and {monkey_dict_copy[second]}")

    if float(monkey_dict_copy[first]) == float(monkey_dict_copy[second]):
        print(f"Found the value: {current_test}")
        complete = True
    elif monkey_dict_copy[first] > monkey_dict_copy[second]:
        # value too high, increase seed value
        min_value = current_test
    else:
        # value too low, decrease seed value
        max_value = current_test

