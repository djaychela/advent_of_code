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

score = 0

while row_pos < rows:
    if map[row_pos][col_pos] == "#":
        score +=1
    row_pos +=1
    col_pos +=3
    col_pos = col_pos % cols

print(score)
