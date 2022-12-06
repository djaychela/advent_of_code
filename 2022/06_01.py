from data_read import read_file

signal = read_file("06.txt")

signal = signal[0].strip()

for idx in range(len(signal)-3):
    chunk = signal[idx:idx+4]
    if len(set(chunk)) == 4:
        print(f"Found at {idx + 4}")
        break