from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def reverse_graph(self):
        reversed_graph = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                reversed_graph.add_edge(v, u)
        return reversed_graph
    
    def dfs(self, v, visited, post_order):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, post_order)
        post_order.append(v)

    def explore(self, v, visited):
        scc = [v]
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                scc.extend(self.explore(neighbor, visited))
        return scc
    
    def scc(self):
        # Step 1: Eun DFS on reversed graph to get post order
        reversed_graph = self.reverse_graph()
        visited = set()
        post_order = []
        for v in reversed_graph.vertices:
            if v not in visited:
                reversed_graph.dfs(v, visited, post_order)

        # Step 2: Run explore on original graph in decreasing post order
        scss = []
        visited = set()
        for v in reversed(post_order):
            if v not in visited:
                scc = self.explore(v, visited)
                scss.append(scc)
        
        return scss

def main():
    n, m = map(int, input().split())
    graph = Graph()

    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    
    result = graph.scc()
    print(len(result))

if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     g = Graph()
#     # Example graph
#     g.add_edge(0, 1)
#     g.add_edge(1, 2)
#     g.add_edge(2, 0)
#     g.add_edge(1, 3)
#     g.add_edge(3, 4)
#     g.add_edge(4, 3)

#     result = g.scc()
#     print("Strongly Connected Components:")
#     for i, scc in enumerate(result, 1):
#         print(f"SCC {i}: {scc}")



