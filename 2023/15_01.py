from data_read import read_file

hashes_raw = read_file("15.txt")

def return_hash(chars):
    current_value = 0
    for char in chars:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

total = 0
for chars in hashes_raw[0].strip().split(","):
    total += return_hash(chars)
    print(f"{chars=} : {return_hash(chars)}")

print(f"Score: {total}")