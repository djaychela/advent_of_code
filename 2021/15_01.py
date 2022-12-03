from data_read import read_file

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

risks = read_file("15.txt")

cave = [[int(chiton) for chiton in risk.strip()] for risk in risks]

grid = Grid(matrix=cave)
max_width = len(cave[0]) - 1
max_height = len(cave) - 1
start = grid.node(0,0)
end = grid.node(max_height,max_width)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

score = sum([cave[jdx][idx] for idx,jdx in path[1:]])

print(f"Score: {score}")