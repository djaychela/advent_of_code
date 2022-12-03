from data_read import read_file

numbers = read_file("01.txt")

maximum = 0
current = 0
for num in numbers:
    try:
        current += int(num.strip())
    except ValueError:
        maximum = max(current, maximum)
        current = 0

maximum = max(current, maximum)

print (maximum)
