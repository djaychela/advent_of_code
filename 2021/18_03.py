from copy import deepcopy
from math import floor, ceil
from time import time

def read_lines():
    with open("data/18_test.txt") as f:
        return f.read().splitlines()


def parse_line(line):
    elements = filter(lambda element: element != ',', line)
    elements = list(map(lambda element: int(element) if element.isdigit() else element, elements))
    return elements

def display(elements):
    for ele in elements:
        if isinstance(ele, int):
            print(f"{ele},", end="")
        else:
            print(f"{ele}", end="")
    print()

def explode(elements, opening_bracket_index):
    left_number = elements[opening_bracket_index + 1]
    right_number = elements[opening_bracket_index + 2]

    for i in range(opening_bracket_index - 1, 0, -1):
        if isinstance(elements[i], int):
            elements[i] += left_number
            break

    for i in range(opening_bracket_index + 4, len(elements)):
        if isinstance(elements[i], int):
            elements[i] += right_number
            break

    return elements[:opening_bracket_index] + [0] + elements[opening_bracket_index + 4:]


def try_to_explode(elements):
    open_brackets = 0
    for i in range(len(elements)):
        if open_brackets == 4 and elements[i] == '[':
            elements = explode(elements, i)
            display(elements)
            return True, elements
        elif elements[i] == '[':
            open_brackets += 1
        elif elements[i] == ']':
            open_brackets -= 1
    return False, elements


def try_to_split(elements):
    for i in range(len(elements)):
        if isinstance(elements[i], int) and elements[i] >= 10:
            elements[i:i + 1] = ['[', floor(elements[i] / 2), ceil(elements[i] / 2), ']']
            return True, elements
    return False, elements


def reduce_elements(elements):
    has_reduced = True
    while has_reduced:
        has_reduced, elements = try_to_explode(elements)
        if not has_reduced:
            has_reduced, elements = try_to_split(elements)

    return elements


def calculate_magnitude(elements, index=0):
    if isinstance(elements[index], int):
        return elements[index], index

    left_sum, index = calculate_magnitude(elements, index + 1)
    right_sum, index = calculate_magnitude(elements, index + 1)

    return 3 * left_sum + 2 * right_sum, index + 1


def part_1():
    lines = read_lines()
    elements = list(map(parse_line, lines))
    result = elements[0]
    for i in range(1, len(elements)):
        result = ['['] + result + elements[i] + [']']
        result = reduce_elements(result)
    
    return calculate_magnitude(result)[0]


def part_2():
    lines = read_lines()
    elements = list(map(parse_line, lines))

    max_magnitude = 0
    for element1 in elements:
        for element2 in elements:
            if element1 == element2:
                continue
            added_element = ['['] + deepcopy(element1) + deepcopy(element2) + [']']
            added_element = reduce_elements(added_element)
            magnitude = calculate_magnitude(added_element)[0]
            if magnitude > max_magnitude:
                max_magnitude = magnitude
    return max_magnitude


if __name__ == "__main__":
    start = time()
    result_part_1 = part_1()
    end = time()
    print(f'Part 1 ran in {round(end - start, 2)} seconds and the result is {result_part_1}')
    exit()
    start = time()
    result_part_2 = part_2()
    end = time()
    print(f'Part 2 ran in {round(end - start, 2)} seconds and the result is {result_part_2}')
