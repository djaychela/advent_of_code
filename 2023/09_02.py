from data_read import read_file

values = read_file("09.txt")

differences = []

for line in values:
    numbers = list(map(int, line.strip().split()))
    differences.append([numbers])

for difference in differences:
    done = False
    difference_index = 0
    while not done:
        new_values = []
        for idx in range(len(difference[difference_index])):
            try:
                new_value = difference[difference_index][idx+1] - difference[difference_index][idx]
            except IndexError:
                continue    
            new_values.append(new_value)
        print(f"{difference_index=}, {new_values=}")
        difference.append(new_values)
        if new_values[0] == 0 and len(set(new_values)) == 1:
            difference[difference_index + 1].append(0)
            print("differences complete.  Zero added")
            done = True
        difference_index +=1
        
for history in differences:
    for idx in range(len(history) -2, -1, -1):
        extrapolated = history[idx][0] - history[idx + 1][0]
        print(f"{history[idx]} - {history[idx + 1]}")
        print(f"{extrapolated=} : {history[idx][0]} - {history[idx + 1][0]}")
        history[idx].insert(0, extrapolated)

score = []
for history in differences:
    score.append(history[0][0])

print(sum(score))
