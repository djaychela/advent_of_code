from data_read import read_file

elves_raw = read_file("23.txt")

elf_coords = []
for idx, elf in enumerate(elves_raw):
    for jdx, cell in enumerate(elf.strip()):
        if cell == "#":
            elf_coords.append([jdx, idx])

# print(elf_coords)

clear_locations = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
check_dirs = [[[0, -1], [-1, -1], [1, -1]], 
            [[0, 1], [-1, 1], [1, 1]], 
            [[-1, 0], [-1, -1], [-1, 1]],
            [[1, 0], [1, -1], [1, 1]]
            ]
check_dirs.extend(check_dirs)

check_idx = 0

print(check_dirs[check_idx:check_idx+4])

current_cycle = 0

def view_elves(elf_coords):
    empty_tiles = 0
    x_coords = [elf[0] for elf in elf_coords]
    y_coords = [elf[1] for elf in elf_coords]

    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    for row in range(min_y, max_y + 1):
        line = []
        for col in range(min_x, max_x + 1):
            if [col, row] in elf_coords:
                # line.append(f"{chr(elf_coords.index([col, row]) + 64)}")
                line.append("#")
            else:
                line.append(".")
                empty_tiles += 1
        print("".join(line))
    print(f"Empty Tiles: {empty_tiles}")

moved = 1
while moved != 0:
    # if current_cycle == 10:
    #     break
    proposed = []
    moved = 0
    for idx, elf in enumerate(elf_coords):
        # check if all positions are clear, if so, elf does not move
        found = False
        for clear in clear_locations:
            new_coord = [elf[0] + clear[0], elf[1] + clear[1]]
            if new_coord in elf_coords:
                found = True
        if not found:
            # print(f"{chr(idx + 64)}->{elf} will not move this time!")
            continue
        else:
            moved += 1
        # check all other elf positions against check_dirs
        # rotate check_dirs
        for check in check_dirs[check_idx:check_idx+4]:
            found = False
            for dr in check:
                new_coord = [elf[0] + dr[0], elf[1] + dr[1]]
                if new_coord in elf_coords:
                    # print(f"{chr(idx + 64)}->{elf}: Elf at {new_coord} {dr}")
                    found = True
            if found:
                # print(f"elf {chr(idx + 64)}->{elf} Cannot move {check[0]}")
                pass
            else:
                prop_coord = [elf[0] + check[0][0], elf[1] + check[0][1]]
                # print(f"elf {chr(idx + 64)}->{elf} Can move {check[0]} to {prop_coord}")
                proposed.append([idx, prop_coord])
                break
        # if ok, propose move in that direction
    # print(proposed)
    proposed_locs = [pr[1] for pr in proposed]
    # print(proposed_locs)
    for prop in proposed:
        if proposed_locs.count(prop[1]) == 1:
            # do move
            current = elf_coords[prop[0]]
            # print(f"Current elf: {current}")
            current[0] += prop[1][0]
            current[1] += prop[1][1]
            elf_coords[prop[0]] = prop[1]
            # print(f"Moved to: {prop[1]}")
    # print(current_cycle, elf_coords, moved)
    # print([(chr(idx + 64), coord) for idx, coord in enumerate(elf_coords)])
    check_idx += 1
    check_idx = check_idx % 4
    current_cycle += 1
    # view_elves(elf_coords)
    print(f"End of round {current_cycle}")
    # wait = input("Next...")

