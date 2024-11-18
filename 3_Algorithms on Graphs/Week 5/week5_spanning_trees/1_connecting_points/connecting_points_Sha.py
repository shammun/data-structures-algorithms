import math

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

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def kruskal(points):
    edges = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            edges.append((i, j, distance(points[i], points[j])))

    edges.sort(key=lambda x: x[2])

    disjoint_set = DisjointSet(range(len(points)))
    mst = []
    total_length = 0

    for edge in edges:
        u, v, length = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append(edge)
            total_length += length
            if len(mst) == len(points) -1:
                break
    
    return total_length

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    min_length = kruskal(points)
    print(f"{min_length:.9f}")

if __name__ == "__main__":
    main()



