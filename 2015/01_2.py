import pathlib

file_name = "01.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    buttons = file.readlines()[0]

floor = 0
for idx, press in enumerate(buttons, 1):
    if press == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(f"Basement reached after {idx} presses.")
        break
