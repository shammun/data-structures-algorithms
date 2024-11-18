from typing import Dict, List, Tuple

def relax(u: int, v: int, w: int, dist: List[float], prev: List[int]) -> None:
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        prev[v] = u

def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], start: int, n: int) -> Tuple[List[float], List[int]]:
    dist = [float('inf')] * (n + 1)
    prev = [None] * (n + 1)
    
    dist[start] = 0
    
    for _ in range(n - 1):
        for u in graph:
            for v, w in graph[u]:
                relax(u, v, w, dist, prev)
    
    # Check for negative weight cycles
    for u in graph:
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                raise ValueError("Graph contains a negative weight cycle")
    
    return dist, prev

def get_path(predecessors: List[int], start: int, end: int) -> List[str]:
    path = []
    current = end
    while current != start:
        if current is None:
            return []  # No path exists
        path.append(str(current))
        current = predecessors[current]
    path.append(str(start))
    return path[::-1]  # Reverse the path

def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        # graph[v].append((u, w))

    start_node = int(input())

    try:
        distances, predecessors = bellman_ford(graph, start_node, n)

        for node in range(1, n + 1):
            if node == start_node:
                continue
            path = get_path(predecessors, start_node, node)
            if path:
                print(f"{start_node} to {node}: {' -> '.join(path)} (distance: {distances[node]})")
            else:
                print(f"{start_node} to {node}: No path exists")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# Example usage:
"""
Example 1: Simple graph with 4 nodes and 5 edges
Input:
4 5
1 2 1
1 3 4
2 3 2
2 4 6
3 4 3
1

Expected Output:
1 to 2: 1 -> 2
1 to 3: 1 -> 2 -> 3
1 to 4: 1 -> 2 -> 3 -> 4

Example 2: Graph with negative weights (but no negative cycles)
Input:
5 7
1 2 -1
1 3 4
2 3 3
2 4 2
3 4 5
3 5 2
4 5 -3
1

Expected Output:
1 to 2: 1 -> 2
1 to 3: 1 -> 2 -> 3
1 to 4: 1 -> 2 -> 4
1 to 5: 1 -> 2 -> 4 -> 5

Example 3: Graph with a negative cycle
Input:
3 3
1 2 1
2 3 -1
3 1 -1
1

Expected Output:
Graph contains a negative weight cycle
"""