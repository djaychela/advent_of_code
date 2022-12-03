from collections import Counter

from data_read import read_file

digits = read_file("08.txt")

digits = [(digit.split("|")[0].strip(), digit.split("|")[1].strip()) for digit in digits]

seven_seg = {"abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
    }

total = 0

def match_length(counter, match):
    output = {k for k,v in counter.items() if v == match}
    return output

for display in digits:
    output = ""
    key = Counter(display[0])
    key_len_dict = {len(key): key for key in display[0].split()}
    del key[" "]
    key_rev = {v: k for k,v in key.items()}
    translation = {}
    p_8 = match_length(key, 8)
    p_7 = match_length(key, 7)
    one = {k for k in key_len_dict[2]}
    four = {k for k in key_len_dict[4]}
    translation['b'] = key_rev[6]
    translation['e'] = key_rev[4]
    translation['f'] = key_rev[9]
    translation['c'] = ''.join(p_8 & one) # P8 and in 1 == c
    translation['a'] = ''.join(p_8 - one) # P8 and not in 1 == a
    translation['d'] = ''.join(p_7 & four) # P7 and in 4 == d
    translation['g'] = ''.join(p_7 - four) # P7 and not in 4 == g
    translation_2 = {v: k for k, v in translation.items()}
    # print(f"{translation = }")

    output_value = ""
    for number in display[1].split():
        translated = "".join(sorted([translation_2[n] for n in number]))
        # print(f"{number} -> {translated} -> {seven_seg[translated]}")
        output_value += str(seven_seg[translated])

    # print(int(output_value))
    total += int(output_value)


print(f"{total=}")

