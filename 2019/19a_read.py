import os

path = os.path.join(os.getcwd(), "data", "output_19a_2.txt")
with open(path, "r") as f:
    data = f.readlines()

for d in data:
    start = 0
    end = 0
    idx = 0
    last_c = ""
    for idx, c in enumerate(list(d)):
        if c == "0" and last_c == "1":
            end = idx
        elif c == "1" and last_c == "0":
            start = idx
        last_c = c
    print(start, end, (end-start))

