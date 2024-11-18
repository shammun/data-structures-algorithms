class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree(n, nodes):
    tree = [TreeNode(key) for key, _, _ in nodes]
    for i, (_, left, right) in enumerate(nodes):
        if left != -1:
            tree[i].left = tree[left]
        if right != -1:
            tree[i].right = tree[right]
    return tree[0]

def inorder(root, result):
    if not root:
        return
    inorder(root.left, result)
    result.append(str(root.key))
    inorder(root.right, result)

def preorder(root, result):
    if not root:
        return
    result.append(str(root.key))
    preorder(root.left, result)
    preorder(root.right, result)

def postorder(root, result):
    if not root:
        return
    postorder(root.left, result)
    postorder(root.right, result)
    result.append(str(root.key))

def main():
    n = int(input())
    nodes = [list(map(int, input().split())) for _ in range(n)]

    root = build_tree(n, nodes)
    
    in_order = []
    pre_order = []
    post_order = []

    inorder(root, in_order)
    preorder(root, pre_order)
    postorder(root, post_order)

    print(" ".join(in_order))
    print(" ".join(pre_order))
    print(" ".join(post_order))

if __name__ == "__main__":
    main()