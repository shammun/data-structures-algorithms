from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        in_degree = [0] * (self.n + 1)
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1
        
        zero_in_degree = []
        for i in range(1, self.n + 1):
            if in_degree[i] == 0:
                zero_in_degree.append(i)
        
        result = []
        while zero_in_degree:
            zero_in_degree.sort()
            u = zero_in_degree.pop(0)
            result.append(u)

            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    zero_in_degree.append(v)

        return result
    
def main():
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    topological_sort = graph.topological_sort()
    print(" ".join(map(str, topological_sort)))

if __name__ == "__main__":
    main()
