from data_read import read_file
from PIL import Image

import sys
sys.setrecursionlimit(50000)

dig_inst_raw = read_file("18.txt")

dig_inst = []
ground = []
location = [0, 0]
directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

def get_bounds(ground):
    low_y = 999999999999999
    high_y = -99999999999999
    low_x = 999999999999999
    high_x = -99999999999999
    for g in ground:
        low_y = min(low_y, g[0])
        high_y = max(high_y, g[0])
        low_x = min(low_x, g[1])
        high_x = max(high_x, g[1])
    
    return (low_y, high_y, low_x, high_x)

def display_ground(ground):
    low_y, high_y, low_x, high_x = get_bounds(ground)
    y_size = (high_y - low_y) + 20
    x_size = (high_x - low_x) + 20

    img = Image.new( 'RGB', (x_size, y_size), "black")
    pixels = img.load()
    locations = [(g[0], g[1]) for g in ground]
    for ydx in range(low_y, high_y + 1):
        current_line = []
        for xdx in range(low_x, high_x + 1):
            if (ydx, xdx) in locations:
                idx = locations.index((ydx, xdx))
                colour = tuple(int(ground[idx][2].strip("#")[i:i+2], 16) for i in (0, 2, 4))
                pixels[10 + xdx - low_x, 10 + ydx - low_y] = colour

    img.show()

def flood_recursive(ground):
    low_y, high_y, low_x, high_x = get_bounds(ground)
    locations = [(g[0], g[1]) for g in ground]
    def fill(x,y,color_to_update):
        if (y, x) in locations:
            return
        else:
            ground.append((y, x, color_to_update))
            locations.append((y, x))
            neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            for n in neighbors:
                if low_x <= n[0] <= high_x and low_y <= n[1] <= high_y:
                    fill(n[0],n[1],color_to_update)
    start_x = 1
    start_y = 1
    fill(start_x,start_y, "#ff0000")
    return ground

for line in dig_inst_raw:
    direction, distance, colour = line.strip().split(" ")
    distance = int(distance)
    colour = colour.strip("()")
    dig_inst.append((direction, distance, colour))


for inst in dig_inst:
    for idx in range(inst[1]):
        move = directions[inst[0]]
        location[0] += move[0]
        location[1] += move[1]
        ground.append((location[0], location[1], inst[2]))

display_ground(ground)
ground = flood_recursive(ground)
print(len(ground))
display_ground(ground)

