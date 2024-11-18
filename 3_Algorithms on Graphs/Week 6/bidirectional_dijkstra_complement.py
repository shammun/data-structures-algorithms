import heapq

def bidirectional_dijkstra(graph, reverse_graph, start, end):
    # Forward pass
    dist_forward = {node: float('inf') for node in graph}
    prev_forward = {node: None for node in graph}
    dist_forward[start] = 0

    # Backward pass
    dist_backward = {node: float('inf') for node in reverse_graph}
    prev_backward = {node: None for node in reverse_graph}
    dist_backward[end] = 0

    # Priority queues for forward and backward passes
    pq_forward = [(0, start)]
    pq_backward = [(0, end)]
    heapq.heapify(pq_forward)
    heapq.heapify(pq_backward)

    # Set of visited nodes for both searches
    visited_forward = set()
    visited_backward = set()

    # Variable to store the minimum distance and meet node
    min_dist = float('inf')
    meet_node = None

    while pq_forward and pq_backward:

        # Forward search steps
        if pq_forward:
            dist, node = heapq.heappop(pq_forward)
            if node in visited_forward:
                continue
            visited_forward.add(node)

            if node in visited_backward:
                total_dist = dist_forward[node] + dist_backward[node]
                if total_dist < min_dist:
                    min_dist = total_dist
                    meet_node = node
            
            for v, weight in graph[node]:
                if dist_forward[node] + weight < dist_forward[v]:
                    dist_forward[v] = dist_forward[node] + weight
                    prev_forward[v] = node
                    heapq.heappush(pq_forward, (dist_forward[v], v))
            
        # Backward search steps
        if pq_backward:
            dist, node = heapq.heappop(pq_backward)
            if node in visited_backward:
                continue
            visited_backward.add(node)

            if node in visited_forward:
                total_dist = dist_forward[node] + dist_backward[node]
                if total_dist < min_dist:
                    min_dist = total_dist
                    meet_node = node
            
            for v, weight in reverse_graph[node]:
                if dist_backward[node] + weight < dist_backward[v]:
                    dist_backward[v] = dist_backward[node] + weight
                    prev_backward[v] = node
                    heapq.heappush(pq_backward, (dist_backward[v], v))

        if meet_node is not None:
            break
        
    if meet_node is None:
        return float('inf'), [], []

    forward_path = get_path(prev_forward, start, meet_node)
    backward_path = get_path(prev_backward, end, meet_node)
    # backward_path.reverse()

    return min_dist, forward_path, backward_path

def get_path(prev, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = prev[current]
    return path

def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}
    reverse_graph = {i: [] for i in range(1, n+1)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        reverse_graph[v].append((u, w))

    start_node = int(input("Enter start node: "))
    end_node = int(input("Enter end node: "))

    # Validate that start and end nodes are within the graph
    if start_node not in graph or end_node not in graph:
        print(f"Error: {start_node} or {end_node} is not in the graph.")

    min_distance, forward_path, backward_path = bidirectional_dijkstra(graph, reverse_graph, start_node, end_node)

    if min_distance == float('inf'):
        print(f"No path found from {start_node} to {end_node}")

    else:
        # Remove meet_node from forward_path to prevent duplication
        for item in forward_path:
            if item in backward_path:
                forward_path.remove(item)
        full_path = forward_path + backward_path
        print(f"Shortest path from {start_node} to {end_node} is:")
        print(" -> ".join(map(str, full_path)))
        print(f"Minimum distance: {min_distance}")

if __name__ == "__main__":
    main()


"""
Sample Input:

Input 1:
4 5
1 2 1
1 3 2
2 3 1
2 4 1
3 4 1
1
4

Input 2:
6 7
1 2 7
1 3 9
1 6 14
2 3 10
2 4 15
3 6 2
4 5 6
1
5

"""