from data_read import read_file

from collections import deque

cubes_raw = read_file("18_test.txt")

class Cube:
    def __init__(self, x, y, z, sides = 6, matching = 0, adjacent = 0):
        self.x = x
        self.y = y
        self.z = z
        self.sides = sides
        self.matching = matching
        self.adjacent = adjacent

    def __repr__(self):
        return f"Cube: [{self.x}, {self.y}, {self.z}]  Sides:{self.sides}"

    def check_sides(self, cube_list):
        # print("****")
        # print(f"{cube_list=}")
        # print("----")
        for cube in cube_list:
            # print(cube)
            self.matching = 0
            if cube.x == self.x:
                self.matching += 1
            if cube.y == self.y:
                self.matching += 1
            if cube.z == self.z:
                self.matching += 1


            self.adjacent = 0
            if abs(cube.x - self.x) == 1:
                self.adjacent += 1
            if abs(cube.y - self.y) == 1:
                self.adjacent += 1
            if abs(cube.z - self.z) == 1:
                self.adjacent += 1

            if self.matching == 2 and self.adjacent == 1:
                self.sides -= 1
                # print(f"Next to each other, sides reduced to {self.sides}")
                # return False

            # print(f" {self.matching=} {self.adjacent=}")
            # return True
    def check_air_next(self, space_3d):
        try:
            if space_3d[self.x-1][self.y][self.z] == 0:
                # print(f"Air at {[self.x-1]},{[self.y]},{[self.z]}")
                self.sides -=1
        except IndexError:
            pass
        try:
            if space_3d[self.x+1][self.y][self.z] == 0:
                # print(f"Air at {[self.x+1]},{[self.y]},{[self.z]}")
                self.sides -=1
        except IndexError:
            pass
        try:
            if space_3d[self.x][self.y-1][self.z] == 0:
                # print(f"Air at {[self.x]},{[self.y-1]},{[self.z]}")
                self.sides -=1
        except IndexError:
            pass
        try:
            if space_3d[self.x][self.y+1][self.z] == 0:
                # print(f"Air at {[self.x]},{[self.y+1]},{[self.z]}")
                self.sides -=1
        except IndexError:
            pass
        try:
            if space_3d[self.x][self.y][self.z-1] == 0:
                # print(f"Air at {[self.x]},{[self.y]},{[self.z-1]}")
                self.sides -=1
        except IndexError:
            pass
        try:
            if space_3d[self.x][self.y][self.z+1] == 0:
                # print(f"Air at {[self.x]},{[self.y]},{[self.z+1]}")
                self.sides -=1
        except IndexError:
            pass
            

cube_list = []
x_max = -1000000
x_min = 1000000
y_max = -1000000
y_min = 1000000
z_max = -1000000
z_min = 1000000

for cube in cubes_raw:
    current_cube = Cube(*list(map(int, cube.strip().split(","))))
    cube_list.append(current_cube)
    x_max = max(x_max, current_cube.x)
    x_min = min(x_min, current_cube.x)
    y_max = max(y_max, current_cube.y)
    y_min = min(y_min, current_cube.y)
    z_max = max(z_max, current_cube.z)
    z_min = min(z_min, current_cube.z)

limits = [x_min, x_max, y_min, y_max, z_min, z_max]

# print(limits)

space_3d = [[[0 for z in range(z_min, z_max + 3)] for y in range(y_min, y_max + 2)] for x in range(x_min, x_max+2)]

def print_nicely(space_3d):
    for x in range(0, x_max + 1):
        print()
        for y in range(0, y_max + 1):
            print("".join(map(str, space_3d[x][y])))


for x in range(0, x_max + 1):
    for y in range(0, y_max + 1):
        for z in range(0, z_max + 1):
            for cube in cube_list:
                if cube.x == x and cube.y == y and cube.z == z:    
                    space_3d[x][y][z] = "#"

search_stack = deque()
search_stack.append((0, 0, 0))
while search_stack:
    x, y, z = search_stack.popleft()
    if x+1 <= x_max and space_3d[x+1][y][z] == 0:
        space_3d[x+1][y][z] = 1
        search_stack.append((x+1, y, z))
    if x-1 >= 0 and space_3d[x-1][y][z] == 0:
        space_3d[x-1][y][z] = 1
        search_stack.append((x-1, y, z))
    if y+1 <= y_max and space_3d[x][y+1][z] == 0:
        space_3d[x][y+1][z] = 1
        search_stack.append((x, y+1, z))
    if y-1 >= 0 and space_3d[x][y-1][z] == 0:
        space_3d[x][y-1][z] = 1
        search_stack.append((x, y-1, z))
    if z+1 <= z_max + 1 and space_3d[x][y][z+1] == 0:
        space_3d[x][y][z+1] = 1
        search_stack.append((x, y, z+1))
    if z-1 >= 0 and space_3d[x][y][z-1] == 0:
        space_3d[x][y][z-1] = 1
        search_stack.append((x, y, z-1))

for slice in space_3d:
    print(slice)

print_nicely(space_3d)

for cube in cube_list:
    value = cube.check_sides(cube_list)

for cube in cube_list:
    cube.check_air_next(space_3d)


area = 0
for cube in cube_list:
    area += cube.sides

print(area)
