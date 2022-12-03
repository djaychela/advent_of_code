from data_read import read_file

from string import ascii_lowercase

rucksacks = read_file("03.txt")

rucksacks = [r.strip() for r in rucksacks]

components = [[set(r[:int(len(r)/2)]), set(r[int(len(r)/2):])] for r in rucksacks]

common = ["".join(c[0] & c[1]) for c in components]

priorities = [ord(c) - 96 if c in ascii_lowercase else ord(c) - 38 for c in common]

print(sum(priorities))
