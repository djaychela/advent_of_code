"""This allowed me to work out how to do this in 1 dimension before making Cuboids in 3 dimensions"""

from dataclasses import dataclass


@dataclass
class Linoid:
    x_start: int
    x_end: int
    status: int
    name: str

    def check_status(self, location):
        if self.x_start <= location <= self.x_end:
            if self.status:
                return 1
            else:
                return 0
        return None


a = Linoid(1, 8, 1, "a")
b = Linoid(2, 7, 0, "b")
c = Linoid(4, 8, 1, "c")

linoid_list = [a, b]

for i in range(0, 10):
    # check linoid intersections
    present = [0]
    for linoid in linoid_list:
        value = linoid.check_status(i)
        if value is not None:
            present.append(value)
    print(i, present[-1])
