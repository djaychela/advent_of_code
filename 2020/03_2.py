import pathlib

file_name = "03.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    map = file.readlines()

map = [line.strip() for line in map]

print(map)

rows = len(map)
cols = len(map[0])

row_pos = 0
col_pos = 0

increments = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

scores = []

for increment in increments:
    current_score = 0
    while row_pos < rows:
        if map[row_pos][col_pos] == "#":
            current_score +=1
        row_pos += increment[0]
        col_pos += increment[1]
        col_pos = col_pos % cols
    scores.append(current_score)
    row_pos = 0
    col_pos = 0

print(scores)
final_score = 1
for score in scores:
    final_score *= score
print(final_score)
