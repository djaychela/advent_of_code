import os

path = os.path.join(os.getcwd(), "data", "input_15a.txt")
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
            if debug:
                print(f"Opcode {opcode}: Output is {value_a}")
            output_value = value_a
            return output_value, loc_puzzle_input

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
            return output_value, mem_status

        idx += increment


mem_status = puzzle_input.copy()
finished = False

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
position = [0, 0]
locations = []

while not finished:
    instructions = input("droid command [1-4], (V)iew: ")
    try:
        instructions = int(instructions)
        if 0 < instructions < 5:
            droid_output, mem_status = run_intcodes(
                mem_status, [instructions], relative_base, debug=False
            )
            if droid_output == 0:  # wall ahead
                wall_loc = [0, 0]
                wall_loc[0] = position[0] + dirs[instructions - 1][0]
                wall_loc[1] = position[1] + dirs[instructions - 1][1]
                if [wall_loc.copy(), "#"] not in locations:
                    locations.append([wall_loc.copy(), "#"])
            if droid_output == 1:
                position[0] += dirs[instructions - 1][0]
                position[1] += dirs[instructions - 1][1]
                if [position.copy(), "."] not in locations:
                    locations.append([position.copy(), "."])
            if droid_output == 2:
                position[0] += dirs[instructions - 1][0]
                position[1] += dirs[instructions - 1][1]
                if [position.copy(), "."] not in locations:
                    locations.append([position.copy(), "2"])
                print(f"generator found at {position}")
                finished = True

    except ValueError:
        pass

    inp = [1, 2, 2, 1, 3, 4, 4, 3]
    idx = 0
    while idx < len(inp):
        droid_output, mem_status = run_intcodes(
            mem_status, [inp[idx]], relative_base, debug=False
        )
        if droid_output == 0:  # wall ahead
            wall_loc = [0, 0]
            wall_loc[0] = position[0] + dirs[inp[idx] - 1][0]
            wall_loc[1] = position[1] + dirs[inp[idx] - 1][1]
            if [wall_loc.copy(), "#"] not in locations:
                locations.append([wall_loc.copy(), "#"])
            idx += 1
        if droid_output == 1:
            position[0] += dirs[inp[idx] - 1][0]
            position[1] += dirs[inp[idx] - 1][1]
            if [position.copy(), "."] not in locations:
                locations.append([position.copy(), "."])
        if droid_output == 2:
            if [position.copy(), "."] not in locations:
                locations.append([position.copy(), "2"])
            finished = True
        idx += 1

    # print(locations)
    y_max = 0
    y_min = 0
    x_max = 0
    x_min = 0

    # find size of grid
    for loc in locations:
        x = loc[0][0]
        x_max = max(x, x_max)
        x_min = min(x, x_min)
        y = loc[0][1]
        y_max = max(y, y_max)
        y_min = min(y, y_min)

    # map locations onto grid:
    visited = [[" " for _ in range(x_min, x_max + 1)] for _ in range(y_min, y_max + 1)]

    # mark out known locations
    for loc in locations:
        visited[(loc[0][1] - y_min)][(loc[0][0] - x_min)] = loc[1]

    # mark current location on map
    visited[(position[1] - y_min)][(position[0] - x_min)] = "x"

    for ydx in range(len(visited) - 1, -1, -1):
        print("".join(visited[ydx]))

    print(f"Current Location: {position}")
print(locations)
