from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def explore(self, v, visited):
        visited.add(v)
        reachable = {v}
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                reachable.update(self.explore(neighbor, visited))
        return reachable
    
    def easy_scc(self):
        scss = []
        for v in self.vertices:
            reachable_from_v = self.explore(v, set())
            scc = {v}
            for u in reachable_from_v:
                if v in self.explore(u, set()):
                    scc.add(u)
            if scc not in scss:
                scss.append(scc)
        return scss


if __name__ == "__main__":
    g = Graph()
    # Example graph
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 3)

    result = g.easy_scc()
    print("Strongly Connected Components:")
    for i, scc in enumerate(result, 1):
        print(f"SCC {i}: {scc}")