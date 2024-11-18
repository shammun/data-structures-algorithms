import heapq
from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = set()
        self.shortcuts = set()
        self.concatenated_neighbors = 0
        self.shortcut_cover = 0
        self.level = 0
        self.importance = 0

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_nodes(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edges(self, node1, node2, distance):
        self.add_node(node1)
        self.add_node(node2)
        self.nodes[node1].neighbors.add(node2)
        self.nodes[node2].neighbors.add(node1)
        self.edges[(node1, node2)] = distance
        self.edges[(node2, node1)] = distance

    def remove_node(self, node):
        if node in self.nodes:
            for neighbor in self.nodes[node].neighbors:
                self.nodes[neighbor].neighbors.remove(node)
            del self.nodes[node]

    def add_shortcut(self, node1, node2, distance):
        self.nodes[node1].shortcuts.add(node2)
        self.nodes[node2].shortcuts.add(node1)
        self.edges[(node1, node2)] = distance
        self.edges[(node2, node1)] = distance

def euclidean_distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def compute_importance(node, graph):
    ed = len(node.shortcuts) - len(node.neighbors)
    importance = ed + node.concatenated_neighbors + node.shortcut_cover + node.level
    return importance

def update_node_importance(node, graph):
    node.importance = compute_importance(graph, node)

def witness_path(graph, u, v, excluded_node):
    dist = defaultdict(lambda: float('inf'))
    dist[u] = 0
    pq = [(0, u)]

    while pq:
        d, node = heapq.heappop(pq)
        if node == v:
            return d <= graph.edges.get((u, v), float('inf'))
        if d > dist[node]:
            continue
        for neighbor in graph.nodes[node].neighbors | graph.nodes[node].shortcuts:
            if neighbor != excluded_node:
                new_dist = d + graph.edges[(node, neighbor)]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

    return False

def check_connectivity(graph, start, goal):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node == goal:
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(graph.nodes[node].neighbors)
    return False

def contract_node(graph, node, start, goal):
    if node not in graph.nodes:
        return False
    print(f"Contracting node: {node}")

    if not check_connectivity(graph, start, goal):
        print(f"Cannot contract node {node} as it would disconnect the graph.")
        return False
    
    for u in graph.nodes[node].neighbors:
        for v in graph.nodes[node].neighbors:
            if u != v:
                if not witness_path(graph, u, v, node):
                    distance = graph.edges[(u, node)] + graph.edges[(node, v)]
                    graph.add_shortcut(u, v, distance)
                    graph.nodes[u].shortcut_cover += 1
                    graph.nodes[v].shortcut_cover += 1

    for neighbor in graph.nodes[node].neighbors:
        graph.nodes[neighbor].contracted_neighbors += 1
        graph.nodes[neighbor].level = max(graph.nodes[neighbor].level, graph.nodes[node].level + 1)
        update_node_importance(graph.nodes[neighbor], graph)

    graph.remove_node(node)
    print(f"Node {node} contracted")
    return True

def preprocess_graph(graph, avoid_nodes, start, goal, max_contractions=3):
    pq = [(compute_importance(node, graph), node.value) for node in graph.nodes.values() if node.value not in avoid_nodes]
    heapq.heapify(pq)

    contractions = 0
    non_contractible_nodes = set()

    while pq and contractions < max_contractions:
        _, node_value = heapq.heappop(pq)

        if node_value not in graph.nodes or node_value in avoid_nodes or node_value in non_contractible_nodes:
            continue

        if not contract_node(graph, node_value, start, goal):
            non_contractible_nodes.add(node_value)
            continue

        contractions += 1
        pq = [(compute_importance(node, graph), node.value) for node in graph.nodes.values() 
              if node.value not in avoid_nodes and node.value not in non_contractible_nodes]
        heapq.heapify(pq)

def bidirectional_dijkstra(graph, start, goal):
    if start == goal:
        return [start], 0
        
    forward_dist = {start: 0}
    backward_dist = {goal: 0}
    forward_parent = {}
    backward_parent = {}
    forward_pq = [(0, start)]
    backward_pq = [(0, goal)]
    forward_visited = set()
    backward_visited = set()

    def process_node(dist, parent, pq, visited, current, direction):
        visited.add(current)

        for neighbor in graph.nodes[current].neighbors | graph.nodes[current].shortcuts:
            new_dist = dist[current] + graph.edges[(current, neighbor)]

            if neighbor not in dist or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))

        if current in (forward_visited if direction == "backward" else backward_visited):
            return current
        return None
        
    meeting_node = None

    while forward_pq and backward_pq:
        _, current_forward = heapq.heappop(forward_pq)
        meeting_node = process_node(forward_dist, forward_parent, forward_pq, forward_visited, current_forward, "forward")
        if meeting_node:
            break

        _, current_backward = heapq.heappop(backward_pq)
        meeting_node = process_node(backward_dist, backward_parent, backward_pq, backward_visited, current_backward, "backward")
        if meeting_node:
            break

    if meeting_node is None:
        return None, float('inf')
        
    path = []
    current = meeting_node
    while current != start:
        path.append(current)
        current = forward_parent[current]
        path.append(current)
    path.append(start)
    path = path[::-1]

    current = meeting_node
    while current != goal:
        current = backward_parent[current]
        path.append(current)

    total_distance = forward_dist[meeting_node] + backward_dist[meeting_node]
    return path, total_distance
    
def main():
    graph = Graph()

    n, m = map(int, input().split())

    print("Enter point coordinates (x, y)")

    nodes = []
    for _ in range(n):
        x, y = map(int, input().split())
        coord = (x, y)
        nodes.append(coord)
        graph.add_nodes(coord)

    print("Enter edges")

    for _ in range(m):
        u, v = map(int, input().split())
        distance = euclidean_distance(nodes[u], nodes[v])
        graph.add_edge(nodes[u], nodes[v], distance)

    print("Preprocessing graph...")

    start_x, start_y = map(int, input("Enter start coordinates (x, y): ").split())
    goal_x, goal_y = map(int, input("Enter goal coordinates (x, y): ").split())

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    avoid_nodes = {start, goal}

    preprocess_graph(graph, avoid_nodes, start, goal, max_contractions=3)
    print("Preprocessing complete.")

    print("Nodes in graph:", list(graph.nodes.keys()))
    print("Edges in graph:", list(graph.edges.keys()))

    path, distance = bidirectional_dijkstra(graph, start, goal)

    if path:
        print(f"Shortest path: {path}")
        print(f"Distance: {distance}")
    else:
        print("No path found")

if __name__ == "__main__":
    main()
        


"""


8 10
Enter point coordinates (x, y)
0 0
1 1
2 0
2 2
3 1
4 2
5 0
5 2
Enter edges
0 1
0 2
1 2
1 3
2 3
3 4
3 5
4 5
4 6
5 7
Selected 4 landmarks on the border
Enter start coordinates (x, y): 0 0
Enter goal coordinates (x, y)5 0


Output:

Preprocessing graph...
Enter start coordinates (x, y): 0 0
Enter goal coordinates (x, y): 5 0
Contracting node: (2, 2)
Node (2, 2) contracted.
Contracting node: (5, 2)
Cannot contract node (5, 2) as it would disconnect the graph.
Contracting node: (2, 0)
Cannot contract node (2, 0) as it would disconnect the graph.
Contracting node: (4, 2)
Cannot contract node (4, 2) as it would disconnect the graph.
Contracting node: (1, 1)
Cannot contract node (1, 1) as it would disconnect the graph.
Contracting node: (3, 1)
Cannot contract node (3, 1) as it would disconnect the graph.
Preprocessing complete.
Nodes in graph: [(0, 0), (1, 1), (2, 0), (3, 1), (4, 2), (5, 0), (5, 2)]
Edges in graph: [((0, 0), (1, 1)), ((1, 1), (0, 0)), ((0, 0), (2, 0)), ((2, 0), (0, 0)), ((1, 1), (2, 0)), ((2, 0), (1, 1)), ((1, 1), (2, 2)), ((2, 2), (1, 1)), ((2, 0), (2, 2)), ((2, 2), (2, 0)), ((2, 2), (3, 1)), ((3, 1), (2, 2)), ((2, 2), (4, 2)), ((4, 2), (2, 2)), ((3, 1), (4, 2)), ((4, 2), (3, 1)), ((3, 1), (5, 0)), ((5, 0), (3, 1)), ((4, 2), (5, 2)), ((5, 2), (4, 2)), ((3, 1), (1, 1)), ((1, 1), (3, 1))]
Shortest path: [(0, 0), (1, 1), (3, 1), (5, 0)]
Distance: 6.4787086646190755

"""
        
