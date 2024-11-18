from collections import deque

def bfs(graph, start, colors):
    queue = deque([start])
    colors[start] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if colors[neighbor] == colors[node]:
                return False
            elif colors[neighbor] == -1:
                colors[neighbor] = 1 - colors[node]
                queue.append(neighbor)
    return True

def is_bipartite(graph):
    n = len(graph)
    colors = [-1] * n

    for i in range(n):
        if colors[i] == -1:
            if not bfs(graph, i, colors):
                return False
    
    return True

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    print(1 if is_bipartite(graph) else 0)

if __name__ == "__main__":
    main()