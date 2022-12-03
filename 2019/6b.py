import os

path = os.path.join(os.getcwd(), "data", "input_6a.txt")
with open(path, "r") as f:
    data = f.readlines()

orbits = [d.rstrip() for d in data]


class planet:
    def __init__(self, name, around):
        self.name = name
        self.around = around
        self.chain = []

    def orbits(self, original):
        """ returns number of orbits from COM"""
        if self.name == "COM":
            return 0
        else:
            planetoids[original].chain.append(self.name)
            return planetoids[self.around].orbits(original) + 1


planetoids = {}

planetoids["COM"] = planet("COM", "-")

for orbit in orbits:
    around, name = orbit.split(")")
    planetoids[name] = planet(name, around)


you_list = planetoids["YOU"].orbits("YOU")
san_list = planetoids["SAN"].orbits("SAN")

you_chain = planetoids["YOU"].chain[1:]
san_chain = planetoids["SAN"].chain[1:]

print(planetoids["YOU"].chain)
print(planetoids["SAN"].chain)

min_distance = 1000000000
for idx, y in enumerate(you_chain, 1):
    if y in san_chain:
        for san_idx, san in enumerate(san_chain, 1):
            if y == san:
                print(f"found link = {y}")
                print(f"Indexes - you: {idx}, san: {san_idx}")
                min_distance = min(min_distance, (san_idx + idx - 2 ))
                print(f"Min Distance now {min_distance}")




