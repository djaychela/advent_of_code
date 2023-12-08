from data_read import read_file

maps = read_file("08.txt")

map_dict = dict()

for line in maps:
    if "=" in line:
        index = line.split("=")[0].strip()
        l, r = line.split("=")[1].split(",")
        l = l.strip().strip("(")
        r = r.strip().strip(")")
        map_dict[index] = dict()
        map_dict[index]["L"] = l
        map_dict[index]["R"] = r
    elif "L" in line:
        instructions = list(line.strip().split()[0])

steps = 0
map_index = "AAA"

while True:
    if map_index == "ZZZ":
        break
    current_idx = steps % len(instructions)
    current_inst = instructions[current_idx]
    map_index = map_dict[map_index][current_inst]
    steps += 1

print(f"{steps=}")