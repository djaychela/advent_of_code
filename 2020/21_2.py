import pathlib

file_name = "21.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    foods = [food.strip() for food in file.readlines()]

allergen_dict = {}
all_ingredients = set()

for food in foods:
    ingredients, contains = food.split("(")
    ingredients_list = set(ingredients.split(" ")[:-1])
    for ingredient in ingredients_list:
        all_ingredients.add(ingredient)
    contains = contains.replace("contains ", "")
    contains = contains.replace(")", "")
    contains_list = contains.split(",")
    for content in contains_list:
        content = content.strip()
        if content in allergen_dict.keys():
            allergen_dict[content].append(ingredients_list)
        else:
            allergen_dict[content] = [ingredients_list]

known_allergen_dict = {}
unknown_allergens = list(allergen_dict.keys())

solved = False

while not solved:
    if len(unknown_allergens) == 0:
            break
    for content in unknown_allergens:
        solved = True
        
        food = set.intersection(*allergen_dict[content])
        if len(food) == 1:
            food_value = food.pop()
            known_allergen_dict[content] = food_value
            solved = False
            for k,v in allergen_dict.items():
                for v_list in v:
                    if food_value in v_list:
                        v_list.remove(food_value)
            unknown_allergens.remove(content)
            break

print(list(known_allergen_dict.keys()))
sorted_allergen_keys = sorted(list(known_allergen_dict.keys()))
canonical = [known_allergen_dict[allergen] for allergen in sorted_allergen_keys]

print(",".join(canonical))






