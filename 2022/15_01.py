from data_read import read_file

from datetime import datetime

sensor_raw = read_file("15.txt")

def manhattan(p, q):
    distance = 0
    for p_i,q_i in zip(p,q):
        # print(f"{p=} {q=} {p_i=} {q_i=}")
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

# find minimum x scan value
min_x = 2000000
max_x = 0
for sensor in sensors:
    min_x = min(min_x, sensor.min_x())
    max_x = max(max_x, sensor.max_x())
print(min_x, max_x)


locations = []
start = datetime.now()
for x in range(min_x, max_x):
    location = (x, 2000000)
    locations.append(check_coord_2(location, sensors))
    
print(datetime.now() - start)
print(sum(locations))
