from data_read import read_file

import networkx as nx

import numpy as np

map_raw = read_file("12.txt")

map=[]

map_nodes = {}

for idx, line in enumerate(map_raw):
    current_line = line.strip()
    processed = []
    for jdx, element in enumerate(current_line):
        if element == "S":
            processed.append(1)
            start_position = (idx, jdx)
        elif element == "E":
            processed.append(26)
            end_position = (idx, jdx)
        else:
            processed.append(ord(element) - 96)
    map.append(processed)

map_data = np.array([m for m in map])

map_nodes = nx.grid_2d_graph(*map_data.shape)

map_nodes = map_nodes.to_directed()

graph = nx.DiGraph([(a,b) for a,b in map_nodes.edges() 
                if map_data[b] <= map_data[a]+1])

p = nx.shortest_path_length(graph, target=end_position)

print(p[start_position])



