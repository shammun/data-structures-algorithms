#Uses python3

import sys
import queue

def distance(adj, s, t):
    # Create a list to store the distances from the source vertex
    dist = [float('inf')] * len(adj)

    # The distance of the source vertex from itself is 0
    dist[s] = 0

    # Create a queue for BFS
    q = queue.Queue()

    # Enqueue the source vertex
    q.put(s)

    # Perform BFS
    while not q.empty():
        # dequeue a vertex form the queue
        u = q.get()

        # Get all the adjacent vertices of the dequeued vertex u
        for v in adj[u]:
            # If the distance of v from s is not calculated yet
            if dist[v] == float('inf'):
                # Increment the distance of v from s by 1
                dist[v] = dist[u] + 1
                # Enqueue v
                q.put(v)

                # If the target vertex is reached, return the distance
                if v == t:
                    return dist[v]
    
    # If the target vertex is not reachable from s, return -1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
