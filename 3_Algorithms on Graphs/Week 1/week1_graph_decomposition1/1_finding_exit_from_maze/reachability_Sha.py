from typing import List, Dict

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

    def reset_visited(self):
        for v in self.visited:
            self.visited[v] = False

    def explore(self, start: int, end: int) -> bool:
        self.visited[start] = True
        if start == end:
            return True
        for w in self.adj_list[start]:
            if not self.visited[w]:
                if self.explore(w, end):
                    return True
        return False
    
    def reachable(self, start: int, end: int) -> bool:
        self.reset_visited()
        return self.explore(start, end)
    
def main():
    n, m = map(int, input().split())
    graph = Graph()

    # Add eddges
    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    
    # Start and end vertices
    start, end = map(int, input().split())

    result = 1 if graph.reachable(start, end) else 0
    print(result)

if __name__ == "__main__":
    main()