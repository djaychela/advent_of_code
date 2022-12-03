import numpy as np

from data_read import read_file
from math import sqrt
from collections import defaultdict

from dataclasses import dataclass, field
from typing import List

ROTATIONS = np.array([
    [[1,0,0],[0,1,0],[0,0,1]],
    [[-1,0,0],[0,-1,0],[0,0,1]],
    [[-1,0,0],[0,1,0],[0,0,-1]],
    [[1,0,0],[0,-1,0],[0,0,-1]],
    [[-1,0,0],[0,0,1],[0,1,0]],
    [[1,0,0],[0,0,-1],[0,1,0]],
    [[1,0,0],[0,0,1],[0,-1,0]],
    [[-1,0,0],[0,0,-1],[0,-1,0]],
    [[0,-1,0],[1,0,0],[0,0,1]],
    [[0,1,0],[-1,0,0],[0,0,1]],
    [[0,1,0],[1,0,0],[0,0,-1]],
    [[0,-1,0],[-1,0,0],[0,0,-1]],
    [[0,1,0],[0,0,1],[1,0,0]],
    [[0,-1,0],[0,0,-1],[1,0,0]],
    [[0,-1,0],[0,0,1],[-1,0,0]],
    [[0,1,0],[0,0,-1],[-1,0,0]],
    [[0,0,1],[1,0,0],[0,1,0]],
    [[0,0,-1],[-1,0,0],[0,1,0]],
    [[0,0,-1],[1,0,0],[0,-1,0]],
    [[0,0,1],[-1,0,0],[0,-1,0]],
    [[0,0,-1],[0,1,0],[1,0,0]],
    [[0,0,1],[0,-1,0],[1,0,0]],
    [[0,0,1],[0,1,0],[-1,0,0]],
    [[0,0,-1],[0,-1,0],[-1,0,0]],
])

scanner_data = read_file("19_test_3.txt")

scanner_data = [scanner.strip() for scanner in scanner_data]

scanners = []
current_scanner = []
for scanner in scanner_data:
    if scanner == "":
        scanners.append(current_scanner)
        current_scanner = []
    elif scanner[:2] != "--":
        scanner_coords = list(map(int, scanner.split(",")))
        current_scanner.append(scanner_coords)


@dataclass
class Scanner:
    beacons: list = field(default=list)
    vectors: list = field(default_factory=list, init=False)
    solved: bool = False

    def __post_init__(self):
        for idx, beacon_1 in enumerate(self.beacons):
            distances = []
            for jdx, beacon_2 in enumerate(self.beacons):
                if idx == jdx:
                    continue
                current_vector = sqrt(
                        (beacon_1[0] - beacon_2[0]) ** 2
                        + (beacon_1[1] - beacon_2[1]) ** 2
                        + (beacon_1[2] - beacon_2[2]) ** 2
                    )
                distances.append(current_vector)
            distances = sorted(distances)
            self.vectors.append(distances)
    
    def __repr__(self):
        return f"{self.beacons}"

    def check_matches(self, other_scanner: "Scanner"):
        match_dict = {}
        for idx in range(len(self.vectors)):
            for jdx in range(len(other_scanner.vectors)):
                matches = 0
                if idx in match_dict:
                    break
                for k in range(12):
                    if self.vectors[idx][k] == other_scanner.vectors[jdx][k]:
                        matches += 1
                if matches > 1:
                    match_dict[idx] = jdx
        if len(match_dict) < 12:
            return False, {}
        return True, match_dict

    def rotate_and_match(self, other: "Scanner"):
        for s_beacon in self.beacons:
            print(s_beacon)
            for rotation in ROTATIONS:
                rot_off = []
                for o_beacon in other.beacons:
                    o_rotated = (o_beacon * rotation).sum(axis = 0)
                    # print(t_rotated, o_beacon, s_beacon)
                    # exit()
                    t_x_offset = s_beacon[0] - o_rotated[0]
                    t_y_offset = s_beacon[1] - o_rotated[1]
                    t_z_offset = s_beacon[2] - o_rotated[2]
                    rot_off.append([t_x_offset, t_y_offset, t_z_offset])
                    # create list of lists of offsets
                    # if 12 offsets are the same, matched.

                    # print(f"Testing rotation {rotation}")
                    if t_x_offset == x_offset and t_y_offset == y_offset and t_z_offset == z_offset:
                        t_matches += 1
                    if t_matches == 11:
                        print("matches found!!!!")
                        print(rotation)
                        exit()
                    if t_matches != 0:
                        print("Bueller.")
                    # x_offset = s_beacon[0] - t_beacon[0]
                    # y_offset = s_beacon[1] - t_beacon[1]
                    # z_offset = s_beacon[2] - t_beacon[2]
                    # pick the location
                    # check the difference between self and other
        pass

    
scanner_list = []
for scanner in scanners:
    scanner_list.append(Scanner(scanner))
print(f"Number of Scanners: {len(scanner_list)}")

scanner_list[0].solved = True

# print(scanner_list[0])
# scanner_list[0].rotate_and_match(scanner_list[1])

# exit()

matches = defaultdict(list)
match_vectors = defaultdict(list)

for idx, scanner in enumerate(scanner_list):
    for jdx, scan_2 in enumerate(scanner_list):
        if idx == jdx:
            continue
        match, match_dict = scanner.check_matches(scan_2)
        if match:
            matches[idx].append(jdx)
            match_vectors[idx].append(match_dict)

for matched_scanner in matches.keys():
    print(f"**** {matched_scanner} has {len(matches[matched_scanner])} matches:")
    print(matches[matched_scanner])
    print(match_vectors[matched_scanner])



                
