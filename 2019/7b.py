import os
from itertools import permutations

path = os.path.join(os.getcwd(), "data", "test_7b_1.txt")
with open(path, "r") as f:
    data = f.readlines()

puzzle_input = [int(d) for d in data[0].split(",")]
print(puzzle_input)


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
            # loc_input_values.append(output_value)
            return output_value, loc_puzzle_input

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
        # print(loc_input_values)

best_value = 0

# for c in permutations([5, 6, 7, 8, 9], 5):
c = [9, 8, 7, 6, 5] # should produce 139629729.
phase_sent = [False, False, False, False, False]
amp_inputs = [0, 0, 0, 0, 0]
amplifiers = [puzzle_input.copy(), puzzle_input.copy(), puzzle_input.copy(), puzzle_input.copy(), puzzle_input.copy()]
running = True
amp_idx = 0
while running:
    if phase_sent[amp_idx]:
        print(f"running {amp_idx}:-")
        print(f"sending {[amp_inputs[amp_idx]]}")
        amp_output, amp_status = run_intcodes(amplifiers[amp_idx], [amp_inputs[amp_idx]])
    else:
        print(f"running {amp_idx} for the first time:")
        print(f"sending {[c[amp_idx], amp_inputs[amp_idx]]}")
        amp_output, amp_status = run_intcodes(amplifiers[amp_idx], [c[amp_idx], amp_inputs[amp_idx]])
        phase_sent[amp_idx] = True
    # check for completion of amp
    if amp_idx <=3:
        amp_inputs[amp_idx + 1] = amp_output
    else:
        amp_inputs[0] = amp_output
    amplifiers[amp_idx] = amp_status.copy()
    amp_idx += 1
    if amp_idx > 4:
        amp_idx = 0

