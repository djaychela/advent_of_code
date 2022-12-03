import os

path = os.path.join(os.getcwd(), "data", "input_8a.txt")
with open(path, "r") as f:
    data = f.readlines()

puzzle_input = data[0]

width = 25
height = 6

layers = []

for c in range(0, len(puzzle_input), (width * height)):
    layers.append(puzzle_input[c : c + (width * height)])

layers=layers[:-1]

image = [[0 for _ in range(width)] for _ in range(height)]

for layer in layers[::-1]:
    w = 0
    h = 0
    for l in layer:
        if l == '1':
            image[h][w] = 'W'
        elif l == '0':
            image[h][w] = ' '
        w += 1
        if w == width:
            w = 0
            h += 1

for i in image:
    print(''.join(i))



