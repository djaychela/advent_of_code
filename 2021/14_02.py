from data_read import read_file
from collections import Counter

polymerisation = read_file("14.txt")

splitpoint = polymerisation.index("\n")

polymer_template = polymerisation[:splitpoint][0].strip()
insertions = {
    insertions.strip().split(" -> ")[0]: insertions.strip().split(" -> ")[1]
    for insertions in polymerisation[splitpoint + 1 :]
}

letters = Counter(polymer_template)
pairs = Counter(
    [polymer_template[idx : idx + 2] for idx in range(len(polymer_template) - 1)]
)

for steps in range(40):
    previous_pairs = pairs.copy()
    for (l_1, l_2), ins in insertions.items():
        count = previous_pairs[l_1 + l_2]
        pairs[l_1 + l_2] -= count
        pairs[l_1 + ins] += count
        pairs[ins + l_2] += count
        letters[ins] += count

most_common = letters.most_common()[0][1]
least_common = letters.most_common()[-1][1]
print(f"Answer: {most_common - least_common}")
