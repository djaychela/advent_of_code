from data_read import read_file
from collections import defaultdict
from copy import deepcopy

graph_data = read_file("12_test_3.txt")

graph_data = [node.strip() for node in graph_data]

node_names = {node_name for node_info in graph_data for node_name in node_info.split("-")}
graph_edges = [(edge.split("-")) for edge in graph_data]

graph_edge_dict = defaultdict(list)
for edge in graph_edges:
    graph_edge_dict[edge[0]].append(edge[1])
    graph_edge_dict[edge[1]].append(edge[0])

nodes = {}
for node in node_names:
    if node == node.upper():
        nodes[node] = 1000
    elif node in ["start", "end"]:
        nodes[node] = 0
    else:
        nodes[node] = 1

number_of_paths = 0

def find_connections(current_node, node_dict, graph_edge_dict, current_path):
    global number_of_paths
    node_dict[current_node] -= 1
    node_dict["parent_path"] = current_path
    for edge in graph_edge_dict[current_node]:
        if edge == "end":
            # print(f"**** Path Found: {current_path},{edge}")
            number_of_paths += 1
            continue
        if node_dict[edge] >= 1:
            old_id = id(node_dict)
            new_node_dict = deepcopy(node_dict)
            find_connections(edge, new_node_dict, graph_edge_dict, f"{current_path},{edge}")

find_connections('start', nodes, graph_edge_dict, "start")
print(number_of_paths)

