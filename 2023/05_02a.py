from data_read import read_file

# An attempt to work backwards from location to seed to try to be intelligent about brute forcing this.
# Not successful, so I've walked away for today.

almanac = read_file("05_test.txt")

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
        if value in range(mapping[0], mapping[0] + mapping[2]):
            return mapping[1] + (value - mapping[0])
    else:
        if index != 0:
            return value
        else:
            return False

dest_list = []

lowest_dest = 999999999999999

# work backwards
# see if this equates to a seed

sorted_locations = sorted(almanac_list[7], key=lambda x: x[1])
sorted_locations = [[0,0,100]]
for location in sorted_locations:
    # print("new loc")
    for test_location in range(location[1], location[1] + location[2]):
        print(f"{test_location=}")
        value = test_location
        for idx in range(7, 0, -1):
            dest = map_lookup(idx, value)
            # print(f"{dest=}")
            value = dest
        print(f"Seed: {value}")
        # check to see if value in given range

