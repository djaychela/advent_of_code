import os

path = os.path.join(os.getcwd(), "data", "input_6a.txt")
with open(path, "r") as f:
    data = f.readlines()

orbits = [d.rstrip() for d in data]


class planet:
    def __init__(self, name, around):
        self.name = name
        self.around = around

    def orbits(self):
        ''' returns number of orbits from COM'''
        if self.name == "COM":
            return 0
        else:
            # return orbit of own around
            return planetoids[self.around].orbits() + 1


planetoids = {}

planetoids['COM'] = planet('COM','-')

for orbit in orbits:
    around, name = orbit.split(")")
    planetoids[name] = planet(name, around)

total = 0
for p in planetoids.keys():
    orbits = planetoids[p].orbits()
    total += orbits

print(total)
