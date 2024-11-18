import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0

    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)

        if current_dist > dist[u]:
            continue

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
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    start_node = int(input())

    distances, predecessors = dijkstra(graph, start_node)

    for node in range(1, n + 1):
        if node == start_node:
            continue
        path = get_path(predecessors, start_node, node)
        print(f"{start_node} to {node}: -> {.join(path)}")

if __name__ == "__main__":
    main()