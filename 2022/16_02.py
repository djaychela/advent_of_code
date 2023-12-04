from data_read import read_file

import networkx as nx

valves_raw = read_file("16.txt")

class Valve:
    def __init__(self, name, flow, connections, paths=None, state=False):
        self.name = name
        self.flow = flow
        self.connections = connections
        self.paths = paths
        self.state = state

    def __repr__(self) -> str:
        return f"""Valve [{self.name}], flow = {self.flow} : <{self.connections}>
                Paths: {self.paths}\n"""

    def calculate_flow(self, time):
        return self.flow * (30 - time)

valves = dict()
g = nx.Graph()

# create valves
for valve_data in valves_raw:
    valve, connections = valve_data.strip().split(";")
    valve_name = valve.split(" ")[1]
    valve_flow = int(valve.split("=")[1])
    valve_connections = connections.split("valve")[1].strip()
    if valve_connections[:2] == 's ':
        valve_connections = valve_connections[2:]
    valve_connections = valve_connections.split(", ")
    current_valve = Valve(valve_name, valve_flow, valve_connections)
    valves[valve_name] = current_valve
    for v in valve_connections:
        g.add_edge(valve_name, v)

# add connection info to valves from nx
for path in nx.all_pairs_shortest_path(g):
    # path[0] is name of node
    # path[1] is connection list
    current_dict = dict()
    for valve_name in valves.keys():
        current_dict[valve_name] = len(path[1][valve_name]) - 1
    if valves[path[0]].flow != 0 or path[0]=="AA":
        valves[path[0]].paths = current_dict
    else:
        valves[path[0]].paths = {}

print(valves)

best = 0
best_combo = {}

def find_best_combination(opened, flowed, valve, time_left):
    
    global best
    global best_combo

    if flowed > best:
        best = flowed
        best_combo = opened

    if time_left <= 0:
        return

    if valve not in opened:
        find_best_combination(opened.union([valve]), flowed + valves[valve].flow * time_left, valve, time_left - 1)
    else:
        for k in [x for x in valves[valve].paths.keys() if x not in opened]:
            find_best_combination(opened, flowed, k, time_left - valves[valve].paths[k])

find_best_combination(set(['AA']), 0, 'AA', 26)

print(f"Best Score: {best}")

# 1892 - too low

def find_best_combination(opened, flowed, current_room, depth_to_go, elephants_turn):
    global best
    if flowed > best:
        best = flowed

    if depth_to_go <= 0:
        return

    if current_room not in opened:
        find_best_combination(opened.union([current_room]), flowed + valves[current_room].flow * depth_to_go, current_room, depth_to_go - 1, elephants_turn)
        if not elephants_turn:
            find_best_combination(set([current_room]).union(opened), flowed + valves[current_room].flow * depth_to_go, 'AA', 25, True)
    else:
        for k in [x for x in valves[current_room].paths.keys() if x not in opened]:
            find_best_combination(opened, flowed, k, depth_to_go - valves[current_room].paths[k], elephants_turn)

find_best_combination(set(['AA']), 0, 'AA', 25, False)
print(best)