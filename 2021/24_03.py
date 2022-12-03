from data_read import read_file
program = [inst.strip().split() for inst in read_file("24.txt")]


def get_inp():
    global test_value
    # print(f"{test_value=}")
    num = int(test_value[0])
    test_value = test_value[1:]
    # print(f"Entering {num}")
    return num

def run_program(program):
    w, x, y, z, = 0, 0, 0, 0
    for idx in range(0, len(program), 18):
        # print(program[idx],program[idx + 4],program[idx + 5],program[idx + 15])

        # get input number
        w = get_inp()
        z *= 26
        z += w + int(program[idx+15][2])
    return z

value = 99999999999999

running = True
while running:
    test_value = str(value)
    if '0' in test_value:
        value -= 1
        continue
    if value % 9999 == 0:
        print(f"Testing {test_value}")
    result = run_program(program)
    if result == 0:
        running = False

    value -= 1

print(f"Highest Value = {value + 1}")