import uuid
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_final_tree(tree_root, visited_nodes):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    labels = {node: data['label'] for node, data in tree.nodes(data=True)}

    node_colors = [visited_nodes.get(node, '#D3D3D3') for node in tree.nodes]
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def bfs_visual(tree_root):
    queue = [tree_root]
    visited_nodes = {}
    color_scale = np.linspace(0.1, 1, 7)
    color_idx = 0

    while queue:
        current_node = queue.pop(0)
        color = plt.cm.Blues(color_scale[color_idx])
        color_hex = '#{:02x}{:02x}{:02x}'.format(int(color[0]*255), int(color[1]*255), int(color[2]*255))
        visited_nodes[current_node.id] = color_hex
        color_idx += 1
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    draw_final_tree(tree_root, visited_nodes)

def dfs_visual(tree_root):
    stack = [tree_root]
    visited_nodes = {}
    color_scale = np.linspace(0.1, 1, 7)
    color_idx = 0

    while stack:
        current_node = stack.pop()
        color = plt.cm.Greens(color_scale[color_idx])
        color_hex = '#{:02x}{:02x}{:02x}'.format(int(color[0]*255), int(color[1]*255), int(color[2]*255))
        visited_nodes[current_node.id] = color_hex
        color_idx += 1
        
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    draw_final_tree(tree_root, visited_nodes)

def create_heap(heap_type="min"):
    if heap_type == "min":
        root = Node(1)
        root.left = Node(3)
        root.right = Node(6)
        root.left.left = Node(5)
        root.left.right = Node(9)
        root.right.left = Node(8)
    elif heap_type == "max":
        root = Node(9)
        root.left = Node(7)
        root.right = Node(6)
        root.left.left = Node(5)
        root.left.right = Node(3)
        root.right.left = Node(2)
    else:
        raise ValueError("Використовуйте 'min' або 'max'")
    
    return root

heap_type = "min"  # або "max"
root = create_heap(heap_type)

print("BFS Visualization:")
bfs_visual(root)

print("DFS Visualization:")
dfs_visual(root)