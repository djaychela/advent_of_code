import os
from itertools import permutations

path = os.path.join(os.getcwd(), "data", "input_7a.txt")
with open(path, "r") as f:
    data = f.readlines()

puzzle_input = [int(d) for d in data[0].split(",")]


def run_intcodes(loc_puzzle_input, loc_input_values, debug=False):
    def get_data(index, mode):
        if mode == "0":
            return loc_puzzle_input[loc_puzzle_input[index]]
        else:
            return loc_puzzle_input[index]

    def get_index(index, mode):
        if mode == "0":
            return loc_puzzle_input[index]
        else:
            return index

    idx = 0
    output_value = 0
    if debug:
        print(f"idx:{idx} P:{loc_puzzle_input}")
    while idx < len(loc_puzzle_input) - 1:
        modes = f"{loc_puzzle_input[idx]:0>5}"
        mode_a = modes[2]
        mode_b = modes[1]
        mode_c = modes[0]
        opcode = modes[3:]
        if debug:
            print(f"current opcode: {opcode}")
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
            input_value = loc_input_values.pop()
            if debug:
                print(
                f"Opcode {opcode}: idx{idx}: Altered {loc_puzzle_input[a]} at {a} to {input_value}"
            )
            loc_puzzle_input[a] = input_value
            increment = 2

        elif opcode == "04":
            a = get_index(idx + 1, mode_a)
            increment = 2
            if debug: 
                print(f"Opcode {opcode}: Output is {loc_puzzle_input[a]}")
            output_value = loc_puzzle_input[a]

        elif opcode == "05":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            if a != 0:
                increment = 0
                idx = b
            else:
                increment = 3

        elif opcode == "06":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            if debug: 
                print(f"Opcode 06: a:{a}, b:{b}")
            if a == 0:
                increment = 0
                idx = b
            else:
                increment = 3

        elif opcode == "07":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            c = get_index(idx + 3, mode_c)
            if a < b:
                loc_puzzle_input[c] = 1
            else:
                loc_puzzle_input[c] = 0
            increment = 4

        elif opcode == "08":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            c = get_index(idx + 3, mode_c)
            if a == b:
                loc_puzzle_input[c] = 1
            else:
                loc_puzzle_input[c] = 0
            increment = 4

        elif opcode == "99":
            print(f"Opcode 99: END -> outputting {output_value}")
            return output_value

        idx += increment
        # print(f"idx:{idx} P:{loc_puzzle_input}")


best_value = 0


for c in permutations([0, 1, 2, 3, 4], 5):
    intcode_output = 0
    for i in c:
        print(f"***+++ running with values {i}, {intcode_output}")
        intcode_output = run_intcodes(puzzle_input.copy(), [intcode_output, i])
    print(f"Final Output: {intcode_output}")
    if intcode_output > best_value:
        best_value = intcode_output
        best_combi = c
print(f"Best: {best_value} Combi: {best_combi}")
