from data_read import read_file
from tqdm import tqdm

area = read_file("17.txt")

area = area[0].split()[2:]


def get_coords(list_item):
    coords = list_item.split("..")
    coords[0] = int(coords[0][2:])
    coords[1] = int(coords[1].strip(","))
    return coords


def run_trial(x_vel, y_vel, x_coords, y_coords):
    running = True
    location = [0, 0]
    max_y = 0
    while running:

        location[0] += x_vel
        location[1] += y_vel
        max_y = max(location[1], max_y)

        if (x_coords[0] <= location[0] <= x_coords[1]) and (
            y_coords[0] <= location[1] <= y_coords[1]
        ):
            return True, max_y

        if location[0] > x_coords[1]:
            running = False
        if location[1] < y_coords[0]:
            running = False

        y_vel -= 1
        try:
            x_vel -= x_vel / abs(x_vel)
        except ZeroDivisionError:
            x_vel = 0

    return False, max_y


x_coords = get_coords(area[0])
y_coords = get_coords(area[1])

velocity_list = [
    [x, y] for x in range(x_coords[1] + 1) for y in range(y_coords[0], 500)
]

success_list = []
for x_vel, y_vel in tqdm(velocity_list):
    success, max_y = run_trial(x_vel, y_vel, x_coords, y_coords)
    if success:
        success_list.append(max_y)

print(f"Part 1: Max Y Height: {max(success_list)}")
print(f"Part 2: Number of Successful Throws: {len(success_list)}")
