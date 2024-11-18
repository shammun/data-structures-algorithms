from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def bfs(self, start):
        dist = {vertex: float('inf') for vertex in self.vertices}
        prev = {vertex: None for vertex in self.vertices}
        dist[start] = 0
        queue = deque([start])

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if dist[v] == float('inf'):
                    queue.append(v)
                    dist[v] = dist[u] + 1
                    prev[v] = u
        return dist, prev
    
    def reconstruct_path(self, start, end, prev):
        result = []
        u = end
        while u != start:
            result.append(u)
            u = prev[u]
            if u is None:
                return None
        result.append(start)
        return list(reversed(result))
    
def main():
        n, m = map(int, input().split())

        graph = Graph()

        for _ in range(m):
            u, v = map(int, input().split())
            graph.add_edge(u, v)

        start, end = map(int, input().split())
        distance, prev = graph.bfs(start)
        path = graph.reconstruct_path(start, end, prev)

        if path:
            print(f"Shortest paths from {start} to {end}:")
            print(" -> ".join(map(str, path)))
            print(f"Distance: {distance[end]}")
        else:
            print(f"No path from  {start} to {end}")

if __name__ == "__main__":
    main()


"""
Input:
5 6
1 2
1 3
2 3
2 4
3 4
4 5
1 5

Output:
Shortest path from 1 to 5:
1 -> 2 -> 4 -> 5
Distance: 3
"""