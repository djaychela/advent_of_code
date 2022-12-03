import os

path = os.path.join(os.getcwd(), "data", "input_14a.txt")
with open(path, "r") as f:
    data = f.readlines()

data = [d.rstrip() for d in data]

ingredients = []
results = []
for d in data:
    ingredient, result = d.split('=>')
    ingredients.append(ingredient)
    results.append(result)

print(ingredients)
print(results)