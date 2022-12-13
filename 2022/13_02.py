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
all_packets = []


for idx in range(0, len(packets_raw), 3):
    p_1 = eval(packets_raw[idx].strip())
    p_2 = eval(packets_raw[idx+1].strip())
    all_packets.append(p_1)
    all_packets.append(p_2)

all_packets.append(list([[2]]))
all_packets.append(list([[6]]))

def bubble_sort(array):
    
    for idx in range(len(array)):
        for jdx in range(0, len(array) - idx - 1):
            if compare(zip_longest(array[jdx], array[jdx + 1])):
                array[jdx], array[jdx + 1] = array[jdx + 1], array[jdx]

    return array

ordered_packets = list(reversed(bubble_sort(all_packets)))

idx_1 = ordered_packets.index([[2]]) + 1
idx_2 = ordered_packets.index([[6]]) + 1

print(idx_1 * idx_2)