import os

input_file_path = os.path.join(os.getcwd(), 'data', 'input_1a.txt')
output_file_path = os.path.join(os.getcwd(), 'data', 'output_1b.txt')

def calculate_fuel(mass):
    def fuel_calc(m):
        return max(0, int(mass / 3) - 2)
    fuel = fuel_calc(mass)
    fuel_total = fuel
    while fuel > 0:
        mass = fuel
        fuel = fuel_calc(mass)
        fuel_total += fuel
    return fuel_total

input_data = []
with open (input_file_path, 'r') as f:
    for line in f:
        input_data.append(int(line.rstrip()))

output = []
for num in input_data:
    output.append(calculate_fuel(num))

output = sum(output)

with open(output_file_path, 'w') as f:
    f.writelines(str(output))