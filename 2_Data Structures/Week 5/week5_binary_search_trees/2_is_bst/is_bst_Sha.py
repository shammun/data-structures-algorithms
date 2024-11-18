import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree(nodes):
    tree = [Node(key) for key, _, _ in nodes]
    for i, (_, left, right) in enumerate(nodes):
        if left != -1:
            tree[i].left = tree[left]
        if right != -1:
            tree[i].right = tree[right]
    return tree[0] if tree else None

def is_bst_util(root, min_value, max_value):
    if root is None:
        return True
    
    if root.key <= min_value or root.key >= max_value:
        return False
    
    return (is_bst_util(root.left, min_value, root.key) and 
            is_bst_util(root.right, root.key, max_value))

def is_bst(root):
    return is_bst_util(root, float('-inf'), float('inf'))

def main():
    n = int(input())
    if n == 0:
        print("CORRECT")
        return
    
    nodes = [tuple(map(int, input().split())) for _ in range(n)]
    root = build_tree(nodes)

    if is_bst(root):
        print("CORRECT")
    else:
        print("INCORRECT")

if __name__ == "__main__":
    sys.setrecursionlimit(10**5)
    main()
