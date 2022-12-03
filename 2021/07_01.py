from functools import lru_cache
from tqdm import tqdm

from data_read import read_file

crabs = read_file("07.txt")

crabs = [int(fish) for fish in crabs[0].strip().split(",")]

@lru_cache(maxsize=2000)
def calc_fuel_used(distance):
    current_fuel = sum([f for f in range(distance + 1)])
    return current_fuel

mode = 2
most = max(crabs)
least = min(crabs)
lowest_fuel_use = float("inf")
lowest_fuel_pos = 0
for poss in tqdm(range(least, most + 1)):
    if mode == 1:
        fuel_used = sum([abs(crab - poss)for crab in crabs])
    else:
        fuel_used = sum([calc_fuel_used(abs(crab - poss)) for crab in crabs])
    if fuel_used < lowest_fuel_use:
        lowest_fuel_use = fuel_used
        lowest_fuel_pos = poss

print(f"Lowest Used: {lowest_fuel_use}, position: {lowest_fuel_pos}")