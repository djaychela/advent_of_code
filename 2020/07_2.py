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
            number = 1
        colour = ' '.join(content.split()[1:3])
        inner_dict[colour]=number
    if outer not in all_bags.keys():
        all_bags[outer] = inner_dict

def number_of_bags_inside(bag_colour, bag_number):
    if bag_colour == "other bags.":
        return 0
    bag_contents = all_bags[bag_colour].items()
    number_of_bags = 0
    for colour, number in bag_contents:
        number_of_bags += number_of_bags_inside(colour, number)
    total_of_bags = bag_number + (bag_number * number_of_bags)
    return total_of_bags
            
print(number_of_bags_inside('shiny gold', 1) - 1)
    

