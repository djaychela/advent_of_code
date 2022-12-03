from data_read import read_file

heightmap = read_file("09.txt")

heightmap = [[int(num) for num in line.strip()] for line in heightmap ]
width = len(heightmap[0])
height = len(heightmap)

total = 0

def get_surrounding_values(grid, y, x):
    deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    output = []
    for delta in deltas:
        i = y + delta[0]
        j = x + delta[1]
        if i < 0 or i == len(grid):
            continue
        if j < 0 or j == len(grid[0]):
            continue
        output.append(grid[i][j])
    return output

for idx in range(height):
    for jdx in range(width):
        surrounding = get_surrounding_values(heightmap, idx, jdx)
        if heightmap[idx][jdx] < min(surrounding):
            total += heightmap[idx][jdx] + 1

print(f"Total: {total}")