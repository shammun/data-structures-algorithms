import heapq

def dijkstra(graph, start):
    # Initialize distances and previous nodes
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    
    # Priority queue: elements are (distance, node)
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    
    while priority_queue:
        # Extract minimum distance node
        current_dist, u = heapq.heappop(priority_queue)
        
        # Skip if the extracted distance is not up to date
        if current_dist > dist[u]:
            continue
        
        # Iterate through all neighbors (u, v) in E
        for v, weight in graph[u]:
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(priority_queue, (alt, v))
    
    return dist, prev

def get_path(prev, start, end):
    path = []
    current = end
    while current is not None:
        path.append(str(current))
        current = prev[current]
    path.reverse()
    return path

def main():
    # Input the number of nodes and edges
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}
    
    # Input all edges with their weights
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Input the start node
    start_node = int(input())
    
    # Run Dijkstra's algorithm
    distances, predecessors = dijkstra(graph, start_node)
    
    # Output the shortest paths
    for node in range(1, n + 1):
        if node == start_node:
            continue
        path = get_path(predecessors, start_node, node)
        print(f"{start_node} to {node}: {' -> '.join(path)}")

if __name__ == "__main__":
    main()


"""

5 6
1 2 4
1 3 1
2 3 2
2 4 5
3 4 8
4 5 3
1


"""