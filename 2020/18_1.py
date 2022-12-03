import re
import pathlib

def evaluate(expression):
    if not (re.search(r"[\+\*]", expression)):
        return expression
    part = re.search(r"\d+[\+\*]\d+", expression).group(0)
    result = eval(part)
    expression = expression.replace(part, str(result), 1)
    return evaluate(expression)

def deal_with_brackets(expression):
    if not (re.search(r"[\(\)]", expression)):
        return evaluate(expression)
    deepest = re.search(r"\(([0-9 +*]+)\)", expression).group(1)
    result = evaluate(deepest)
    expression = expression.replace(f"({deepest})", str(result))
    return deal_with_brackets(expression)


file_name = "18.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    homework_list = [homework.strip() for homework in file.readlines()]

total = 0
for line in homework_list:
    line = line.replace(" ","")
    value = int(deal_with_brackets(line))
    total += value
    print(f"{line} -> {value}.  Total = {total}")

