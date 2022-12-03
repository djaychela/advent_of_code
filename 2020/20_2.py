import pathlib
from itertools import combinations

file_name = "20_test.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    tiles = [tile.strip() for tile in file.readlines()]

sea_monster = ["                  #", 
                "#    ##    ##    ###",
                " #  #  #  #  #  #   "]

tile_dict = {}
for tile_idx in range(0,len(tiles), 12):
    tile_id = tiles[tile_idx].split()[1][:-1]
    print(tile_id)
    top = tiles[tile_idx + 1]
    bottom = tiles[tile_idx + 10]
    left = "".join([tiles[tile_idx + jdx][0] for jdx in range(1,11)])
    right = "".join([tiles[tile_idx + jdx][9] for jdx in range(1,11)])
    edges = [top, bottom, left, right]
    tile_dict[tile_id] = edges

match_dict = {}

for tile_id in tile_dict.keys():
    match_total = 0
    for check_id in tile_dict.keys():
        if tile_id == check_id:
            continue
        for tile_side in tile_dict[tile_id]:
            for check_side in tile_dict[check_id]:
                if tile_side == check_side or tile_side == check_side[::-1]:
                    match_total += 1
                    # store which tile this matched with, and which way round
    match_dict[tile_id] = match_total

# somehow work out how to stitch these all together
# magic
# search for the sea monster

total = 1
for k, v in match_dict.items():
    if v == 2:
        total *= int(k)

print(total)
