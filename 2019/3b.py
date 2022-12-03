import os

file_path = os.path.join(os.getcwd(), 'data', 'input3a.txt')

with open(file_path, 'r') as f:
    d1 = f.readline().rstrip().split(',')
    d2 = f.readline().rstrip().split(',')

data_1 = [(d[0], int(d[1:])) for d in d1]
data_2 = [(d[0], int(d[1:])) for d in d2]

locs_1 = [[0,0]]
locs_2 = [[0,0]]

def convert_to_coords(instructions):
    locs = [[0,0]]
    loc = [0,0]
    for data in instructions:
        if data[0] == "R":
            idx = 0
            inc = +1
        elif data[0] == "L":
            idx = 0
            inc = -1
        elif data[0] == "U":
            idx = 1
            inc = +1
        else:
            idx = 1
            inc = -1
        for _ in range(data[1]):
            loc[idx] += inc
            locs.append(loc.copy())
    return locs
print('converting 1')
route_1 = convert_to_coords(data_1)
print(f'converted - length is {len(route_1)}')
print('converting 2')
route_2 = convert_to_coords(data_2)
print(f'converted - length is {len(route_2)}')

print('finding minimum')
minimum_distance = 1000000000
for idx, element_i in enumerate(route_1[1:],1):
    if idx %1000 == 0:
        print(f'comparing {idx} - current minimum: {minimum_distance}')
    for jdx, element_j in enumerate(route_2[1:],1):
        if element_i == element_j:
            print(f'Intersection found at i={idx}, j={jdx}')
            minimum_distance = min((idx+jdx), minimum_distance)
            print(f'Current Minimum: {minimum_distance}')

print(minimum_distance)