import os

input_file_path = os.path.join(os.getcwd(), 'data', 'input_1a.txt')
output_file_path = os.path.join(os.getcwd(), 'data', 'output_1a.txt')

input_data = []
with open (input_file_path, 'r') as f:
    for line in f:
        input_data.append(int(line.rstrip()))

output = []
for num in input_data:
    output.append(int(num / 3) - 2)

output = sum(output)

with open(output_file_path, 'w') as f:
    f.writelines(str(output))