from data_read import read_file

# First Attempt.... brute force will not solve this!

almanac = read_file("05.txt")

seeds = []
seed_to_soil = dict()
soil_to_fertilizer = dict()
fertilizer_to_water = dict()
water_to_light = dict()
light_to_temperature = dict()
temperature_to_humidity = dict()
humidity_to_location = dict()
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
    else:
        if data_idx == 0:
            almanac_list[data_idx] = list(map(int, line.strip().split(":")[1].strip().split()))
        else:
            if ":" in line:
                pass
            else:
                dest, source, num_range = list(map(int, line.strip().split(" ")))
                print( dest, source, num_range)
                for idx in range(num_range):
                    almanac_list[data_idx][source + idx] = dest + idx

dest_list = []

for seed in almanac_list[0]:
    print(f"{seed=}")
    value = seed
    for idx in range(1, 8):
        try:
            dest = almanac_list[idx][value]
        except KeyError:
            dest = value
        value = dest
    print(dest)
    dest_list.append(dest)

print(min(dest_list))
