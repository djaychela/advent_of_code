import os
from time import sleep

path = os.path.join(os.getcwd(), "data", "input_11a.txt")
with open(path, "r") as f:
    data = f.readlines()

puzzle_input = [int(d) for d in data[0].split(",")]

for _ in range(3000):
    puzzle_input.append(0)

relative_base = 0


def run_intcodes(loc_puzzle_input, loc_input_values, relative_base, debug=False):

    output_pair = []

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
            input_value = loc_input_values.pop()
            if debug:
                print(
                    f"Opcode {opcode}: idx{idx}: Altered {loc_puzzle_input[a]} at {a} to {input_value}"
                )
            loc_puzzle_input[a] = input_value
            increment = 2

        elif opcode == "04":
            value_a = get_data(idx + 1, mode_a)
            increment = 2
            # if debug:
            print(f"Opcode {opcode}: Output is {value_a}")
            output_value = value_a
            output_pair.append(output_value)
            if len(output_pair) == 2:
                return output_pair, loc_puzzle_input

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
                    print(
                        f"Opcode {opcode}: {a} < {b}, loc {c} from {loc_puzzle_input[c]} to 1"
                    )
                loc_puzzle_input[c] = 1
            else:
                if debug:
                    print(
                        f"Opcode {opcode}: {a} !< {b}, loc {c} from {loc_puzzle_input[c]} to 0"
                    )
                loc_puzzle_input[c] = 0
            increment = 4

        elif opcode == "08":
            a = get_data(idx + 1, mode_a)
            b = get_data(idx + 2, mode_b)
            c = get_index(idx + 3, mode_c)
            if a == b:
                if debug:
                    print(
                        f"Opcode {opcode}: {a} == {b}, loc {c} from {loc_puzzle_input[c]} to 1"
                    )
                loc_puzzle_input[c] = 1
            else:
                if debug:
                    print(
                        f"Opcode {opcode}: {a} != {b}, loc {c} from {loc_puzzle_input[c]} to 1"
                    )
                loc_puzzle_input[c] = 0
            increment = 4

        elif opcode == "09":
            a = get_data(idx + 1, mode_a)
            if debug:
                print(f"opcode 9, mode = {mode_a}, value = {a}")
            relative_base += a
            if debug:
                print(f"Relative Base now {relative_base}")
            increment = 2

        elif opcode == "99":
            print(f"Opcode 99: END -> outputting {output_value}")
            return output_value, ["END"]

        idx += increment


locations_visited = {}
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
location = [0, 0]
orientation = 0
done = False
int_input = 0
current_status = puzzle_input.copy()
while not done:
    output, current_status = run_intcodes(
        current_status, [int_input], relative_base, debug=False
    )
    if current_status[0] == "END":
        done = True
        break

    # store colour in current location
    colour, turn = output[0], output[1]
    loc_index = location[0]*1000 + location[1]
    locations_visited[loc_index] = colour
    # turn robot
    if turn == 0:
        turn = -1
    orientation += turn
    if orientation < 0:
        orientation = 3
    if orientation > 3:
        orientation = 0
    location[0] += directions[orientation][0]
    location[1] += directions[orientation][1]

    # check for current location's value
    loc_index = location[0]*1000 + location[1]
    if loc_index in locations_visited.keys():
        int_input = locations_visited[loc_index]
    else:
        int_input = 0

    print(f"Current location: {location} - input: {int_input}, c:{colour}, t: {turn}")
    sleep(1)

    

