from data_read import read_file

from itertools import zip_longest

packets_raw = read_file("13.txt")


def compare(data):

    for l, r in data:

        if l is None:
            return True
        elif r is None:
            return False

        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            elif l > r:
                return False
        else:    
            if isinstance(l, int):
                l = [l]
            if isinstance(r, int):
                r = [r]
            
            result = compare(zip_longest(l, r))

            if result is not None:
                return result     

pdx = 1
ordered = []

for idx in range(0, len(packets_raw), 3):
    p_1 = eval(packets_raw[idx].strip())
    p_2 = eval(packets_raw[idx+1].strip())
    if compare(zip_longest(p_1, p_2)):
        ordered.append(pdx)
    pdx += 1

# print(ordered)
print(sum(ordered))