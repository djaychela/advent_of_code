from data_read import read_file

numbers = read_file("01.txt")

maximum = []
current = 0
for num in numbers:
    try:
        current += int(num.strip())
    except ValueError:
        maximum.append(current)
        current = 0

maximum.append(current)

print(sum(sorted(maximum)[-3:]))
