from data_read import read_file

heightmap = read_file("09.txt")

heightmap = [[0 if num !="9" else 9 for num in line.strip() ] for line in heightmap ]
width = len(heightmap[0])
height = len(heightmap)

def floodfill(matrix, x, y):
    score = 0
    if matrix[y][x] == 0:  
        matrix[y][x] = 1 
        score = 1
        if x > 0:
            score += floodfill(matrix,x-1,y)
        if x < len(matrix[0]) - 1:
            score += floodfill(matrix,x+1,y)
        if y > 0:
            score += floodfill(matrix,x,y-1)
        if y < len(matrix) - 1:
            score += floodfill(matrix,x,y+1)
    return score

scores = []
for idx in range(width):
    for jdx in range(height):
        scores.append(floodfill(heightmap, idx, jdx))

scores = sorted(scores, reverse=True)[:3]

print(f"Total: {scores[0] * scores[1] * scores[2]}")