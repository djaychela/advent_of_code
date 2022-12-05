from data_read import read_file

import re

assignments = read_file("04_test.txt")

# Split the assignments on "," and "-" and convert to integerspwd
assignments = [list(map(int, re.split(r',|-', a))) for a in assignments]

# total = 0

# for a in assignments:
#     if a[0] <= a[2] and a[1] >= a[3]:
#         total += 1
#     elif a[2] <= a[0] and a[3] >= a[1]:
#         total += 1


# Check if any assignments overlap
overlap = [any(a[0] <= a[2] and a[1] >= a[3] or a[2] <= a[0] and a[3] >= a[1] for a in assignments)]
print(overlap)

# Calculate the total number of assignments
total = sum(1 for a in assignments if overlap)

print(total)

