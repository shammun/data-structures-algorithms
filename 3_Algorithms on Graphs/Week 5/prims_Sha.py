import heapq
from typing import Dict, List, Tuple

def prims(graph: Dict[int, List[Tuple[int, int]]]) -> List[Tuple[int, int, int]]:
    if not graph:
        return []
    
    vertices = set(graph.keys())
    start_vertex = min(graph.keys())

    cost = {v: float('inf') for v in vertices}
    parent = {v: None for v in vertices}
    cost[start_vertex] = 0

    pq = [(0, start_vertex)]
    mst = []
    visited = set()

    while pq:
        _, v = heapq.heappop(pq)

        if v in visited:
            continue

        visited.add(v)

        if parent[v] is not None:
            mst.append((parent[v], v, cost[v]))

        for neighbor, weight in graph[v]:
            if neighbor in vertices and weight < cost[neighbor]:
                parent[neighbor] = v
                cost[neighbor] = weight
                heapq.heappush(pq, (weight, neighbor))

        vertices.remove(v)

    return mst

def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    minimum_spanning_tree = prims(graph)

    print("\nEdges in the minimum spanning tree:")
    total_weight = 0
    for u, v, w in minimum_spanning_tree:
        print(f"{u} -> {v} : {w}")
        total_weight += w
    print(f"Total weight: {total_weight}")

if __name__ == "__main__":
    main()


"""
Example 1:

Input:

4 5
1 2 10
2 3 15
1 3 5
4 2 2
4 3 40

Output:

Edges in the minimum spanning tree:
1 -> 3 : 5
1 -> 2 : 10
2 -> 4 : 2
Total weight: 17

"""