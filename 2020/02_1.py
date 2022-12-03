import pathlib

file_name = "02.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    passwords = file.readlines()

total = 0
for password in passwords:
    limit, letter, pwd = password.split()
    lower , upper = map(int, limit.split('-'))
    characters = list(pwd).count(letter[0])
    if lower <= characters <= upper:
        total += 1

print(total)