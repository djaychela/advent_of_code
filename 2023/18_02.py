
from data_read import read_file
from PIL import Image
import numpy as np


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
hex_directions = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U"
}

def shoelace_formula_3(x, y, absoluteValue = True):

    result = 0.5 * np.array(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    if absoluteValue:
        return abs(result)
    else:
        return result
    
for line in dig_inst_raw:
    direction, distance, colour = line.strip().split(" ")
    distance = int(colour.strip("()#")[:5], 16)
    direction = hex_directions[colour.strip("()#")[-1]]
    colour = colour.strip("()#")
    # print(direction, distance, colour)
    dig_inst.append((direction, distance, colour))

line_length = 0
for inst in dig_inst:
    for idx in range(inst[1]):
        move = directions[inst[0]]
        location[0] += move[0]
        location[1] += move[1]
        line_length += 1
    ground.append((location[0], location[1]))
    
x,y = zip(*ground)
area = (shoelace_formula_3(x, y)) + (line_length + 2) / 2
print(int(area))