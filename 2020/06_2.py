import pathlib

file_name = "06.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    groups = file.readlines()


def score_group(current_group_answers, current_group):
    group_score = 0
    for letter in current_group:
        letter_score = 1
        for current_answer in current_group_answers:
            if letter not in current_answer:
                letter_score = 0
        group_score += letter_score
    return group_score

scores = []
current_group = set()
current_group_answers = []
for group in groups:
    if group != '\n':
        group_elements = list(group.strip())
        for element in group_elements:
            current_group.add(element)
        current_group_answers.append(group.strip())
    else:
        group_score = score_group(current_group_answers, current_group)
        scores.append(group_score)
        current_group = set()
        current_group_answers = []
group_score = score_group(current_group_answers, current_group)
scores.append(group_score)

print(sum(scores))

