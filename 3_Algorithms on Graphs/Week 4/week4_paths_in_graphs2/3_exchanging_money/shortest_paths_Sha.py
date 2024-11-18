from typing import Dict, List, Tuple

def relax(u: int, v: int, w: int, dist: List[float]) -> None:
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w

def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], n: int, s: int) -> List[str]:
    dist = [float('inf')] * (n + 1)
    dist[s] = 0

    # Relax edges |V| - 1 times
    for _ in range(n - 1):
        for u in graph:
            for v, w in graph[u]:
                relax(u, v, w, dist)

    # Check for negative weight cycles and propagate -inf
    for _ in range(n):
        for u in graph:
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = float('-inf')

    # Format output
    result = []
    for i in range(1, n + 1):
        if i == s:
            result.append('0')
        elif dist[i] == float('inf'):
            result.append("*")
        elif dist[i] == float("-inf"):
            result.append("-")
        else:
            result.append(str(dist[i]))
    return result

def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    s = int(input())

    result = bellman_ford(graph, n, s)

    for r in result:
        print(r)

if __name__ == "__main__":
    main()