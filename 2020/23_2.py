""" This might work if I had infinite time. """

cups = list(map(int, list("962713854")))
cups = list(map(int, list("389125467")))

cup_fill_start = max(cups) + 1

while cup_fill_start <= 1000000:
    cups.append(cup_fill_start)
    cup_fill_start += 1

moves = 10000000
index = 0
pickup = 3
number_of_cups = len(cups)

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
    dest_cups = dest_cups[:number_of_cups]

    # rotate cups to appropriate position.

    # print(f"cups: {cups}")
    # print(f"pick up: {picked_up}")
    # print(f"destination: {destination}")
    index += 1
    index = index % number_of_cups
    
    cups = dest_cups.copy()
    # print(f"cups now: {cups}")
    cups.extend(dest_cups.copy())
    cups.extend(dest_cups.copy())
    # print(f"cups now: {cups}")
    
    # rotate here
    next_current_index = cups.index(next_current) + number_of_cups
    # print(index, next_current_index)
    # take slice from nci - index to 9 more than that
    cups = cups[next_current_index - index : next_current_index - index  + number_of_cups]
    # cups = cups[:9]
    # print(f"cups now: {cups}")
    

    # print(f"next cups: {cups}")

cups.extend(dest_cups.copy())

final_index = cups.index(1)
print(cups[final_index + 1])
print(cups[final_index + 2])
print(cups[final_index + 1] * cups[final_index + 2])