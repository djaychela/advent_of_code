from data_read import read_file

jets_raw = read_file("17_test.txt")

jets = jets_raw[0].strip().split()[0]

jet_len = len(jets)

print(jet_len)

# exit()

pieces = [["....", "....", "....", "####"], 
        ["....",".#..", "###.", ".#.."], 
        ["....","..#.", "..#.", "###."],
        ["#...","#...", "#...", "#..."],
        ["....","....", "##..", "##.."],
        ]

rock_height = 4
play_field = dict()
for r in range(8):
    play_field[r, 0] = "#"
print(play_field)
current_piece = 0
current_jet = 0

def det_future_coll(play_field, cp_locations, movement):
    found = False
    for piece in cp_locations:
        loc = (piece[0] + movement[0], piece[1] + movement[1])
        if loc in play_field.keys():
            found = True
    return found

def visualise_play_field(play_field, cp_locations):
    values = list(play_field.keys())
    for cp_loc in cp_locations:
        values.append((cp_loc[0], cp_loc[1]))
    # print(list(values))
    max_y = max(y for x,y in values)
    for x in range(max_y, -1, -1):
        line = []
        for y in range(7):
            loc = (y, x)
            if loc in values:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))

for i in range(2022):
    cp_locations = []
    # create list of coordinates based on pieces and current height
    for idx, line in enumerate(pieces[current_piece][::-1]):
        for jdx, element in enumerate(line):
            if element=="#":
                cp_locations.append([2 + jdx, rock_height + idx])
    # print(f"{current_piece=}")
    # print(f"Piece: {pieces[current_piece]}")
    # print(cp_locations)
    falling = True
    while falling:
        
        max_x = max([x for x,y in cp_locations])
        min_x = min([x for x,y in cp_locations])
        min_y = min([y for x,y in cp_locations])
        # print(f"{min_x=} {max_x=}, {min_y=}")
        # print(f"{jets[current_jet]}")
        # print(cp_locations)
        # jet pushes it
        if jets[current_jet] == ">" and max_x < 6:
            right_coll = det_future_coll(play_field, cp_locations, [1, 0])
            if not right_coll:
                cp_locations = [[x + 1, y] for x,y in cp_locations]
        elif jets[current_jet] == "<" and min_x > 0:
            left_coll = det_future_coll(play_field, cp_locations, [-1, 0])
            if not left_coll:
                cp_locations = [[x -1, y] for x,y in cp_locations]
        # print(cp_locations)
        # falls if possible
        grav_found = det_future_coll(play_field, cp_locations, [0, -1])
        if grav_found:
            falling = False
            # add pieces to play field
            for piece in cp_locations:
                play_field[piece[0], piece[1]] = "#"
        else:
            cp_locations = [[x, y - 1] for x, y in cp_locations]
        # visualise_play_field(play_field, cp_locations)
        current_jet = (current_jet + 1) % len(jets)
    current_piece = (current_piece + 1) % len(pieces)
    # increase insertion height
    play_field_max_y = max([y for x,y in play_field.keys()])
    rock_height = play_field_max_y + 4
    if i % 1000 == 0:
        print(f"{i}:{play_field_max_y=}")
    # visualise_play_field(play_field, [])
print(f"{i+1}:{play_field_max_y=}")