from data_read import read_file

hashes_raw = read_file("15.txt")

def return_hash(chars):
    current_value = 0
    for char in chars:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

def show_boxes(boxes):
    for idx, box in enumerate(boxes):
        if len(box) > 0:
            print(f"{idx}: {box}")

def find_lens_index(current_contents, lens_label):
    # print(f"{current_contents=}, {lens_label=}")
    for idx, lens in enumerate(current_contents):
        if lens.split("=")[0] == lens_label:
            return idx

def get_box_scores(current_contents):
    score = 0
    for idx, lens in enumerate(current_contents, 1):
        focal_length = int(lens.split("=")[1])
        score += idx * focal_length
    return score


total = 0

boxes = []

for i in range(256):
    boxes.append([])

for chars in hashes_raw[0].strip().split(","):
    hashable = chars.replace("-", "=").split("=")[0]
    box = return_hash(hashable)
    # print(f"{chars=} : {return_hash(hashable)}")
    if "=" in chars:
        current_contents = boxes[box]
        lens_index = find_lens_index(current_contents, hashable)
        if lens_index is not None:
            # print("Replacing Lens..")
            # print(f"{current_contents=}")
            current_contents[lens_index] = chars
            # print(f"{current_contents=}")
            # wait = input("Press a key...")
        else:
            current_contents.append(chars)
        boxes[box] = current_contents
    elif "-" in chars:
        current_contents = boxes[box]
        lens_index = find_lens_index(current_contents, hashable)
        if lens_index is not None:
            # print(f"Lens Already Present at index {lens_index}")
            # print(f"{current_contents=}")
            del(current_contents[lens_index])
            # print(f"{current_contents=}")
            # wait = input("Press a key...")
            boxes[box] = current_contents

show_boxes(boxes)
        
# score boxes
score = 0
for idx, box in enumerate(boxes, 1):
    current_box_score = get_box_scores(box)
    score += current_box_score * idx
    if len(box) > 0:
        print(f"Box {idx - 1}: {current_box_score * idx}")

print(f"Score: {score}")

# 6287832 - too high
""" 248279 - correct!  Had used if lens[:2] == lens_label instead of 
    :if lens.split("=")[0] == lens_label, leading to multiple lenses in the same box!
    You know what they say about assumptions!!!"""