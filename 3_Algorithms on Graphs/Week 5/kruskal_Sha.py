class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

def kruskal(graph):
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])

    vertices = list(graph.keys())
    disjoint_set = DisjointSet(vertices)
    minimum_spanning_tree = []

    for u, v, w in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            minimum_spanning_tree.append((u, v ,w))

    return minimum_spanning_tree

def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    
    minimum_spanning_tree = kruskal(graph)
    total_weight = 0

    for u, v, w in minimum_spanning_tree:
        print(f"{u} -- {v} : {w}")
        total_weight += w
    print(f"Total weight: {total_weight}")

if __name__ == "__main__":
    main()

"""
Example Input:
4 5
1 2 10
2 3 15
1 3 5
4 2 2
4 3 40

Example Output:
4 -- 2 : 2
1 -- 3 : 5
1 -- 2 : 10
Total weight: 17

"""