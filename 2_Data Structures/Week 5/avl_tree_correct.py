class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None
        self.parent = None

class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, k, node):
        if node is None or node.key == k:
            return node
        elif node.key > k:
            if node.left is not None:
                return self.find(k, node.left)
        else:
            if node.right is not None:
                return self.find(k, node.right)
        return node

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def adjust_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        if T2:
            T2.parent = y
        x.parent = y.parent
        y.parent = x

        if not x.parent:
            self.root = x
        elif y == x.parent.right:
            x.parent.right = x
        else:
            x.parent.left = x

        self.adjust_height(y)
        self.adjust_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        if T2:
            T2.parent = x
        y.parent = x.parent
        x.parent = y

        if not y.parent:
            self.root = y
        elif x == y.parent.left:
            y.parent.left = y
        else:
            y.parent.right = y

        self.adjust_height(x)
        self.adjust_height(y)

        return y

    def insert(self, k):
        p = self.find(k, self.root)
        new_node = AVLNode(k)
        if p is None:
            self.root = new_node
        elif k < p.key:
            p.left = new_node
            new_node.parent = p
        else:
            p.right = new_node
            new_node.parent = p
        self.rebalance(new_node)

    def rebalance_right(self, node):
        m = node.left
        if self.get_height(m.right) > self.get_height(m.left):
            self.rotate_left(m)
        self.rotate_right(node)
        self.adjust_height(node)
        self.adjust_height(m)

    def rebalance_left(self, node):
        m = node.right
        if self.get_height(m.left) > self.get_height(m.right):
            self.rotate_right(m)
        self.rotate_left(node)
        self.adjust_height(node)
        self.adjust_height(m)

    def rebalance(self, node):
        while node:
            p = node.parent
            if self.get_height(node.left) > self.get_height(node.right) + 1:
                self.rebalance_right(node)
            elif self.get_height(node.right) > self.get_height(node.left) + 1:
                self.rebalance_left(node)
            self.adjust_height(node)
            node = p

    def next(self, node):
        if node.right:
            return self.min_value_node(node.right)
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, k):
        N = self.find(k, self.root)
        if N is None or N.key != k:
            return
        
        self._delete_node(N)

    def _delete_node(self, node):
        if node.left is None and node.right is None:
            self._remove_leaf(node)
        elif node.left is None:
            self._remove_with_single_child(node, node.right)
        elif node.right is None:
            self._remove_with_single_child(node, node.left)
        else:
            successor = self.min_value_node(node.right)
            node.key = successor.key
            self._delete_node(successor)
            return

        self.rebalance(node.parent)

    def _remove_leaf(self, node):
        parent = node.parent
        if parent is None:
            self.root = None
        elif node == parent.left:
            parent.left = None
        else:
            parent.right = None
        node.parent = None

    def _remove_with_single_child(self, node, child):
        parent = node.parent
        if parent is None:
            self.root = child
            child.parent = None
        elif node == parent.left:
            parent.left = child
        else:
            parent.right = child
        child.parent = parent
        node.parent = node.left = node.right = None

    def print_tree_inorder(self, node):
        if node:
            self.print_tree_inorder(node.left)
            print(node.key, end=" ")
            self.print_tree_inorder(node.right)

    def insert_and_print(self, key):
        self.insert(key)
        print(f"\nAfter inserting {key}:")
        self.print_tree_inorder(self.root)
        print()

    def delete_and_print(self, key):
        self.delete(key)
        print(f"\nAfter deleting {key}:")
        self.print_tree_inorder(self.root)
        print()

# Create and populate the AVL tree
avl_tree = AVLTree()

avl_tree.insert_and_print(10)
avl_tree.insert_and_print(20)
avl_tree.insert_and_print(30)
avl_tree.insert_and_print(40)
avl_tree.insert_and_print(50)
avl_tree.insert_and_print(25)

print("\nFinal tree after insertions:")
avl_tree.print_tree_inorder(avl_tree.root)
print()

# Delete some nodes
avl_tree.delete_and_print(30)
avl_tree.delete_and_print(50)

print("\nFinal tree after deletions:")
avl_tree.print_tree_inorder(avl_tree.root)
print()