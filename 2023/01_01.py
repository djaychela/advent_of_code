from data_read import read_file
import re

values = read_file("01.txt")

total = 0

for value in values:
    val_1 = re.findall("^[^\d]*(\d)", value.strip())[0]
    val_2 = re.findall("^[^\d]*(\d)", value.strip()[::-1])[0]
    val = int(val_1 + val_2)
    print(val)
    total += val

print(total)