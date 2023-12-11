from data_read import read_file

galaxies_raw = read_file("11.txt")
galaxies = []

y_set = set()
x_set = set()
y_len = len(galaxies_raw)
x_len = len(galaxies_raw[0].strip())

for ydx, line in enumerate(galaxies_raw):
    for xdx, char in enumerate(line):
        # print(f"{ydx=}, {xdx=}, {char}")
        if char == "#":
            galaxies.append([ydx, xdx])
            y_set.add(ydx)
            x_set.add(xdx)

y_missing = [y for y in range(y_len) if y not in y_set]
x_missing = [x for x in range(x_len) if x not in x_set]

for g in galaxies:
    y_og = g[0]
    x_og = g[1]
    for y in y_missing:
        if y_og > y:
            g[0] += 1
    for x in x_missing:
        if x_og > x:
            g[1] += 1
            
distances = []

for idx, g in enumerate(galaxies):
    for jdx, g_2 in enumerate(galaxies):
        if idx != jdx:
            distance = abs(g[0] - g_2[0]) + abs(g[1] - g_2[1])
            print(f"{idx+1} - {g} : {g_2}: {distance=}")
            distances.append(distance)

print(sum(distances) / 2)
