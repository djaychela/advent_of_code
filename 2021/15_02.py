from data_read import read_file

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

risks = read_file("15.txt")

cave = [[int(chiton) for chiton in risk.strip()] for risk in risks]
cave_width = len(cave[0])
cave_height = len(cave)
max_width = (len(cave[0]) * 5)
max_height = (len(cave) * 5)

new_cave = [[0 for _ in range(max_width)] for _ in range(max_height)]

for idx in range(max_height):
    for jdx in range(max_width):
        idx_grid_num = idx // cave_height
        idx_grid = idx % cave_height
        jdx_grid_num = jdx // cave_width 
        jdx_grid = jdx % cave_width
        og_grid_value = (cave[idx_grid][jdx_grid] + idx_grid_num + jdx_grid_num)
        while og_grid_value > 9:
            og_grid_value -= 9

        new_cave[idx][jdx] = og_grid_value

grid = Grid(matrix=new_cave)
start = grid.node(0,0)
end = grid.node(max_height - 1,max_width - 1)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

score = sum([new_cave[jdx][idx] for idx,jdx in path[1:]])

print(f"Score: {score}")