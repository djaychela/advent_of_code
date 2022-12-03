from data_read import read_file

players = read_file("21.txt")

positions = [int(player.strip()[-1]) for player in players][::-1]
scores = [0, 0]

def det_dice():
    nums = list(range(1,101))
    pointer = 0
    throws = 0
    while True:
        output = []
        for idx in range(3):
            loc = pointer + idx
            if loc >= 100:
                loc = loc % 100
            output.append(nums[loc])
        pointer += 3
        throws += 3
        pointer = pointer % 100
        yield output, throws

dice = det_dice()

running = True
while running:
    roll, throws = next(dice)
    
    round_score = positions[throws % 2] + sum(roll)
    while round_score >10:
        round_score -=10
    positions[throws % 2] = round_score
    
    scores[throws % 2] += round_score
    print(f"Player {throws % 2} rolls {roll}, moves to space {positions[throws % 2]} for score of {scores[throws % 2]}")
    if scores[throws % 2] >= 1000:
        running = False
        losing_score = scores[(throws + 1) % 2]
print(f"Part 1: {throws=} {losing_score=} = {losing_score * throws}")
