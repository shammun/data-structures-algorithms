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
        dist[start] = 0
        queue = deque([start])

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if dist[v] == float('inf'):
                    queue.append(v)
                    dist[v] = dist[u] + 1
        
        return dist

def main():
    n, m = map(int, input().split())
    graph = Graph()
    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    start_vertex = int(input(f"Enter the start vertex (1-{n}): "))

    dist = graph.bfs(start_vertex)

    for vertex in range(1, n + 1):
        distance = dist.get(vertex, -1)
        print(distance, end=" ")
    print()

if __name__ == "__main__":
    main()

"""
Enter the number of vertices and edges (n m): 6 7
Enter 7 edges in the format 'u v':
1 2
1 3
2 4
2 5
3 5
4 6
5 6
Enter the start vertex (1-6): 1
"""