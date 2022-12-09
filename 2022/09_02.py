from data_read import read_file

from numpy import sign

rope_inst = read_file("09.txt")

dir_map = {'R':[1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

rope_position = [[0, 0] for _ in range(10)]
tail_unique = []
tail_delta = [0, 0]

for inst in rope_inst:
    inst = inst.strip().split()
    direction = inst[0]
    distance = int(inst[1])
    for _ in range(distance):
        # update rope head position [0] from direction
        rope_position[0][0] += dir_map[direction][0]
        rope_position[0][1] += dir_map[direction][1]
        
        # update all rope positions, based on previous part's location
        for idx in range(1, 10):
            # calculate current delta
            tail_delta[0] = rope_position[idx-1][0] - rope_position[idx][0]
            tail_delta[1] = rope_position[idx-1][1] - rope_position[idx][1]
            tail_direction = [0, 0]

            # check for distance and move if needed
            abs_delta = [abs(x) for x in tail_delta]
            if max(abs_delta) >= 2:
                tail_direction = list(sign(tail_delta))     

            # update tail position
            rope_position[idx][0] += tail_direction[0]
            rope_position[idx][1] += tail_direction[1]
            
        # print(f"head:{head_position}, tail:{tail_position}, dir:{tail_direction}")
        loc_string = f"{rope_position[9][0]}-{rope_position[9][1]}"
        if loc_string not in tail_unique:
            tail_unique.append(loc_string)

print(f"Positions Visited by tail: {len(tail_unique)}")
