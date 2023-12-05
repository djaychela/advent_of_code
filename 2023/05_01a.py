from data_read import read_file

""" Second Attempt - stores the mappings and only works through for each 'path' needed through them.  
Adaptation of the first code attempt."""

almanac = read_file("05.txt")

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
locations = []

almanac_list = [
    seeds,
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location
]

data_idx = 0
for line in almanac:
    print(f"{data_idx=}")
    if line == "\n":
        data_idx += 1
        data_jdx = 0
    else:
        if data_idx == 0:
            almanac_list[data_idx] = list(map(int, line.strip().split(":")[1].strip().split()))
        else:
            if ":" in line:
                pass
            else:
                dest, source, num_range = list(map(int, line.strip().split(" ")))
                almanac_list[data_idx].append([dest, source, num_range])

def map_lookup(index, value):
    current_map = almanac_list[index]
    for mapping in current_map:
        if value in range(mapping[1], mapping[1] + mapping[2]):
            return mapping[0] + (value - mapping[1])
    else:
        return value

# print(almanac_list)

dest_list = []

for seed in almanac_list[0]:
    print(f"{seed=}")
    value = seed
    for idx in range(1, 8):
        dest = map_lookup(idx, value)
        value = dest
    print(dest)
    dest_list.append(dest)

print(min(dest_list))
