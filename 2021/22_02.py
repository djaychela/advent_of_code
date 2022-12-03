from data_read import read_file
from tqdm import tqdm
from dataclasses import dataclass, field

cuboids = read_file("22_test.txt")

cuboids = [cubes.strip().split() for cubes in cuboids]
cuboids = [[cubes[0], cubes[1].split(",")] for cubes in cuboids]
cuboids = [[1 if cubes[0] == "on" else 0, [list(map(int, cube[2:].split('..'))) for cube in cubes[1]]] for cubes in cuboids]

cubes = []

@dataclass
class Cuboid:
    x_start: int
    x_end: int
    y_start: int
    y_end: int
    z_start: int
    z_end: int
    status: int

    def check_status(self, loc_x, loc_y, loc_z):
        if self.x_start <= loc_x <= self.x_end:
            if self.y_start <= loc_y <= self.y_end:
                if self.z_start <= loc_z <= self.z_end:
                    if self.status:
                        return 1
                    else:
                        return 0
        return None
    

cuboid_list = []
for step in cuboids:
    print(step)
    current_cuboid = Cuboid(step[1][0][0], step[1][0][1], step[1][1][0], step[1][1][1], step[1][2][0], step[1][2][1], step[0])
    cuboid_list.append(current_cuboid)

cubes_on = 0
for cuboid in cuboid_list:
    for loc_x in tqdm(range(cuboid.x_start, cuboid.x_end + 1)):
        for loc_y in range(cuboid.y_start, cuboid.y_end + 1):
            for loc_z in range(cuboid.z_start, cuboid.z_end + 1):
                print(f"{loc_x=}:{loc_y=}:{loc_z=}")
                present = [0]
                for cube in cuboid_list:
                    value = cube.check_status(loc_x, loc_y, loc_z)
                    if value is not None:
                        present.append(value)
                cubes_on += present[-1]
                print(f"{cubes_on=},  {present[-1]=}")

print(cubes_on)

                