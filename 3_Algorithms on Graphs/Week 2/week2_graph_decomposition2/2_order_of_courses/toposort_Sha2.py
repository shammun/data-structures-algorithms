from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_topological_sort(self, v, visited, stack):
        visited[v] = True
        for neighbor in sorted(self.graph[v]):
            if not visited[neighbor]:
                self.dfs_topological_sort(neighbor, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * (self.n + 1)
        stack = []
        
        # Find vertices with no incoming edges
        has_incoming = set()
        for u in self.graph:
            for v in self.graph[u]:
                has_incoming.add(v)
        
        # Process vertices with no incoming edges first
        for v in range(1, self.n + 1):
            if v not in has_incoming and not visited[v]:
                self.dfs_topological_sort(v, visited, stack)
        
        # Process remaining vertices
        for v in range(1, self.n + 1):
            if not visited[v]:
                self.dfs_topological_sort(v, visited, stack)
        
        return stack[::-1]

def main():
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    topological_order = graph.topological_sort()
    print(" ".join(map(str, topological_order)))

if __name__ == "__main__":
    main()