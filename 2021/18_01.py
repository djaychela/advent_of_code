import enum
import re
from data_read import read_file
from pyparsing import nestedExpr, stringEnd
import re
from math import ceil


def parse(line):
    expanded = re.findall(r"\d+|[\[\]]", line)
    return [int(exp) if exp not in ["[", "]"] else exp for exp in expanded]


def find_left_bracket(idx):
    while idx > 0:
        if hw[idx] != "[":
            idx -= 1
        else:
            return idx
    return None


def find_left_num(idx):
    idx -= 1
    while idx > 0:
        if isinstance(hw[idx], int):
            return idx
        else:
            idx -= 1
    return None

def find_curr_num(idx):
    while idx < len(hw):
        if isinstance(hw[idx], int):
            return idx
        else:
            idx += 1
    return None


def find_right_bracket(idx):
    while idx < len(hw):
        if hw[idx] != "]":
            idx += 1
        else:
            return idx
    return None

def find_deepest_bracket(hw):
    depth = 0
    max_depth = 0
    max_idx = 0
    for idx, element in enumerate(hw):
        if element == "[":
            depth += 1
        elif element == "]":
            depth -= 1
        if depth > max_depth:
            max_depth = depth
            max_idx = idx
    return max_depth, max_idx


def find_right_num(idx):
    idx += 2
    while idx < len(hw):
        if hw[idx] not in ["[", "]"]:
            return idx
        else:
            idx += 1
    return None


def find_next_num(idx):
    idx += 1
    while idx < len(hw):
        if hw[idx] not in ["[", "]"]:
            return idx
        else:
            idx += 1
    return None


def display_hw(elements):
    output = ""
    for ele in elements:
        if isinstance(ele, int):
            output += f"{ele},"
        else:
            output += f"{ele}"
    return output


def explode(idx, hw):
    idx += 1
    cn_idx = find_curr_num(idx)
    lb_idx = find_left_bracket(cn_idx)
    rb_idx = find_right_bracket(cn_idx)
    ln_idx = find_left_num(cn_idx)
    rn_idx = find_right_num(cn_idx)
    nn_idx = find_next_num(cn_idx)
    print(f"{cn_idx=}, {lb_idx=}, {rb_idx=}, {ln_idx=}, {rn_idx=}, {nn_idx=}, {idx=}")
    for item in [
        ["cn_idx", cn_idx],
        ["lb_idx", lb_idx],
        ["rb_idx", rb_idx],
        ["ln_idx", ln_idx],
        ["rn_idx", rn_idx],
        ["nn_idx", nn_idx],
        ["idx", idx],
    ]:
        try:
            print(f"{item[0]} => {hw[item[1]]}")
        except TypeError:
            print(f"{item[0]} => {item[1]}")
    if ln_idx:
        left_sum = hw[cn_idx] + hw[ln_idx]
    else:
        left_sum = 0
    if rn_idx:
        right_sum = hw[nn_idx] + hw[rn_idx]
    else:
        right_sum = 0
    print(f"{left_sum=}, {right_sum=}")
    if ln_idx:
        hw[ln_idx] = left_sum
    else:
        # change index to suit removal
        rb_idx += 1
        # pass
    if rn_idx:
        hw[rn_idx] = right_sum
    else:
        rb_idx += 1
        # pass
    try:
        if rn_idx - rb_idx > 1:
            rb_idx += 1
    except TypeError:
        pass
    print(f"{lb_idx=}, {rb_idx=}, {ln_idx=}, {rn_idx=}, {nn_idx=}, {idx=}")
    print(display_hw(hw))
    pulled = hw.pop(lb_idx)
    while pulled != "]":
        print(f"Removed {pulled}")
        pulled = hw.pop(lb_idx)
        # rb_idx -= 1
    print(f"Removed {pulled}")

    hw.insert(lb_idx, 0)

    return hw


def split(idx, hw):
    num_1 = hw[idx] // 2
    num_2 = ceil(hw[idx] / 2)
    _ = hw.pop(idx)
    for ins in ["]", num_2, num_1, "["]:
        hw.insert(idx, ins)
    return hw


def detect_first_split(hw):
    for idx, element in enumerate(hw):
        try:
            num = int(element)
        except ValueError:
            num = 0
        if num >= 10:
            return idx, True
    return len(hw), False


def detect_explode(hw):
    count = 0
    for idx, item in enumerate(hw):
        if hw[idx] == "[":
            count += 1
            if count >= 5:
                if hw[idx + 3] == "]":
                    return idx - 1, True
        if hw[idx] == "]":
            count -= 1

    return len(hw), False

def reduce_homework(hw):
    explode_idx, explode_go = detect_explode(hw)
    first_split_idx, split_go = detect_first_split(hw)
    while split_go or explode_go:
        print(f"{explode_idx=}, {first_split_idx=}")
        if explode_go:
            print(f"Exploding... {display_hw(hw)}")
            hw = explode(explode_idx, hw)
            print(f"Exploded.... {display_hw(hw)}")
        elif split_go:
            print(f"Splitting... {display_hw(hw)}")
            hw = split(first_split_idx, hw)
            print(f"Split....... {display_hw(hw)}")

        explode_idx, explode_go = detect_explode(hw)
        first_split_idx, split_go = detect_first_split(hw)
        print(f"{explode_idx=}, {first_split_idx=}")

    return hw

def calculate_magnitude(hw, idx):
    magnitude = (3 * hw[idx]) + (2 * hw[idx+ 1])
    for i in range(idx -1, idx + 3):
        _ = hw.pop(idx - 1)
    hw.insert(idx-1, magnitude)
    return hw


def calculate_overall_magnitude(hw):
    complete = False
    while not complete:
        depth, idx = find_deepest_bracket(hw)
        if depth == 1:
            complete = True
        hw = calculate_magnitude(hw, idx + 1)

    return hw


homework = read_file("18.txt")
homework = [home.strip() for home in homework]

hw = parse(homework[0])
hw = reduce_homework(hw)

for home in homework[1:]:
    print(f"ADDING {home}")
    print(hw)
    hw.insert(0, "[")
    hw.extend(parse(home))
    hw.append("]")
    hw = reduce_homework(hw)

print("*** FINAL ***")
print(display_hw(hw))
print(calculate_overall_magnitude(hw))

