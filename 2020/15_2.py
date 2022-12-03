import pathlib

file_name = "15.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    numbers = [int(number) for number in file.readlines()[0].split(",")]

turn = 1
num_dict = {number:[idx] for idx, number in enumerate(numbers, 1)}
turn_dict = {idx:number for idx, number in enumerate(numbers, 1)}

while turn <= 30000000:
    if turn in turn_dict.keys():
        current = turn_dict[turn]
    else:
        if len(num_dict[current]) < 2:
            current = 0
            num_list = num_dict[current]
            num_list.append(turn)
            num_dict[current] = num_list[-2:]
        else:
            num_list = num_dict[current]
            current = num_list[1] - num_list[0]
            try:
                num_list = num_dict[current]
                num_list.append(turn)
                num_dict[current] = num_list[-2:]
                
            except KeyError:
                num_dict[current] = [turn]

    if turn %10000 == 0:
        print(turn)
    turn += 1
    
print(turn - 1, current)