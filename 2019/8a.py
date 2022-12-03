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

zeros = [list(layer).count('0') for layer in layers[:-1]]
ones = [list(layer).count('1') for layer in layers[:-1]]
twos = [list(layer).count('2') for layer in layers[:-1]]

lowest = zeros.index(min(zeros))

print(ones[lowest])
print(twos[lowest])

