from data_read import read_file

groves_raw = read_file("20.txt")

groves = [[idx, int(grove.strip()) * 811589153] for idx, grove in enumerate(groves_raw)]

length = len(groves)

for rounds in range(10):
    for idx in range(length):
        # find relevant
        jdx = 0
        found = False
        while not found:
            if groves[jdx][0] == idx:
                found = True
            else:
                jdx += 1
        action = groves[jdx][1] % length
        removed = groves.pop(jdx)
        final_location = (jdx + removed[1]) % (length - 1)
        # print(jdx, jdx + removed[1], (final_location + removed[1]) % (length - 1))
        groves.insert(final_location, removed)
        # print(f"Moved: {removed[1]}")
    print(f"Round {rounds+1} Complete:") 
    print([v for k,v in groves])

groves_final = [v for k,v in groves]

# print(groves_final)

zero_idx = groves_final.index(0)
nums = [groves[(zero_idx + idx) % length][1] for idx in (1000,2000,3000)]

print(sum(nums))