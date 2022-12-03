"""Went back to a recursive function-based version for V4.  Finally got it working in the end.
Never again."""

from math import prod
from data_read import read_file

bits = read_file("16.txt")


def hex_convert_to_bin(input):
    return "".join([str(bin(int(bit, 16))[2:].zfill(4)) for bit in input.strip()])


def read_literal_value(input_string):
    idx = 0
    done = False
    number = ""
    while not done:
        current_value = input_string[idx : idx + 5]
        number += current_value[1:]
        if current_value[0] == "0":
            done = True
        idx += 5
    return idx, int(number, 2)


def parse_packet(bits):

    operators = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: x[0] > x[1],
    6: lambda x: x[0] < x[1],
    7: lambda x: x[0] == x[1],
    }

    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)

    idx = 6
    if type_id == 4:
        delta, n = read_literal_value(bits[idx:])
        return version, n, idx + delta
    else:
        res = version
        nums = []

        if bits[idx] == "0":
            len_subpackets = int(bits[idx + 1 : idx + 16], 2)
            idx += 16
            parse_until = idx + len_subpackets

            while idx < parse_until:
                value, number, delta = parse_packet(bits[idx:])
                idx += delta
                res += value
                nums.append(number)
        else:
            n_subpackets = int(bits[idx + 1 : idx + 12], 2)
            idx += 12
            while n_subpackets > 0:
                value, number, delta = parse_packet(bits[idx:])
                idx += delta
                res += value
                nums.append(number)
                n_subpackets -= 1

        return res, operators[type_id](nums), idx


for bit in bits:
    part1, part2, idx = parse_packet(hex_convert_to_bin(bit))
    print(f"{bit} : {part1=}")
    print(f"{bit} : {part2=}")
