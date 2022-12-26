from data_read import read_file

from functools import lru_cache

from collections import deque

blizzard_raw = read_file("24.txt")

x_limit = len(blizzard_raw[0].strip()) - 2
y_limit = len(blizzard_raw) - 2

blizzard_list = []

end_position = (x_limit - 1, y_limit)

start_position = (0, -1)


class Blizzard:
    def __init__(self, x, y, direction, x_limit, y_limit):
        self.x = x
        self.y = y
        self.direction = direction
        self.icon = direction
        self.x_limit = x_limit
        self.y_limit = y_limit

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        blizzard_types = ["<", ">", "^", "v"]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self._direction = directions[blizzard_types.index(value)]

    def __repr__(self):
        return f"B: [{self.x},{self.y}] -> {self.direction}"

    def calculate_position(self, time):
        x_pos = (self.x + (time * self.direction[0])) % x_limit
        y_pos = (self.y + (time * self.direction[1])) % y_limit
        return (x_pos, y_pos)


def view_blizzards(blizzard_list, wall_list, time, current_position):
    global x_limit, y_limit

    blizzard_coords = []
    blizzard_icons = []
    for blizzard in blizzard_list:
        blizzard_coords.append(blizzard.calculate_position(time))
        blizzard_icons.append(blizzard.icon)

    for row in range(-1, y_limit + 1):
        line = []
        for col in range(-1, x_limit + 1):
            if (col, row) == current_position:
                line.append("E")
            elif (col, row) == end_position:
                line.append("F")
            elif (col, row) in wall_list:
                line.append("#")
            elif (col, row) in blizzard_coords:
                line.append(blizzard_icons[blizzard_coords.index((col, row))])
            else:
                line.append(".")
                # empty_tiles += 1
        # line.append("#")
        print("".join(line))
    # print(f"Empty Tiles: {empty_tiles}")


@lru_cache
def build_blizzard_list(time):
    global blizzard_list

    blizzard_coords = []
    for blizzard in blizzard_list:
        blizzard_coords.append(blizzard.calculate_position(time + 1))

    return blizzard_coords


def find_locations(time, current_position):
    # find all possible locations from current position
    global blizzard_list
    global wall_list

    blizzard_coords = build_blizzard_list(time)

    possibles_list = []
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]]
    for direction in directions:
        possible_position = (
            current_position[0] + direction[0],
            current_position[1] + direction[1],
        )
        if -2 in possible_position:
            continue
        if possible_position in wall_list:
            continue
        if possible_position not in blizzard_coords:
            possibles_list.append(possible_position)

    return possibles_list


def create_walls(x_limit, y_limit):
    # print(x_limit, y_limit)
    walls_list = []
    for y in range(-1, y_limit + 1):
        for x in range(-1, x_limit + 1):
            if y == -1:
                if x == 0:
                    continue
                else:
                    walls_list.append((x, y))
            elif y == y_limit:
                if x == x_limit - 1:
                    continue
                else:
                    walls_list.append((x, y))
            else:
                if x == -1 or x == (x_limit):
                    walls_list.append((x, y))

    return walls_list


for rdx, line in enumerate(blizzard_raw):
    for cdx, cell in enumerate(line):
        blizzard_types = ["<", ">", "^", "v"]
        if cell in blizzard_types:
            current_blizzard = Blizzard(cdx - 1, rdx - 1, cell, x_limit, y_limit)
            blizzard_list.append(current_blizzard)

wall_list = create_walls(x_limit, y_limit)

searched_dict = {}
time = 0
search_list = [[0, [(0, -1)]]]


def bfs(start, end, time=0):
    queue = deque([start])
    while queue:
        seen = set()
        for _ in range(len(queue)):
            location = queue.popleft()
            # print(f"{location=}")
            if location == end:
                return time
            for possible in find_locations(time, location):
                if possible not in seen:
                    seen.add(possible)
                    queue.append(possible)
        time += 1
        if time % 100 == 0:
            print(f"{time=}")
    return time


first = bfs(start_position, end_position)
print(f"Part 1: {first}")
second = bfs(end_position, start_position, first)
print(second)
third = bfs(start_position, end_position, second)
print(f"Part 2: {third}")
