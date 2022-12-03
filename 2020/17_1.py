from collections import defaultdict
import pathlib
import copy

file_name = "17.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    starting = [list(cube.strip()) for cube in file.readlines()]

cube_size = 17

def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, type))

def generate_blank_cube(size):
    blank_cube = nested_dict(3, dict)
    ptr = (size - 1) // 2
    for dx in range(-ptr, ptr + 1):
        for dy in range(-ptr, ptr + 1):
            for dz in range(-ptr, ptr + 1):
                blank_cube[dx][dy][dz] = "."
    return blank_cube

def load_cube_data(cube, data, size):
    if size % 2 == 0:
        ptr_a = -(size // 2)
        ptr_b = size // 2
    else:
        ptr_a = -((size - 1) // 2)
        ptr_b = (size - 1) // 2
    for idx, dx in enumerate(range(ptr_a, ptr_b)):
        for idy, dy in enumerate(range(ptr_a, ptr_b)):
            print(idx, idy)
            cube[dx][dy][0] = data[idx][idy]
    return cube

cube_dict = generate_blank_cube(cube_size)
cube_dict = load_cube_data(cube_dict, starting, len(starting))

def display_cube(cube, size):
    ptr = (size - 1) // 2
    for dz in range(-ptr, ptr + 1):
        print(f"Z={dz}")
        for dx in range(-ptr, ptr + 1):
            for dy in range(-ptr, ptr + 1):
                print(cube[dx][dy][dz], end="")
            print()

max_scan = 5
min_scan = -4

def scan_cube(sx, sy, sz, cube):
    cube_score = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if cube[sx + dx][sy + dy][sz + dz] == "#":
                    if dx == 0 and dy == 0 and dz == 0:
                        pass
                    else:
                        cube_score += 1
    return cube_score


cycle = 1
while cycle < 7:
    new_cube = generate_blank_cube(cube_size)
    temp_cube = generate_blank_cube(cube_size)
    current_cube_score = 0
    for z in range(min_scan, max_scan):
        for x in range(min_scan, max_scan):
            for y in range(min_scan, max_scan):
                cube_score = scan_cube(x, y, z, cube_dict)
                temp_cube[x][y][z] = cube_score
                if cube_dict[x][y][z] == "#":
                    if cube_score == 2 or cube_score == 3:
                        new_cube[x][y][z] = "#"
                        current_cube_score += 1
                    else:
                        new_cube[x][y][z] = "."
                if cube_dict[x][y][z] == ".":
                    if cube_score == 3:
                        new_cube[x][y][z] = "#"
                        current_cube_score += 1
                    else:
                        new_cube[x][y][z] = "."

    display_cube(new_cube, cube_size)
    print(f"Scan: {min_scan}, {max_scan}")
    print(f"Cycle: {cycle} - score {current_cube_score}")
    max_scan += 1
    min_scan -= 1
    cycle += 1
    cube_size += 2

    cube_dict = copy.deepcopy(new_cube)
