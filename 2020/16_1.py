import pathlib

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

# load rules into dict
for ticket in ticket_rules:
    name, rule = ticket.split(":")
    rule = rule.split(" ")
    name = name.replace(" ", "_")
    r1 = list(map(int, rule[1].split('-')))
    r2 = list(map(int, rule[3].split('-')))
    rules[name] = [r1, r2]

# check my ticket
my_ticket = map(int, my_ticket_info.split(','))
print(check_ticket(my_ticket, rules))

# check nearby tickets
for near_ticket in near_tickets_info:
    near_ticket = map(int, near_ticket.split(','))
    all_invalid.extend(check_ticket(near_ticket, rules))

print(sum(all_invalid))


