from data_read import read_file
from tqdm import tqdm
from dataclasses import dataclass, field



def inp(num_1, num_2):
    global test_value
    # print(f"{test_value=}")
    num = int(test_value[0])
    test_value = test_value[1:]
    # print(f"Entering {num}")
    return num


def add(num_1, num_2):
    return num_1 + num_2


def mul(num_1, num_2):
    return num_1 * num_2


def div(num_1, num_2):
    return int(num_1 / num_2)


def mod(num_1, num_2):
    return num_1 % num_2


def eql(num_1, num_2):
    if num_1 == num_2:
        return 1
    return 0




def run_program(program, data):
    w, x, y, z, = 0, 0, 0, 0
    i_map = {"inp": inp, "add": add, "mul": mul, "div": div, "mod": mod, "eql": eql}
    v_map = {"w": w, "x": x, "y": y, "z": z}

    for inst in program:
        # print(f"{inst=}")
        op = i_map[inst[0]]

        try:
            v_2 = int(inst[2])
        except IndexError:
            v_2 = 0
        except ValueError:
            v_2 = inst[2]

        v_1 = v_map[inst[1]]
        match inst[1]:
            case "w":
                match v_2:
                    case "w":
                        w = op(w, w)
                    case "x":
                        w = op(w, x)
                    case "y":
                        w = op(w, y)
                    case "z":
                        w = op(w, z)
                    case _:
                        w = op(w, v_2)
            case "x":
                match v_2:
                    case "w":
                        x = op(x, w)
                    case "x":
                        x = op(x, x)
                    case "y":
                        x = op(x, y)
                    case "z":
                        x = op(x, z)
                    case _:
                        x = op(x, v_2)
            case "y":
                match v_2:
                    case "w":
                        y = op(y, w)
                    case "x":
                        y = op(y, x)
                    case "y":
                        y = op(y, y)
                    case "z":
                        y = op(y, z)
                    case _:
                        y = op(y, v_2)
            case "z":
                match v_2:
                    case "w":
                        z = op(z, w)
                    case "x":
                        z = op(z, x)
                    case "y":
                        z = op(z, y)
                    case "z":
                        z = op(z, z)
                    case _:
                        z = op(z, v_2)
        # print(op, v_1, v_2)
        # print(f"{v_1}:{v_1=}, {id(v_1)}")
        # # print(id(op), id(v_1), id(v_2))
        # print(f"{w=}, {x=}, {y=}, {z=}")
    return (w, x, y, z)

program = [inst.strip().split() for inst in read_file("24_test_2.txt")]
value = 99

running = True
while running:
    test_value = str(value)
    print(f"Testing {test_value}")
    result = run_program(program, test_value)
    print(result)
    if result[3] == 0:
        running = False

    value -= 1
    if value <10:
        running = False

print(f"Highest Value = {value + 1}")