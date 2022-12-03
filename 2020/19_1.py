import pathlib
from itertools import combinations

file_name = "19_test.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    received = [line.strip() for line in file.readlines()]

splitpoint = received.index('')

rules = received[:splitpoint]
messages = received[splitpoint + 1:]

rules_dict = {}
complete = {}

# find letters
for rule in rules:
    index, content = rule.split(": ")
    if content[0] == '"':
        rules_dict[index] = content[1]
        complete[index] = True

print(complete)
print(complete.keys())

# parse rules into rules dict
for rule in rules:
    index, content = rule.split(": ")
    print(index, content)
    if content[0] == '"':
        continue
    else:
        content = content.split("|")
        content = [[co for co in cont if co != " "] for cont in content]
        # split on or terminator into two different lists
    rules_dict[index] = content

# replace rules with known info
all_done = False
passes = 0
while not all_done:
    passes +=1
    for k, v in rules_dict.items():
        if k in complete.keys():
            continue
        current_rules_list = []
        for rule in v:
            current_rule = []
            for fragment in rule:
                print(f"frag: {fragment}")
                if fragment in complete.keys():
                    current_rule.append(rules_dict[fragment])
                else:
                    current_rule.append(fragment)
            current_rules_list.append(current_rule)
        rules_dict[k] = current_rules_list
    
    # check for any completed, mark as complete in complete dict
    all_done = True
    for k,v in rules_dict.items():
        if k in complete.keys():
            continue
        done = True
        for rule in v:
            for fragment in rule:
                print(f"checkfrag: {fragment}")
                if fragment not in ['a','b']:
                    done = False
                    all_done = False
        if done:
            complete[k] = True        

            
    print(f"Results after {passes}")
    print(rules_dict)
