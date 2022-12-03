from data_read import read_file
from collections import Counter

polymerisation = read_file("14.txt")

splitpoint = polymerisation.index("\n")

polymer_template = polymerisation[:splitpoint][0].strip()
insertions = {insertions.strip().split(" -> ")[0]:insertions.strip().split(" -> ")[1] for insertions in polymerisation[splitpoint+1:]}

new_polymer = polymer_template

current_polymer = polymer_template
new_polymer = ""
for steps in range(40):
    
    for idx in range(len(current_polymer)):
        current = current_polymer[idx:idx+2]
        if current in insertions.keys():
            new_polymer += current_polymer[idx] + insertions[current]
        else:
            new_polymer += current_polymer[idx]

    print(f"After Step {steps + 1}: {new_polymer}")
    current_polymer = new_polymer
    new_polymer = ""

counts = Counter(current_polymer)
most_common = counts.most_common()[0][1]
least_common = counts.most_common()[-1][1]
print(f"Answer: {most_common - least_common}")