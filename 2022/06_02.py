from data_read import read_file

signal = read_file("06.txt")

signal = signal[0].strip()

for idx in range(len(signal)-3):
    chunk = signal[idx:idx+14]
    if len(set(chunk)) == 14:
        print(f"Found at {idx + 14}")
        break