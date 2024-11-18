from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.vertices = set(range(1, n+1))

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_topological_sort(self, v, visited, stack):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_topological_sort(neighbor, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = set()
        stack = []
        for v in self.vertices:
            if v not in visited:
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