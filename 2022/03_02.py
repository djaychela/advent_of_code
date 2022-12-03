from data_read import read_file

from string import ascii_lowercase

rucksacks = read_file("03.txt")

rucksacks = [r.strip() for r in rucksacks]

groups = [[rucksacks[r],rucksacks[r+1],rucksacks[r+2]] for r in range(0, len(rucksacks), 3)]

components = [[set(g[0]), set(g[1]), set(g[2])] for g in groups]

common = ["".join(c[0] & c[1] & c[2]) for c in components]

priorities = [ord(c) - 96 if c in ascii_lowercase else ord(c) - 38 for c in common]

print(sum(priorities))
