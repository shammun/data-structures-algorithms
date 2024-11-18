import sys

def toposort(G):
    visited = set()
    post_order = []

    def dfs(node):
        visited.add(node)
        for neighbor in G[node]:
            if neighbor not in visited:
                dfs(neighbor)
        post_order.append(node)

    for node in range(len(G)):
        if node not in visited:
            dfs(node)

    return list(reversed(post_order))

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    n, m = map(int, input_data[:2])
    data = list(map(int, input_data[2:]))
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')