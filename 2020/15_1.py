import pathlib

file_name = "15.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    numbers = [int(number) for number in file.readlines()[0].split(",")]

turn = 1
starting_numbers = len(numbers)
while turn <= 2020:
    if turn <= starting_numbers:
        current = numbers[turn - 1]
    elif numbers.count(current) <= 1:
        current = 0
        numbers.append(current)
    else:
        idx = len(numbers) - 1
        while numbers[idx] != current:
            idx -= 1
        previous = idx
        idx -=1
        while numbers[idx] != current:
            idx -= 1
        last = idx
        current = previous - last 
        numbers.append(current)

    turn += 1
    
print(turn - 1, current)
