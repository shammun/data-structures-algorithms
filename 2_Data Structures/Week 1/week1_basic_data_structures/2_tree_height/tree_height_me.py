from collections import deque

def tree_height_stack(adj, root):
    stack = [(root, 0)]
    # queue =  deque([(root, 0)])
    max_height = 0

    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)

        for child in adj[node]:
            stack.append((child, height + 1))

        return max_height + 1

def tree_height_queue(adj, root):
    # stack = [(root, 0)]
    queue = deque([(root, 0)])
    max_height = 0

    while queue:
        node, height = queue.popleft()
        max_height = max(max_height, height)

        for child in adj[node]:
            queue.append((child, height + 1))

        return max_height + 1

def tree_height(adj, root):
    queue = deque([(root, 0)])
    max_depth = 0

    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)

        for child in adj[node]:
            queue.append((child, depth + 1))
    return max_depth + 1

def main():
    n = int(input())
    all_nodes = list(map(int, input().split()))
    root = all_nodes.index(-1)
    adj = [[] for _ in range(n)]

    for child in range(n):
        if all_nodes[child] != -1:
            adj[all_nodes[child]].append(child)

    print(tree_height_stack(adj, root))

if __name__ == '__main__':
    main()