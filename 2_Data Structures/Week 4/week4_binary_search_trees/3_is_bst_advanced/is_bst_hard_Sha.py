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
    return tree[0] if tree else None

def is_bst_hard(root):
    def is_bst_util(node, min_val, max_val):
        if not node:
            return True

        if min_val is not None and node.key <= min_val:
            return False
        if max_val is not None and node.key > max_val:
            return False
        
        # Check left subtree (all values must be less than this node's value)
        if not is_bst_util(node.left, min_val, node.key - 1):
            return False
        
        # Check right subtree (all values must be greater than or equal to this node's value)
        if not is_bst_util(node.right, node.key, max_val):
            return False
        
        return True
    return is_bst_util(root, None, None)

def main():
    n = int(input())
    if n == 0:
        print("CORRECT")
        return
    
    nodes = [list(map(int, input().split())) for _ in range(n)]
    root = build_tree(n, nodes)

    if is_bst_hard(root):
        print("CORRECT")
    else:
        print("INCORRECT")

if __name__ == "__main__":
    main()