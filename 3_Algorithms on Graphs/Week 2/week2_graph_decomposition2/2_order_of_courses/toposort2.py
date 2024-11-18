import sys

def dfs(adj, used, order, x):
    used[x] = 1
    for neighbor in adj[x]:
        if not used[neighbor]:
            dfs(adj, used, order, neighbor)
    order.append(x)

def toposort(adj):
    used = [0] * len(adj)
    order = []
    for vertex in range(len(adj)):
        if not used[vertex]:
            dfs(adj, used, order, vertex)
    return order[::-1]

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
