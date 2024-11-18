import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        distance = euclidean_distance(from_node, to_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

def euclidean_distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

class Landmark:
    def __init__(self, node):
        self.node = node
        self.distances = {}

    def precompute_distances(self, graph):
        open_set = [(0, self.node)]
        closed_set = set()
        while open_set:
            dist, current = heapq.heappop(open_set)
            if current in closed_set:
                continue
            self.distances[current] = dist
            closed_set.add(current)
            for neighbor in graph.edges[current]:
                if neighbor not in closed_set:
                    heapq.heappush(open_set, (dist + graph.distances[(current, neighbor)], neighbor))

def find_border_nodes(graph):
    min_x = min(node[0] for node in graph.nodes)
    max_x = max(node[0] for node in graph.nodes)
    min_y = min(node[1] for node in graph.nodes)
    max_y = max(node[1] for node in graph.nodes)
    
    border_nodes = [node for node in graph.nodes if 
                    node[0] in (min_x, max_x) or node[1] in (min_y, max_y)]
    return border_nodes

def select_landmarks(graph, num_landmarks):
    border_nodes = find_border_nodes(graph)
    
    if len(border_nodes) < num_landmarks:
        print(f"Warning: Not enough border nodes ({len(border_nodes)}) for requested landmarks ({num_landmarks})")
        num_landmarks = len(border_nodes)
    
    landmarks = []
    for i in range(num_landmarks):
        index = i * len(border_nodes) // num_landmarks
        landmark = Landmark(border_nodes[index])
        landmark.precompute_distances(graph)
        landmarks.append(landmark)
    
    return landmarks

def landmark_heuristic(v, t, landmarks):
    return max(max(abs(landmark.distances[t] - landmark.distances[v]),
                   abs(landmark.distances[v] - landmark.distances[t]))
               for landmark in landmarks)

def bidirectional_astar(graph, start, goal, landmarks):
    if start == goal:
        return [start], 0

    def astar(graph, start, goal, landmarks, forward=True):
        closed_set = set()
        open_set = {start}
        came_from = {}
        g_score = {start: 0}
        f_score = {start: landmark_heuristic(start, goal, landmarks)}
        open_heap = [(f_score[start], start)]

        while open_set:
            current = heapq.heappop(open_heap)[1]
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1] if forward else path, g_score[goal]
            
            open_set.remove(current)
            closed_set.add(current)

            for neighbor in graph.edges[current]:
                if neighbor in closed_set:
                    continue
                tentative_g_score = g_score[current] + graph.distances[(current, neighbor)]

                if neighbor not in open_set:
                    open_set.add(neighbor)
                elif tentative_g_score >= g_score.get(neighbor, float('inf')):
                    continue

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + landmark_heuristic(neighbor, goal, landmarks)

                heapq.heappush(open_heap, (f_score[neighbor], neighbor))

        return None, float('inf')

    forward_path, forward_cost = astar(graph, start, goal, landmarks, True)
    if forward_path:
        return forward_path, forward_cost

    backward_path, backward_cost = astar(graph, goal, start, landmarks, False)
    if backward_path:
        return backward_path[::-1], backward_cost

    return None, float('inf')

def main():
    graph = Graph()

    n, m = map(int, input().split())

    print("Enter point coordinates (x, y)")
    nodes = []
    for _ in range(n):
        x, y = map(int, input().split())
        coord = (x, y)
        nodes.append(coord)
        graph.add_node(coord)

    print("Enter edges (From one node to another)")
    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(nodes[u], nodes[v])

    num_landmarks = min(4, n)  # Use at least 4 landmarks or all nodes if less than 4
    landmarks = select_landmarks(graph, num_landmarks)

    print(f"Selected {len(landmarks)} landmarks on the border")

    start_x, start_y = map(int, input("Enter start coordinates (x y): ").split())
    goal_x, goal_y = map(int, input("Enter goal coordinates (x y): ").split())

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    path, distance = bidirectional_astar(graph, start, goal, landmarks)

    if path:
        print(f"Shortest path: {path}")
        print(f"Distance: {distance}")
    else:
        print("No path found")

if __name__ == "__main__":
    main()

"""
Example Input:

8 10
0 0
1 1
2 0
2 2
3 1
4 2
5 0
5 2
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
0 0
5 0

This input represents a graph with 8 nodes and 10 edges. The nodes are given as (x, y) coordinates, followed by the edges connecting these nodes. The start point is (0, 0) and the goal point is (5, 0).
"""