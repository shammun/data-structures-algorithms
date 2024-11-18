from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
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

        for vertex in self.graph:
            if vertex not in self.visited:
                self.dfs(vertex)
        
        return self.post_order[::-1]
    
if __name__ == "__main__":
    g = Graph()
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    result = g.topological_sort()
    print("Topological Sort Order:", result)