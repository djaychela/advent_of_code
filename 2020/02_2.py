import pathlib

file_name = "02.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    passwords = file.readlines()

total = 0
for password in passwords:
    limit, letter, pwd = password.split()
    pos_1 , pos_2 = map(int, limit.split('-'))
    p1_ok = (pwd[pos_1 - 1] == letter[0])
    p2_ok = (pwd[pos_2 - 1] == letter[0])
    if p1_ok ^ p2_ok:
        total += 1


print(total)