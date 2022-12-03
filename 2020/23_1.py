cups = list(map(int, list("962713854")))
# cups = list(map(int, list("389125467")))

moves = 100
index = 0
pickup = 3

for move in range(moves):
    print(f" -- move {move + 1} --")
    current_cup = cups[index] # turns out this isn't right!

    temp_cups = cups.copy()
    temp_cups.extend(cups)
    picked_up = temp_cups[index + 1 : index + 1 + pickup]
    next_current = temp_cups[index + 1 + pickup]

    for remover in picked_up:
        while remover in temp_cups:
            temp_cups.remove(remover)

    # locate destination
    destination = -1
    while destination not in temp_cups:
        if destination == -1:
            destination = current_cup - 1
        else:
            destination -=1
        if destination == 0:
            destination = max(temp_cups)

    # place back in list
    insertion_index = temp_cups.index(destination) + 1
    dest_cups = temp_cups[:insertion_index]
    dest_cups.extend(picked_up)
    dest_cups.extend(temp_cups[insertion_index:])
    dest_cups = dest_cups[:9]

    # rotate cups to appropriate position.

    print(f"cups: {cups}")
    print(f"pick up: {picked_up}")
    print(f"destination: {destination}")
    index += 1
    index = index % 9
    
    cups = dest_cups.copy()
    # print(f"cups now: {cups}")
    cups.extend(dest_cups.copy())
    cups.extend(dest_cups.copy())
    # print(f"cups now: {cups}")
    
    # rotate here
    next_current_index = cups.index(next_current) + 9
    # print(index, next_current_index)
    # take slice from nci - index to 9 more than that
    cups = cups[next_current_index - index : next_current_index - index  + 9]
    # cups = cups[:9]
    # print(f"cups now: {cups}")
    

    # print(f"next cups: {cups}")

print(f"-- final --")
print("".join(map(str, cups)))

cups.extend(dest_cups.copy())
final_index = cups.index(1)
print("".join(map(str, cups[final_index + 1:final_index + 9])))