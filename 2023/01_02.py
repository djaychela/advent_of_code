from data_read import read_file
import re

values = read_file("01.txt")

initials = ["o", "t", "f", "s", "e", "n"]
words = ["&&&", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

total = 0

for value in values:
    """
    look through string for each value
    """
    val_1 = None
    for idx, letter in enumerate(value):
        if letter in nums:
            val_1 = int(letter)
            break
        elif letter in initials:
            for word in words:
                try:
                    slice = value[idx:idx+len(word)]
                    if slice == word:
                        val_1 = words.index(word)
                        break
                except:
                    pass
        if val_1:
            break
    print(f"{val_1=}")
    val_2 = None
    # for idx, letter in enumerate(value[::-1], start=-len(value)):
    for idx in range(len(value) -1, -1, -1):
        letter = value[idx]
        # print(idx, letter)
        if letter in nums:
            val_2 = int(letter)
            break
        elif letter in initials:
            for word in words:
                try:
                    slice = value[idx:idx+len(word)]
                    # print(f"{slice=}")
                    if slice == word:
                        val_2 = words.index(word)
                        break
                except:
                    pass
        if val_2:
            break
    print(f"{val_2=}")
    print("---")
    val = int(val_1 * 10 + val_2)
    print(val)
    total += val

print(total)