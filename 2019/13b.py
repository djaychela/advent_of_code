import os
from time import sleep

path = os.path.join(os.getcwd(), "data", "input_13b.txt")
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
            try:
                input_value = loc_input_values.pop()
            except IndexError:
                input_value = 0
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
            output_values.append(value_a)

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
            print(f"Opcode 99: END -> outputting list of values")
            return output_values, loc_puzzle_input

        idx += increment


screen_data, mem_state = run_intcodes(puzzle_input, [0], relative_base, debug=False)

# find area of screen
x_coords = screen_data[::3]
y_coords = screen_data[1::3]

score = -1

finished = False

while not finished:
    # 0 is an empty tile. No game object appears in this tile.
    # 1 is a wall tile. Walls are indestructible barriers.
    # 2 is a block tile. Blocks can be broken by the ball.
    # 3 is a horizontal paddle tile. The paddle is indestructible.
    # 4 is a ball tile. The ball moves diagonally and bounces off objects.

    screen = [[0 for _ in range(max(x_coords) + 1)] for _ in range(max(y_coords) + 1)]

    # write data to screen
    for idx in range(0, (len(screen_data) - 3), 3):
        x = screen_data[idx]
        y = screen_data[idx + 1]
        v = screen_data[idx + 2]
        if x >= 0:
            screen[y][x] = v
        elif x == -1:
            score = v

    # screen display + count non-zero:
    total = 0
    finished = True
    for ydx in range(len(screen)):
        for xdx in range(len(screen[0])):
            output = screen[ydx][xdx]
            if output == 2:
                finished = False
            print(output, end="")
        print("")

    print(f"Score: {score}")

    screen_data, mem_state = run_intcodes(mem_state, [0], relative_base, debug=False)
