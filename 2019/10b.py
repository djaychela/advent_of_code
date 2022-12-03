import os
from math import sqrt, asin, degrees

path = os.path.join(os.getcwd(), "data", "input_10a.txt")
with open(path, "r") as f:
    data = f.readlines()

puzzle_data = [d.rstrip() for d in data]

print(puzzle_data)
width = len(puzzle_data[0])
height = len(puzzle_data)
print(width, height)
lasers = {}

# position of laser
loc_w = 8
loc_h = 16

for w in range(width):
    for h in range(height):
        if loc_w == w and loc_h == h:
            continue
        if puzzle_data[h][w] == '#': 
            print(f'laser to ({h},{w}):')
            a = h - loc_h
            b = w - loc_w
            c = sqrt((a ** 2) + (b ** 2))
            sin_val = abs(round(degrees(asin(b / c)), 8))
            if a == abs(a):
                if b!= abs(b):
                    # print('a+b-')
                    sin_val = 180 + sin_val
                else:
                    # print('a+b+')
                    sin_val = 180 - sin_val
            else:
                if b != abs(b):
                    # print('a-b-')
                    sin_val = 360 - sin_val
                else:
                    # print('a-b+')
                    sin_val = sin_val
            if sin_val == 360:
                sin_val = 0

            print(f"to ({h}, {w}):{round(degrees(asin(b / c)), 8):.2f} -> {sin_val:.2f} - a:{a}, b:{b}, c:{c}")
            if sin_val in lasers.keys():
                lasers[sin_val].append([w, h])
            else:
                lasers[sin_val] = [[w,h]]

print(lasers)
angles = sorted(list(lasers.keys()))
print(angles)

destroyed = 0
dest_target = 200
done = False
while not done:
    angles = sorted(list(lasers.keys()))
    for angle in angles:
        nearest = 10000
        to_destroy = []
        for loc in lasers[angle]:
            a = loc[1] - loc_h
            b = loc[0] - loc_w
            distance = sqrt((a ** 2) + (b ** 2))
            if distance < nearest:
                nearest = distance
                to_destroy = loc.copy()
        print(f"Destroying {destroyed+1} - {to_destroy}...")
        lasers[angle].remove(to_destroy)
        if lasers[angle] == []:
            del(lasers[angle])
        destroyed += 1
        if destroyed == dest_target:
            print(f'Target of {dest_target} reached...')
            done = True      
    
# print(lasers)



            
