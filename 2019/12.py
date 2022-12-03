import os

path = os.path.join(os.getcwd(), "data", "input_12a.txt")
with open(path, "r") as f:
    data = f.readlines()

data = [d.rstrip() for d in data]

pos = [[0 for _ in range(3)] for _ in range(4)]
vel = [[0 for _ in range(3)] for _ in range(4)]
pot = [0 for _ in range(4)]
kin = [0 for _ in range(4)]

# read data into array:
for ddx, d in enumerate(data):
    for idx, v in enumerate(map(int, d.split(',')[1::2])):
        pos[ddx][idx] = v

for _ in range(1000):
    # create velocities:
    for jdx in range(len(pos)):
        for idx in range(len(pos[0])):
            current_value = pos[jdx][idx]
            current_vel = vel[jdx][idx]
            for vdx in range(len(pos)):
                if vdx == jdx:
                    continue
                if pos[vdx][idx] < current_value:
                    current_vel -= 1
                elif pos[vdx][idx] > current_value:
                    current_vel += 1
            vel[jdx][idx] = current_vel

    # apply velocities:
    for jdx in range(len(pos)):
        for idx in range(len(pos[0])):
            pos[jdx][idx] += vel[jdx][idx]

# calculate potential energy and kinetic energy
for jdx in range(len(pos)):
    for idx in range(len(pos[0])):
        pot[jdx] += abs(pos[jdx][idx])
        kin[jdx] += abs(vel[jdx][idx])
print(pot)
print(kin)
sum = 0
for jdx in range(len(pos)):
    sum += pot[jdx] * kin[jdx]

print(sum)