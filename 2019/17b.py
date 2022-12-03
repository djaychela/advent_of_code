import os

path = os.path.join(os.getcwd(), "data", "input_17b.txt")
with open(path, "r") as f:
    data = f.readlines()

puzzle_input = [int(d) for d in data[0].split(",")]

for _ in range(3000):
    puzzle_input.append(0)

relative_base = 0

def run_intcodes(loc_puzzle_input, loc_input_values, relative_base, debug=False):
    
    def get_data(index, mode):
        return loc_puzzle_input[get_index(index, mode)]

    def get_index(index, mode):
        if mode == "0":
            return loc_puzzle_input[index]
        elif mode == "1":
            return index
        elif mode == "2":
            return relative_base + loc_puzzle_input[index]
        else:
            return ValueError

    idx = 0
    output_value = 0
    output_values = []

    while idx < len(loc_puzzle_input) - 1:
        modes = f"{loc_puzzle_input[idx]:0>5}"
        mode_a = modes[2]
        mode_b = modes[1]
        mode_c = modes[0]
        opcode = modes[3:]
        if debug:
            print(f"idx: {idx} - current opcode: {opcode}, {modes}")
        if opcode == "01":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            c = get_index(idx + 3, mode_c)
            r = a + b
            if debug:
                print(f"Opcode {opcode}: Altered {loc_puzzle_input[c]} at {c} to {r}")
            loc_puzzle_input[c] = r
            increment = 4

        elif opcode == "02":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            c = get_index(idx + 3, mode_c)
            r = a * b
            if debug:
                print(f"Opcode {opcode}: Altered {loc_puzzle_input[c]} at {c} to {r}")
            loc_puzzle_input[c] = r
            increment = 4

        elif opcode == "03":
            a = get_index(idx + 1, mode_a)
            input_value = loc_input_values[0]
            loc_input_values = loc_input_values[1:]
            if debug:
                print(
                    f"Opcode {opcode}: idx{idx}: Altered {loc_puzzle_input[a]} at {a} to {input_value}"
                )
            loc_puzzle_input[a] = input_value
            increment = 2

        elif opcode == "04":
            value_a = get_data(idx + 1, mode_a)
            increment = 2
            if debug:
                print(f"Opcode {opcode}: Output is {value_a}")
            output_value = value_a
            output_values.append(output_value)

        elif opcode == "05":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            if a != 0:
                if debug:
                    print(f"Opcode {opcode}: {a} != 0. idx from {idx} to {b}")
                increment = 0
                idx = b
            else:
                if debug:
                    print(f"Opcode {opcode}: {a} == 0. noop")
                increment = 3

        elif opcode == "06":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            if a == 0:
                if debug:
                    print(f"Opcode {opcode}: idx from {idx} to {b}")
                increment = 0
                idx = b
            else:
                increment = 3

        elif opcode == "07":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            c = get_index(idx + 3, mode_c)
            if a < b:
                if debug:
                    print(f"Opcode {opcode}: {a} < {b}, loc {c} from {loc_puzzle_input[c]} to 1")
                loc_puzzle_input[c] = 1
            else:
                if debug:
                    print(f"Opcode {opcode}: {a} !< {b}, loc {c} from {loc_puzzle_input[c]} to 0")
                loc_puzzle_input[c] = 0
            increment = 4

        elif opcode == "08":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            c = get_index(idx + 3, mode_c)
            if a == b:
                if debug:
                    print(f"Opcode {opcode}: {a} == {b}, loc {c} from {loc_puzzle_input[c]} to 1")
                loc_puzzle_input[c] = 1
            else:
                if debug:
                    print(f"Opcode {opcode}: {a} != {b}, loc {c} from {loc_puzzle_input[c]} to 1")
                loc_puzzle_input[c] = 0
            increment = 4

        elif opcode == "09":
            a = get_data(idx + 1, mode_a)
            if debug:
                print(f'opcode 9, mode = {mode_a}, value = {a}')
            relative_base += a
            if debug:
                print(f"Relative Base now {relative_base}")
            increment = 2

        elif opcode == "99":
            print(f"Opcode 99: END -> outputting {output_value}")
            return output_values, puzzle_input

        idx += increment

def show_output(op):
    ascii_output = []

    # output:
    for o in op:
        ascii_output.append(chr(o))

    print(''.join(ascii_output))

# main routine: A,C,A,B,A,C,B,C,B,C
# A: L, 10, R, 8, L, 6, R, 6
# B: R, 8, L, 6, L, 10, L 10
# C: L, 8, L, 8, R, 8

main = [65, 44, 67, 44, 65, 44, 66, 44, 65, 44, 67, 44, 66, 44, 67, 44, 66, 44, 67, 10]
a = [76, 44, 49, 48, 44, 82, 44, 56, 44, 76, 44, 54, 44, 82, 44, 54, 10]
b = [82, 44, 56, 44, 76, 44, 54, 44, 76, 44, 49, 48, 44, 76, 44, 49, 48, 10]
c = [76, 44, 56, 44, 76, 44, 56, 44, 82, 44, 56, 10]
viz = [121,10]

instructions = main + a + b + c + viz

instructions = instructions

output, state = run_intcodes(puzzle_input, instructions, relative_base, debug=False)

