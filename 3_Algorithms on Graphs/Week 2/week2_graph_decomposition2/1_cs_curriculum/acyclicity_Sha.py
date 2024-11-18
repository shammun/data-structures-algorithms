from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_helper(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in self.graph[v]:
            if neighbor == v:
                return True
            if not visited[neighbor]:
                if self.is_cyclic_helper(neighbor, visited, rec_stack):
                    return True
            # If visited but still a neighbor or in 
            # rec_stack, then there is a cycle
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * (self.V + 1)
        rec_stack = [False] * (self.V + 1)

        for node in range(1, self.V + 1):
            if not visited[node]:
                if self.is_cyclic_helper(node, visited, rec_stack):
                    return True 
        return False
    
def main():
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    print(1 if graph.is_cyclic() else 0)

if __name__ == "__main__":
    main()

