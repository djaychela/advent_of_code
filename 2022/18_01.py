from data_read import read_file

cubes_raw = read_file("18.txt")

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

cube_list = []

for cube in cubes_raw:
    current_cube = Cube(*list(map(int, cube.strip().split(","))))
    cube_list.append(current_cube)


for cube in cube_list:
    value = cube.check_sides(cube_list)

area = 0
for cube in cube_list:
    area += cube.sides

print(area)