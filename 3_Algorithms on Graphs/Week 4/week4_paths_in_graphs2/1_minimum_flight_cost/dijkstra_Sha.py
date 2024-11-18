import heapq

def dijkstra(graph, start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)

        if u == end:
            return current_dist
        
        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(priority_queue, (alt, v))
        
    return -1


def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    start, end = map(int, input().split())

    result = dijkstra(graph, start, end)
    print(result)

if __name__ == "__main__":
    main()