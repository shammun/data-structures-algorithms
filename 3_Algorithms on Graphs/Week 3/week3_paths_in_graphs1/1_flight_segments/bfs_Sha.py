from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, 0)])
    visited = set([start])
    distance = 0

    while queue:
        vertex, distance = queue.popleft()
        if vertex == end:
            return distance
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

        distance += 1
    
    return -1

def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    start, end = map(int, input().split())

    result = bfs(graph, start, end)
    print(result)

if __name__ == "__main__":
    main()