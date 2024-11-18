from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n
        self.visited = set()
        self.post_order = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v):
        self.visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
        self.post_order.append(v)

    def topological_sort(self):
        self.visited = set()
        self.post_order = []

        # Iterate through all possible vertices
        for vertex in range(1, self.n + 1):
            if vertex not in self.visited:
                self.dfs(vertex)
        
        return self.post_order[::-1]

def main():
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    result = graph.topological_sort()
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()