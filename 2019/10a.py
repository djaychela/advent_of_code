import os
from math import sqrt, sin, degrees

path = os.path.join(os.getcwd(), "data", "input_10a.txt")
with open(path, "r") as f:
    data = f.readlines()

puzzle_data = [d.rstrip() for d in data]

print(puzzle_data)
width = len(puzzle_data[0])
height = len(puzzle_data)

views = [['.' for w in range(width)] for h in range(height)]

best = 0
best_loc = ''
for w in range(width):
    for h in range(height):
        if puzzle_data[w][h] == '#':
            print(f'looking from ({h},{w}):')
            current_views = set()
            for view_w in range(width):
                for view_h in range(height):
                    if view_w == w and view_h == h:
                        continue
                    if puzzle_data[view_w][view_h] == "#":
                        a = view_w - w
                        b = view_h - h
                        c = sqrt((a ** 2) + (b ** 2))
                        sin_val = abs(round(degrees(sin(b / c)), 8))
                        if a != abs(a):
                            if b!= abs(b):
                                sin_val = 180 + sin_val
                            else:
                                sin_val = 180 - sin_val
                        if a == abs(a) and b != abs(b):
                            sin_val = 360 - sin_val

                        print(f"to ({view_h}, {view_w}):{round(degrees(sin(b / c)), 8)} -> {sin_val} - a:{a}, b:{b}, c:{c}")
                        current_views.add(sin_val)
            views[w][h] = len(current_views)
            if len(current_views) > best:
                best_loc = [h, w]
                best = len(current_views)
print(views)
print(best_loc, best)

            
