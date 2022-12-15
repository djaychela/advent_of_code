from data_read import read_file

sensor_raw = read_file("15.txt")

def manhattan(p, q):
    distance = 0
    for p_i,q_i in zip(p,q):
        distance += abs(p_i - q_i)
    return distance

class Sensor():
    def __init__(self, s_x, s_y, b_x, b_y):
        self.s_x = s_x
        self.s_y = s_y
        self.b_x = b_x
        self.b_y = b_y
        self.man = manhattan((s_x, s_y), (b_x, b_y))

    def __repr__(self):
        return f"Sensor: ({self.s_x}:{self.s_y}) - Beacon ({self.b_x}:{self.b_y})  MD:{self.man}"

    def check_location(self, x, y):
        distance = 0
        for p_i,q_i in zip((x, y), (self.s_x, self.s_y)):
            distance += abs(p_i - q_i)
            if distance > self.man:
                return False
        return distance <= self.man

    def check_beacon(self, x, y):
        return (self.b_x == x and self.b_y == y)

    def min_x(self):
        return self.s_x - self.man - 1

    def max_x(self):
        return self.s_x + self.man + 1

    def next_x(self, x, y):
        # return next valid x position for a given x and y
        # check if location is in this sensor, return False if not
        if not self.check_location(x, y):
            return False
        # return next x co-ord that falls outside sensor range
        return self.s_x + self.man - abs(y - self.s_y) + 1


sensors = []
for sensor in sensor_raw:
    sensor_loc_str = sensor.split(":")[0].split("Sensor at ")[1]
    beacon_loc_str = sensor.split(":")[1].split("closest beacon is at ")[1].strip()
    sensor_loc_x = int(sensor_loc_str.split(", ")[0].split("x=")[1])
    sensor_loc_y = int(sensor_loc_str.split(", ")[1].split("y=")[1])
    beacon_loc_x = int(beacon_loc_str.split(", ")[0].split("x=")[1])
    beacon_loc_y = int(beacon_loc_str.split(", ")[1].split("y=")[1])
    current_sensor = Sensor(sensor_loc_x, sensor_loc_y, beacon_loc_x, beacon_loc_y)
    sensors.append(current_sensor)

def check_coord(location, sensors):
    beacon = any([sensor.check_beacon(*location) for sensor in sensors])
    if beacon:
        return False
    result = any([sensor.check_location(*location) for sensor in sensors])
    return result

def check_coord_2(location, sensors):
    for sensor in sensors:
        if sensor.check_beacon(*location):
            return False
    for sensor in sensors:
        if sensor.check_location(*location):
            return True
    return False

def check_coord_3(location, sensors):
    for sensor in sensors:
        if sensor.check_beacon(*location):
            return False
    for idx, sensor in enumerate(sensors):
        if sensor.check_location(*location):
            return idx
    return False

# sensor 6

print(sensors[6])
for i in range(-2,20):
    print(f"{i=}: {sensors[6].next_x(i, 8)=}")

# exit()

# scan_size = 20
scan_size = 4000000

loop = 0

for y in range(0, scan_size + 1): 
    print(f"Checking row {y=}")
    x = 0
    while x < scan_size:
        updated = False
        loop += 1
        # find index of first beacon to contain x and y
        sensor_idx = check_coord_3((x, y), sensors)
        next_x = sensors[sensor_idx].next_x(x, y)
        if next_x:
            updated = True
            x = next_x
        else:
            # move along 1 step
            x+=1
            continue
        
        # check current location
        if x < scan_size:
            print(f"Checking coord {x=}:{y=}")
            current_val = check_coord_2((x, y), sensors)
            print(f"Value = {current_val}")
            if not current_val:
                solution = (x * 4000000) + y
                print(solution)
                exit()








