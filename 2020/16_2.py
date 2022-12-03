import pathlib

""" Day 16 code.  This is -not- pretty, and I'm sure it could be done in
far fewer lines of code.  BUT it's all my own work, worked out from scratch,
and worked FIRST TIME on the real data, so I'm really pleased with it."""

file_name = "16.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    ticket_info = [ticket_info.strip() for ticket_info in file.readlines()]

split_1 = ticket_info.index("")
ticket_info[split_1] = 'x'
split_2 = ticket_info.index("")
ticket_rules = ticket_info[:split_1]
my_ticket_info = ticket_info[split_1 + 2]
near_tickets_info = ticket_info[split_2 + 2:]

rules = {}
all_invalid = []

def check_ticket(ticket, rules):
    invalid = []
    for my_value in ticket:
        ok = False
        for k,v in rules.items():
            for values in v:
                if my_value in range(values[0], values[1] + 1):
                    ok = True
        if not ok:
            invalid.append(my_value)
    return invalid

def return_valid_rules(ticket, rules):
    ticket_valid = []
    for my_value in ticket:
        value_valid = []
        for k,v in rules.items():
            for values in v:
                if my_value in range(values[0], values[1] + 1):
                    value_valid.append(k)
        ticket_valid.append(value_valid)
    return ticket_valid

# load rules into dict
for ticket in ticket_rules:
    name, rule = ticket.split(":")
    rule = rule.split(" ")
    name = name.replace(" ", "_")
    r1 = list(map(int, rule[1].split('-')))
    r2 = list(map(int, rule[3].split('-')))
    rules[name] = [r1, r2]

# check my ticket
my_ticket = list(map(int, my_ticket_info.split(',')))
print(check_ticket(my_ticket, rules))

# check and remove invalid tickets
valid_nearby = []
for near_ticket in near_tickets_info:
    near_ticket = list(map(int, near_ticket.split(',')))
    if len(check_ticket(near_ticket, rules)) == 0:
        valid_nearby.append(near_ticket)

# list of sets, length of rules list
all_valid_ticket_rules = []
for valid_ticket in valid_nearby:
    valid_rules_list = return_valid_rules(valid_ticket, rules)
    all_valid_ticket_rules.append(valid_rules_list)


# find out ticket rules possible for each column
columns = []
for idx in range(len(all_valid_ticket_rules[0])):
    current = []
    for jdx in range(len(all_valid_ticket_rules)):
        current.append(set(all_valid_ticket_rules[jdx][idx]))

    columns.append((idx, set.intersection(*current)))

# create dict with fewest options at start
col_dict = {len(column[1]): column for column in columns}

# algorithm to find columns that match
used = []
final_columns = {}
for idx in range(1,21):
    columns = col_dict[idx][1]
    for column in columns:
        if column not in used:
            final_columns[col_dict[idx][0]] = column
            used.append(column)
            break

# find columns from data that are required, and add them to a list
print("Columns with departure in them:")
my_column_values = []
for k, v in final_columns.items():
    if 'departure' in v:
        print(f"{k} : {v}")
        print(f"My value: {my_ticket[k]}")
        my_column_values.append(my_ticket[k])

# multiply my values together
total = 1
for value in my_column_values:
    total *= value

print(f"Final value: {total}")