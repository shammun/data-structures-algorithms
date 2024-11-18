class TableUnionFind:
    def __init__(self, sizes):
        self.parent = list(range(len(sizes)))
        self.rank = [0] * len(sizes)
        self.size = sizes
        self.max_size = max(sizes)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, dest, source):
        root_dest = self.find(dest)
        root_source = self.find(source)

        if root_dest != root_source:
            self.parent[root_source] = root_dest
            self.size[root_dest] += self.size[root_source]
            self.size[root_source] = 0
        
            if self.rank[root_dest] == self.rank[root_source]:
                self.rank[root_dest] += 1
        
            self.max_size = max(self.max_size, self.size[root_dest])

        return self.max_size
    
def table_merging(n, size, queries):
    uf = TableUnionFind(size)
    results = []

    for dest, source in queries:
        results.append(uf.union(dest-1, source-1))

    return results

def main():
    n, m = map(int, input().split())
    size = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(m)]

    results = table_merging(n, size, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()