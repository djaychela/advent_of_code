import pathlib
from itertools import combinations

file_name = "19.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    received = [line.strip() for line in file.readlines()]

splitpoint = received.index('')

rules = received[:splitpoint]
messages = received[splitpoint + 1:]


max_lines = 0
for message in rules:
    # mess = list(message)
    max_lines = max(max_lines, message.count("|"))
print(max_lines)