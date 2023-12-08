from data_read import read_file
from math import lcm

maps = read_file("08.txt")

map_dict = dict()

starting_locations = dict()

for line in maps:
    if "=" in line:
        index = line.split("=")[0].strip()
        if index[2] == "A":
            starting_locations[index] = [0, index]
        l, r = line.split("=")[1].split(",")
        l = l.strip().strip("(")
        r = r.strip().strip(")")
        map_dict[index] = dict()
        map_dict[index]["L"] = l
        map_dict[index]["R"] = r
    elif "L" in line:
        instructions = list(line.strip().split()[0])

def find_next_z(steps, starting_index):
    step_start = steps
    map_index = starting_index
    print(f"Starting for {steps=}, {starting_index=}")
    while True:
        if map_index[2] == "Z" and steps != step_start:
            break
        current_idx = steps % len(instructions)
        current_inst = instructions[current_idx]
        map_index = map_dict[map_index][current_inst]
        steps += 1

    print(f"{starting_index=}: {steps=}, {map_index=}")
    return steps, map_index

def get_current_steps(starting_index):
    return [v[0] for k,v in starting_index.items()]

def get_current_minimum(starting_locations):
    minimum = 99999999999999
    min_key = None
    for k,v in starting_locations.items():
        if v[0] < minimum:
            minimum = v[0]
            min_key = k
    return min_key 

complete = False
counter = 1

while not complete:
    current_follow = get_current_minimum(starting_locations)
    starting_locations[current_follow] = find_next_z(starting_locations[current_follow][0], starting_locations[current_follow][1])
    current_steps = set(get_current_steps(starting_locations))
    if len(current_steps) == 1:
        complete = True
    counter += 1
    if counter > len(starting_locations.keys()):
        break

steps_taken = get_current_steps(starting_locations)
print(lcm(*steps_taken))

