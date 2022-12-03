from data_read import read_file

digits = read_file("08.txt")

digits = [(digit.split("|")[0].strip(), digit.split("|")[1].strip()) for digit in digits]

total = 0

for display in digits:
    for digit in display[1].split():
        print(digit)
        match len(digit):
            case 2:
                total += 1
            case 3:
                total += 1
            case 4:
                total += 1
            case 7:
                total += 1

print(total)