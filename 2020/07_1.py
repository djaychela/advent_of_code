import pathlib

file_name = "07.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    bags = file.readlines()

all_bags = {}
for bag in bags:
    outer, inner = bag.split("contain")
    outer = ' '.join(outer.split()[:2])
    inner_dict = {}
    inner_contents = inner.split(',')
    for content in inner_contents:
        try:
            number = int(content.split()[0])
        except ValueError:
            number = 0
        colour = ' '.join(content.split()[1:3])
        inner_dict[colour]=number
    if outer not in all_bags.keys():
        all_bags[outer] = inner_dict


def find_contents(bag_colour):
    if bag_colour == "shiny gold":
        return True
    if bag_colour == "other bags.":
        return None
    bag_contents = all_bags[bag_colour].keys()
    content_returns = []
    for colour in bag_contents:
        content_returns.append(find_contents(colour))
    return any(content_returns)
            

print(all_bags)
total = 0
for colour in all_bags.keys():
    contents = find_contents(colour)
    if contents and colour !="shiny gold":
        print(f"{colour} : {all_bags[colour]} := {contents}")
        total += 1
    
print(total)
