import pickle

from data_read import read_file

jets_raw = read_file("17.txt")

jets = jets_raw[0].strip().split()[0]

jet_len = len(jets)

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
# print(play_field)
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

def scan_play_field_top(play_field, jet_position):
    values = list(play_field.keys())
    # for cp_loc in cp_locations:
    #     values.append((cp_loc[0], cp_loc[1]))
    # print(list(values))
    top_line = []
    norm_y = max(y for x,y in values)
    
    for idx in range(0, 7):
        max_y = max(y-norm_y for x,y in values if x == idx)
        top_line.append(max_y)
    return (top_line, jet_position)

def scan_play_field_top_2(play_field):
    values = list(play_field.keys())
    # add top 25 rows for each column
    rows_to_scan = 25
    top_line = []
    norm_y = max(y for x,y in values)
    
    for idx in range(0, 7):
        sum_y = sum(y-norm_y for x,y in values if x == idx and y-norm_y <= rows_to_scan)
        top_line.append(sum_y)
    return top_line

play_field_maxes = []

play_field_tops = []



for i in range(60000):
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
        # if i > 76:
            # print(f"Play Field {i}")
            # visualise_play_field(play_field, cp_locations)
        # visualise_play_field(play_field, cp_locations)
        current_jet = (current_jet + 1) % len(jets)
    new_top_line = scan_play_field_top(play_field, current_jet)
    play_field_max_y = max([y for x,y in play_field.keys()])
    play_field_maxes.append(play_field_max_y)
    
    if new_top_line not in play_field_tops:
        play_field_tops.append(new_top_line)
    else:
        target_cycle_value = 1000000000000
        original_index = play_field_tops.index(new_top_line)
        repeat_length = i - original_index
        baseline = play_field_maxes[original_index]
        add_per_cycle = play_field_maxes[i] - play_field_maxes[original_index]
        print(f'duplicate top line at {i} - originally at {original_index}')
        print(f"{current_piece=}")
        print(f"{play_field_tops=}")
        print(f"{new_top_line=}")
        # print(f"originally at {original_index}")
        print(f"pattern repeating every {repeat_length}")
        print(f"Height at {original_index}: {play_field_maxes[original_index]}")
        print(f"Height at {i}: {play_field_maxes[i]}")
        print(f"Cycle adds: {add_per_cycle}")
        repeat_cycle_value = target_cycle_value - baseline
        number_of_cycles = repeat_cycle_value // repeat_length
        cycle_total_value = number_of_cycles * add_per_cycle
        remaining_drops = target_cycle_value - ((number_of_cycles * repeat_length) + original_index)
        after_value = play_field_maxes[original_index + remaining_drops] - play_field_maxes[original_index]
        print(f"Cycle Total Value: {cycle_total_value}")
        print(f"Before Value: {baseline}")
        print(f"Remaining Drops: {remaining_drops}")
        print(f"After Value: {after_value}")
        print(f"Total Rocks: {cycle_total_value + baseline + after_value - 1}")
        break
    # play_field_tops.append(scan_play_field_top(play_field))
    current_piece = (current_piece + 1) % len(pieces)
    if current_piece == 0 and current_jet == 0:
        print(f"Cycle Repeated: {i}")
    # increase insertion height
    rock_height = play_field_max_y + 4
    if i % 1000 == 0:
        print(f"{i}:{play_field_max_y=}")
    # visualise_play_field(play_field, [])
# print(f"{i+1}:{play_field_max_y=}")



# 1629629629629 - too high