import math

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1, root2 = self.find(set1), self.find(set2)
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def clustering(points, k):
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((distance(points[i], points[j]), i, j))
    
    edges.sort()  # Sort in ascending order
    
    uf = UnionFind(n)
    cluster = n
    
    for d, u, v in edges:
        if uf.find(u) != uf.find(v):
            if cluster <= k:
                return d
            uf.union(u, v)
            cluster -= 1
    
    # If we reach here, something went wrong
    raise ValueError("Unable to find a valid clustering. Check input constraints.")

def main():
    # Read input
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    cluster = int(input())

    # Compute and output the result
    result = clustering(points, cluster)
    print("{:.9f}".format(result))

if __name__ == "__main__":
    main()