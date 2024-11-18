class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree(n, nodes):
    tree = [Node(key) for key, _, _ in nodes]
    for i, (_, left, right) in enumerate(nodes):
        if left != -1:
            tree[i].left = tree[left]
        if right != -1:
            tree[i].right = tree[right]
    return tree[0]

def in_order(root, result):
    if root:
        in_order(root.left, result)
        result.append(str(root.key))
        in_order(root.right, result)

def pre_order(root, result):
    if root:
        result.append(str(root.key))
        pre_order(root.left, result)
        pre_order(root.right, result)

def post_order(root, result):
    if root:
        post_order(root.left, result)
        post_order(root.right, result)
        result.append(str(root.key))

def main():
    n = int(input())
    nodes = [tuple(map(int, input().split())) for _ in range(n)]

    root = build_tree(n, nodes)

    in_order_result = []
    pre_order_result = []
    post_order_result = []

    in_order(root, in_order_result)
    pre_order(root, pre_order_result)
    post_order(root, post_order_result)

    print(" ".join(in_order_result))
    print(" ".join(pre_order_result))
    print(" ".join(post_order_result))

if __name__ == "__main__":
    main()