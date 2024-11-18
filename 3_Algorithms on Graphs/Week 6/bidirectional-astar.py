import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

def euclidean_distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def bidirectional_astar(graph, start, goal):
    if start == goal:
        return [start], 0

    def astar(graph, start, goal, forward=True):
        # Nodes that have been fully explored
        closed_set = set()
        # Nodes that have been discovered but not fully explored
        open_set = {start}
        # A dictionary to reconstruct the path
        came_from = {}
        # The cost to reach each node from the start
        g_score = {start: 0}
        # The estimated total cost from start to goal through each node
        f_score = {start: euclidean_distance(start, goal)}
        # A priority queue to efficiently select the most promising node
        open_heap = [(f_score[start], start)]

        # continue looping as long as open_set is not empty
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
                # Once a node is in the closed_set, we've already found the optimal path to it.
                if neighbor in closed_set:
                    continue
                
                # For a newly discovered neighbor (not in open_set), we don't have any previous 
                # path to compare with, so we always add it and update its score.
                # The g_score represents the actual cost of the path from the start node to the 
                # current node

                # This calculates the potential g_score for the neighbor if we reach it through 
                # the current node.
                tentative_g_score = g_score[current] + graph.distances[(current, neighbor)]

                if neighbor not in open_set:
                    open_set.add(neighbor)
                # When a neighbor is already in the open_set, it means we've 
                # found a path to this node before.
                # We need to check if the new path we've just found (represented 
                # by tentative_g_score) is better than the previously known path.
                elif tentative_g_score >= g_score.get(neighbor, float('inf')):
                    continue

                # the new path we've just found is better than the previously known path
                came_from[neighbor] = current

                # g_score[neighbor] is the actual cost to reach the neighbor 
                # (which we just calculated)
                g_score[neighbor] = tentative_g_score

                # The f_score is an estimate of the total cost of the path through a given node.
                # It's calculated as f(n) = g(n) + h(n), where:
                # g(n) is the actual cost from the start to node n (g_score)
                # h(n) is the heuristic estimate of the cost from n to the goal
                f_score[neighbor] = g_score[neighbor] + euclidean_distance(neighbor, goal)
                heapq.heappush(open_heap, (f_score[neighbor], neighbor))

        return None, float('inf')

    forward_path, forward_cost = astar(graph, start, goal, True)
    backward_path, backward_cost = astar(graph, goal, start, False)

    if forward_path and backward_path:
        # Find the meeting point
        meeting_point = None
        min_total_cost = float('inf')
        for node in set(forward_path) & set(backward_path):
            total_cost = euclidean_distance(start, node) + euclidean_distance(node, goal)
            if total_cost < min_total_cost:
                min_total_cost = total_cost
                meeting_point = node

        if meeting_point:
            forward_index = forward_path.index(meeting_point)
            backward_index = backward_path.index(meeting_point)
            return forward_path[:forward_index + 1] + backward_path[backward_index - 1::-1], min_total_cost

    return None, float('inf')

def main():
    graph = Graph()

    n, m = map(int, input().split())

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph.add_node(u)
        graph.add_node(v)
        graph.add_edge(u, v, w)

    start = int(input())
    goal = int(input())

    path, distance = bidirectional_astar(graph, start, goal)

    if path:
        print(f"Shortest path: {path}")
        print(f"Distance: {distance}")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
