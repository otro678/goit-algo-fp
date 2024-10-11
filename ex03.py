import heapq
import networkx as nx
import matplotlib.pyplot as plt

def add_edge(graph, u, v, weight):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, weight))
    graph[v].append((u, weight))

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {}
add_edge(graph, 'A', 'B', 1)
add_edge(graph, 'A', 'C', 4)
add_edge(graph, 'B', 'C', 2)
add_edge(graph, 'B', 'D', 5)
add_edge(graph, 'C', 'D', 1)
add_edge(graph, 'C', 'E', 3)
add_edge(graph, 'D', 'E', 2)

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Відстань до {vertex}: {distance}")

def visualize_graph(graph, distances, start_vertex):
    G = nx.Graph()

    for u in graph:
        for v, weight in graph[u]:
            G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G)

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold', edge_color='gray')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    distance_labels = {node: f'{distances[node]}' for node in distances}
    offset = 0.1
    for node, (x, y) in pos.items():
        plt.text(x, y + offset, distance_labels[node], fontsize=10, color='red', ha='center')

    plt.title(f"Граф із відстанями від вершини {start_vertex}")
    plt.show()

visualize_graph(graph, distances, start_vertex)