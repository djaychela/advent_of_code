import os

path = os.path.join(os.getcwd(), 'data', 'input_5a.txt')
with open(path, 'r') as f:
    data = f.readlines()

puzzle_input = list(map(int, data[0].split(',')))
input_value = 5

# print(puzzle_input)

def get_data(index, mode):
    if mode == '0':
        return puzzle_input[puzzle_input[index]]
    else:
        return puzzle_input[index]

def get_index(index, mode):
    if mode == '0':
        return puzzle_input[index]
    else:
        return index

idx = 0
print(f'idx:{idx} P:{puzzle_input}')
while idx < len(puzzle_input)-1:
    modes = f"{puzzle_input[idx]:0>5}"
    mode_a = modes[2]
    mode_b = modes[1]
    mode_c = modes[0]
    opcode = modes[3:]
    print(f'current opcode: {opcode}')
    if opcode == '01':
        a = get_data(idx+1, mode_a)
        b = get_data(idx+2, mode_b)
        c = get_index(idx+3, mode_c)
        r = a + b
        print(f"Opcode {opcode}: Altered {puzzle_input[c]} to {r}")
        puzzle_input[c] = r
        increment = 4
        

    elif opcode == '02':
        a = get_data(idx+1, mode_a)
        b = get_data(idx+2, mode_b)
        c = get_index(idx+3, mode_c)
        r = a * b
        print(f"Opcode {opcode}: Altered {puzzle_input[c]} to {r}")
        puzzle_input[c] = r
        increment = 4
        

    elif opcode == '03':
        a = get_index(idx+1, mode_a)
        print(f"Opcode {opcode}: idx{idx}: Altered {puzzle_input[a]} to {input_value}")
        puzzle_input[a] = input_value
        increment = 2
        
    elif opcode == '04':
        a = get_index(idx+1, mode_a)
        increment = 2
        print(f"Opcode {opcode}: Output is {puzzle_input[a]}")

    elif opcode == '05':
        a = get_data(idx+1, mode_a)
        b = get_data(idx+2, mode_b)
        if a != 0:
            increment = 0
            idx = b
        else:
            increment = 3

    elif opcode == '06':
        a = get_data(idx+1, mode_a)
        b = get_data(idx+2, mode_b)
        print(f"Opcode 06: a:{a}, b:{b}")
        if a == 0:
            increment = 0
            idx = b
        else:
            increment = 3

    elif opcode == '07':
        a = get_data(idx+1, mode_a)
        b = get_data(idx+2, mode_b)
        c = get_index(idx+3, mode_c)
        if a < b:
            puzzle_input[c] = 1
        else:
            puzzle_input[c] = 0
        increment = 4

    elif opcode == '08':
        a = get_data(idx+1, mode_a)
        b = get_data(idx+2, mode_b)
        c = get_index(idx+3, mode_c)
        if a == b:
            puzzle_input[c] = 1
        else:
            puzzle_input[c] = 0
        increment = 4

    elif opcode == '99':
        print('Opcode 99: END')
        break
    
    idx += increment
    print(f'idx:{idx} P:{puzzle_input}')
