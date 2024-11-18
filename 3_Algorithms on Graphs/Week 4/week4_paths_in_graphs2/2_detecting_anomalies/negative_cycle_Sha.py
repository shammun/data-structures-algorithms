from typing import Dict, List, Tuple

def relax(u: int, v: int, w: int, dist: List[float]) -> bool:
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        return True
    return False

def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], n: int) -> int:
    dist = [float('inf')] * (n + 1)
    dist[1] = 0

    for _ in range(n - 1):
        for u in graph:
            for v, w in graph[u]:
                relax(u, v, w, dist)

    for u in graph:
        for v, w in graph[u]:
            if relax(u, v, w, dist):
                return 1
    
    return 0

def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].appen((v, w))

    result = bellman_ford(graph, n)
    print(result)

if __name__ == "__main__":
    main()