#Uses python3

import sys

def explore(adj, v, visited, rec_stack):
    visited[v] = True
    rec_stack[v] = True

    for neighbor in adj[v]:
        if not visited[neighbor] and explore(adj, neighbor, visited, rec_stack):
            return True
        elif rec_stack[neighbor]:
            return True
    rec_stack[v] = False
    return False

def acyclic(adj):
    n = len(adj)
    visited = [False] * n
    rec_stack = [False] * n
    for v in range(n):
        if not visited[v] and explore(adj, v, visited, rec_stack):
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
