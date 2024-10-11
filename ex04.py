import uuid
import networkx as nx
import matplotlib.pyplot as plt

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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    labels = {node: data['label'] for node, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color="skyblue")
    plt.show()

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
draw_tree(root)