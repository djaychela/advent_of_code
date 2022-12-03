import pathlib

file_name = "06.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    groups = file.readlines()

scores = []
current_group = set()
for group in groups:
    if group != '\n':
        group_elements = list(group.strip())
        for element in group_elements:
            current_group.add(element)
    else:
        scores.append(current_group)
        current_group = set()
scores.append(current_group)
total = 0
for score in scores:
    total += len(score)
print(total)