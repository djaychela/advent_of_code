from data_read import read_file

assignments = read_file("04.txt")

assignments = [a.strip() for a in assignments]

assignments = [list(map(int, a.replace(","," ").replace("-"," ").split(" "))) for a in assignments]

total = 0

for a in assignments:
    if a[0] <= a[2] and a[1] >= a[3]:
        total += 1
    elif a[2] <= a[0] and a[3] >= a[1]:
        total += 1

print(total)
