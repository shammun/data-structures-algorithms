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
        
        elif k < node.key:
            if node.left is not None:
                return self.find(k, node.left)

        else:
            if node.right is not None:
                return self.find(k, node.right)
            
        # The final return node is needed when we're searching 
        # for a key that doesn't exist in the tree, and we've 
        # reached a leaf node or a node where the next child in 
        # the search path doesn't exist.
        return node
        
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def adjust_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def next(self, node):
        """
        Find the in-order successor of a given node in the AVL tree.
        The in-order successor is the node that would come immediately after
        the given node in an in-order traversal of the tree.

        There are two main cases to consider:
        1. The node has a right subtree
        2. The node doesn't have a right subtree
        """
        # Case 1: Node has a right subtree
        if node.right:
            return self.min_value_node(node.right)
        # Case 2: Node doesn't have a right subtree
        # We need to traverse up the tree to find the first ancestor
        # where the current node is in the left subtree
        while node.parent and node == node.parent.right:
            # Move up the tree
            node = node.parent

        # Return the parent of the last node we visited
        # If we reached the root (no parent), this will return None,
        # which is correct as the original node was the largest in the tree
        # If we found a node that is the left child of its parent,
        # then that parent is the successor we're looking for
        return node.parent



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
        if node is None:
            return
        p = node.parent
        if self.get_height(node.left) > self.get_height(node.right) + 1:
            self.rebalance_right(node)
        elif self.get_height(node.right) > self.get_height(node.left) + 1:
            self.rebalance_left(node)
        self.adjust_height(node)
        if p is not None:
            self.rebalance(p)
        else:
            self.root = node
    
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
            # if child:
                # child.parent = None
        elif node == parent.left:
            parent.left = child
        else:
            parent.right = child
        if child:
            child.parent = parent
        node.parent = node.left = node.right = None

    def print_tree_inorder(self, node):
        if node:
            self.print_tree_inorder(node.left)
            print(node.key, end = " ")
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

avl_tree = AVLTree()
avl_tree.insert_and_print(10)
avl_tree.insert_and_print(20)
avl_tree.insert_and_print(30)
avl_tree.insert_and_print(40)
avl_tree.insert_and_print(50)
avl_tree.insert_and_print(25)

print("Final tree after insertions")
avl_tree.print_tree_inorder(avl_tree.root)
print()

# Delete some nodes
avl_tree.delete_and_print(30)
avl_tree.delete_and_print(50)

print("Final tree after insertions")
avl_tree.print_tree_inorder(avl_tree.root)
print()
