from typing import List, Dict, Set

class Graph:
    def __init__(self):
        self.adj_list: Dict[int, List[int]] = {}
        self.visited: Dict[int, bool] = {}
        self.cc_num: Dict[int, int] = {}
        self.clock: int = 1
        self.pre: Dict[int, int] = {}
        self.post: Dict[int, int] = {}
        
    def add_edge(self, u:int, v:int):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        self.visited[u] = False
        self.visited[v] = False

    def reset_visited(self):
        for v in self.adj_list:
            self.visited[v] = False

    def find_components(self) -> List[Set[int]]:
        self.reset_visited()
        components = []
        for v in self.adj_list:
            if not self.visited[v]:
                component = set()
                self.explore_component(v, component)
                components.append(component)
        return components
    
    def explore_component(self, v:int, component: Set[int]):
        self.visited[v] = True
        component.add(v)
        for w in self.adj_list[v]:
            if not self.visited[w]:
                self.explore_component(w, component)

    def explore(self, v:int):
        self.visited[v] = True
        self.previsit(v)
        for w in self.adj_list[v]:
            if not self.visited[w]:
                self.explore(w)
        self.postvisit(v)

    def dfs(self):
        self.reset_visited()
        cc = 1
        for v in self.adj_list:
            if not self.visited[v]:
                self.explore(v)
                cc += 1
    
    def previsit(self, v:int):
        self.pre[v] = self.clock
        self.clock += 1
    
    def postvisit(self, v:int):
        self.post[v] = self.clock
        self.clock += 1

def main():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(1, 4)
    graph.add_edge(5, 6)
    graph.add_edge(7, 8)
    graph.add_edge(7, 9)
    graph.add_edge(8, 9)

    print("Running DFS...")
    graph.dfs()
    print("Visited: ", graph.visited)
    print("Previsit numbers: ", graph.pre)
    print("Postvisit numbers: ", graph.post)

    print("\nFinding connected components...")
    components = graph.find_components()
    for i, component in enumerate(components, 1):
        print(f"Component {i}: {component}")

if __name__ == "__main__":
    main()