import pathlib

file_name = "01.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    buttons = file.readlines()[0]

up = buttons.count("(")
down = buttons.count(")")
floor = up - down
print(floor)