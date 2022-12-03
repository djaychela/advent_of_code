from data_read import read_file

cucumbers = [[cuc for cuc in cucumber.strip()] for cucumber in read_file("25.txt")]

def check_moves(cucumbers):
    check = {">": (1, 0), "v": (0, 1)}
    width = len(cucumbers[0])
    height = len(cucumbers)
    moved = False
    for type in [">", "v"]:
        movable = []
        for idx in range(height):
            for jdx in range(width):
                cuc = cucumbers[idx][jdx]
                if cuc == type:
                    delta = check[cuc]
                    pidx = (idx + delta[1]) % height
                    pjdx = (jdx + delta[0]) % width
                    if cucumbers[pidx][pjdx] == ".":
                        moved = True
                        movable.append((idx, jdx))
                    # print(f"{idx=},{jdx=}:{cucumbers[idx][jdx]=}, {pidx=}{pjdx=}, {cucumbers[pidx][pjdx]=}")
        for move in movable:
            cucumbers[move[0]][move[1]] = "."
            pidx = (move[0] + delta[1]) % height
            pjdx = (move[1] + delta[0]) % width
            cucumbers[pidx][pjdx] = type
    
    return cucumbers, moved

def display_grid(cucumbers):
    width = len(cucumbers[0])
    height = len(cucumbers)
    for idx in range(height):
        for jdx in range(width):
            print(cucumbers[idx][jdx], end="")
        print("")

running = True
move = 0
while running:
    move += 1
    cucumbers, running = check_moves(cucumbers)
    print(f"Move: {move}")
    if move % 10 == 0:
        display_grid(cucumbers)

print(f"Number of Moves: {move}")