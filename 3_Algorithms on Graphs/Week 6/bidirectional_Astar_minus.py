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

def bidirectional_astar(graph, start, goal):
    if start == goal:
        return [start], 0

    def astar(graph, start, goal, forward=True):
        closed_set = set()
        open_set = {start}
        came_from = {}
        g_score = {start: 0}
        f_score = {start: euclidean_distance(start, goal)}
        open_heap = [(f_score[start], start)]

        while open_set:
            current = heapq.heappop(open_heap)[1]
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1] if forward else path, g_score
            
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
                f_score[neighbor] = g_score[neighbor] + euclidean_distance(current, neighbor)

                heapq.heappush(open_heap, (f_score[neighbor], neighbor))

        return None, defaultdict(lambda: float('inf'))
    
    path_forward, g_score_forward = astar(graph, start, goal, True)
    path_backward, g_score_backward = astar(graph, goal, start, False)

    if path_forward and path_backward:
        meeting_points = set(path_forward).intersection(set(path_backward))
        if not meeting_points:
            return None, float('inf')
        
        meeting_point = min(meeting_points, key=lambda x: g_score_forward[x] + g_score_backward[x])

        # Get index of meeting point in both paths
        forward_index = path_forward.index(meeting_point)
        backward_index = path_backward.index(meeting_point)
        
        # We need to reverse the backward path to connect correctly
        backward_path_reversed = path_backward[:backward_index + 1][::-1]

        # Combine forward path up to meeting point and backward path from meeting point
        combined_path = path_forward[:forward_index + 1] + backward_path_reversed[1:]
        total_distance = g_score_forward[meeting_point] + g_score_backward[meeting_point]

        return combined_path, total_distance

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

    print()
    start_x, start_y = map(int, input("Enter start coordinates (x y): ").split())
    goal_x, goal_y = map(int, input("Enter goal coordinates (x y): ").split())

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    path, distance = bidirectional_astar(graph, start, goal)

    if path:
        print(f"Shortest path: {path}")
        print(f"Distance: {distance}")
    else:
        print("No path found")

if __name__ == "__main__":
    main()


"""
Sample Input:

Input 1:
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
"""