from typing import List, Dict, Set

class Graph:
    def __init__(self):
        self.adj_list: Dict[int, List[int]] = {}
        self.visited: Dict[int, bool] = {}

    def add_edge(self, u: int, v: int):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        self.visited[u] = False
        self.visited[v] = False

    def add_vertex(self, v: int):
        if v not in self.adj_list:
            self.adj_list[v] = []
            self.visited[v] = False

    def reset_visited(self):
        for v in self.adj_list:
            self.visited[v] = False
    
    def explore(self, v: int, component: Set[int]):
        self.visited[v] = True
        component.add(v)
        for w in self.adj_list[v]:
            if not self.visited[w]:
                self.explore(w, component)

    def find_connected_components(self) -> List[Set[int]]:
        self.reset_visited()
        components = []
        for v in self.adj_list:
            if not self.visited[v]:
                component = set()
                self.explore(v, component)
                components.append(component)
        return components
    
def main():
    n, m = map(int, input().split())
    graph = Graph()

    # Add all vertices (including isolated ones)
    for i in range(1, n + 1):
        graph.add_vertex(i)

    # Add edges
    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    # Find connected components
    components = graph.find_connected_components()

    # Print the number of connected components
    print(len(components))

if __name__ == "__main__":
    main()