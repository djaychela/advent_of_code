import time

from data_read import read_file

binary = read_file("03.txt")


def load_digits():
    digits = []
    for bin in binary:
        for idx, digit in enumerate(bin.strip()):
            try:
                digits[idx].append(int(digit))
            except IndexError:
                digits.append([int(digit)])
    return digits


def remove_numbers(digit_to_delete, location):
    for l_index in range(len(digits[0])):
        if digits[location][l_index] == digit_to_delete:
            for jdx in range(len(digits)):
                digits[jdx][l_index] = "x"


def count_valid(digits):
    total = 0
    for idx in range(len(digits[0])):
        if digits[0][idx] != "x":
            total += 1

    return total


def print_nicely(digits):
    return_value = ""
    for idx in range(len(digits[0])):
        output = ""
        for jdx in range(len(digits)):
            output += str(digits[jdx][idx])
        if output[0] != "x":
            print(output)
            return_value = output
    return return_value


def locate_rating(mode):
    index = 0
    while index < len(digits):
        digit = digits[index]
        zeros = digit.count(0)
        ones = digit.count(1)
        valid = count_valid(digits)
        print(f"**** VALID: {valid}")
        if valid == 1:
            break
        if zeros > ones and zeros > 1:
            if mode == 1:
                print(f"{index = } - removing ones")
                remove_numbers(1, index)
            else:
                print(f"{index = } - removing zeros")
                remove_numbers(0, index)
            print_nicely(digits)
        elif ones > zeros and ones > 1:
            if mode == 1:
                print(f"{index = } - removing zeros")
                remove_numbers(0, index)
            else:
                print(f"{index = } - removing ones")
                remove_numbers(1, index)
            print_nicely(digits)
        else:
            if mode == 1:
                print(f"{index = } - keeping ones")
                remove_numbers(0, index)
            else:
                print(f"{index = } - keeping zeros")
                remove_numbers(1, index)
            print_nicely(digits)

        index += 1
    return digits


digits = load_digits()
oxygen = locate_rating(1)
digits = load_digits()
co2 = locate_rating(0)
print("**** OXYGEN ****")
oxygen_value = print_nicely(oxygen)
print("**** CO2 ****")
co2_value = print_nicely(co2)
print(
    f"Answer: {int(oxygen_value,2)} * {int(co2_value,2)} = {int(oxygen_value,2) * int(co2_value,2)} "
)
