import os

path = os.path.join(os.getcwd(), "data", "test_16b_1.txt")
with open(path, "r") as f:
    data = f.readlines()

data = data[0].rstrip()
initial_signal = [int(d) for d in data]
input_signal = []
for k in range(10000):
    for i in initial_signal:
        input_signal.append(i)
        
print('duplication complete.')
base_pattern = [0,1,0,-1]
phases = 100

for p in range(phases):
    output = []
    for jdx in range(1, len(input_signal)+1):
        pattern = []
        for b in base_pattern:
            for _ in range(jdx):
                pattern.append(b)
        while len(pattern) <= len(str(input_signal)):
            pattern += pattern
        
        total = 0
        for idx, i in enumerate(input_signal,1):
            total += i * pattern[idx]

        output.append(int(str(abs(total))[-1]))

    # print(p, output)
    print(p)
    input_signal = output.copy()
print(output[:8])