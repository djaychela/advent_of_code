from data_read import read_file

# Brute Force Also Not working here...

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
    # print(f"{data_idx=}")
    if line == "\n":
        data_idx += 1
        data_jdx = 0
    else:
        if data_idx == 0:
            seed_data = list(map(int, line.strip().split(":")[1].strip().split()))
            final_seed_data = []
            for idx in range(0, len(seed_data), 2):
                final_seed_data.append((seed_data[idx], seed_data[idx + 1]))
            almanac_list[data_idx] = final_seed_data
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

dest_list = []

lowest_dest = 999999999999999

for seed in almanac_list[0]:
    print(f"{seed=}")
    for sdx in range(seed[0], seed[0] + seed[1]):
        value = sdx
        for idx in range(1, 8):
            dest = map_lookup(idx, value)
            value = dest
        lowest_dest = min(lowest_dest, value)

print(lowest_dest)
