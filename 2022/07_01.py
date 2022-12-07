from data_read import read_file

terminal = read_file("07.txt")

class Node:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.sizes = []
        self.nodes = []
        self.size = 0
        self.parent = "/"

    def add_file(self, filename, filesize):
        self.files.append(filename)
        self.sizes.append(filesize)
        self.size += filesize

    def add_node(self, node):
        self.nodes.append(node)

    def print_files(self):
        for idx, file in enumerate(self.files):
            print(f"{file} (file, size={self.sizes[idx]})")

    def calculate_size(self):
        child_sizes = [child.calculate_size() for child in self.nodes]
        return sum(child_sizes) + self.size

    def __repr__(self):
        return f"Node '{self.name}', L={len(self.files)}"

nodes = dict()
root_node = Node("None-/")
root_node.parent="Sausage"
nodes["None-/"] = root_node
current_node = None
mode = 0

for line in terminal:
    line = line.strip().split()
    if line[0] == "$":
        mode = 0
        # command
        if line[1] == "cd":
            # change directory
            if line [2] == "..":
                current_node = nodes[current_node].parent.name
            else:
                current_node = f"{current_node}-{line[2]}"
        elif line[1] == "ls":
             # listing
            mode = 1
    elif line[0] == "dir":
        # dir present, add new child
        new_name = f"{current_node}-{line[1]}"
        new_node = Node(new_name)
        new_node.parent = nodes[current_node]
        nodes[new_name] = new_node
        nodes[current_node].add_node(nodes[new_name])
    else:
        # add file to current node
        nodes[current_node].add_file(line[1], int(line[0]))
        
total = 0

for node_name, node in nodes.items():
    current_size = node.calculate_size()
    if current_size <=100000:
        total += current_size
    # node.print_files()

print(total)

# 1153329 - too low
# 1127800 - too low