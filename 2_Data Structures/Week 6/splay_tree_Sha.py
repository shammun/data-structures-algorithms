class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        # Zig operation (right rotation)
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None: # x is root
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _left_rotate(self, y):
        x = y.right
        y.right = x.left
        if x.left is not None:
            x.left.parent = y
        # Update the parent's child pointer
        if y.parent is None: # y is root
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        # Finish the rotation
        x.left = y
        y.parent = x

    def _splay(self, x):
        while x.parent is not None:
            print(f"Splaying node {x.key}")  # Add this line to track the node being splayed
            # Zig or zag: when x's parent is the root
            if x.parent.parent is None:
                # Zig: if x is the left child of its parent
                if x == x.parent.left:
                    self._right_rotate(x.parent)
                # Zag: if x is the right child of its parent
                else:
                    self._left_rotate(x.parent)
            # Zig-Zig: when x and its parent are both left children
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self._right_rotate(x.parent.parent)
                self._right_rotate(x.parent)
            # Zag-Zag: when x and its parent are both right children
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self._left_rotate(x.parent.parent)
                self._left_rotate(x.parent)
            # Zig-Zag: when x is a left child and its parent is a right child
            elif x == x.parent.left and x.parent == x.parent.parent.right:
                self._right_rotate(x.parent)
                self._left_rotate(x.parent)
            # Zag-Zig: when x is a right child and its parent is a left child
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self._left_rotate(x.parent)
                self._right_rotate(x.parent)


    def insert(self, key):
        print(f"Inserting {key}")  # Add this to track insertions
        node = Node(key)
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node  # tree was empty
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self._splay(node)

    def search(self, key):
        print(f"Searching for {key}")  # Add this to track searches
        x = self.root
        while x is not None:
            if key == x.key:
                self._splay(x)
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return None

    
    def delete(self, key):
        """
        Removes the node with the given key from the Splay Tree.

        1. Search for the Node to Delete. Return if the node doesn't exist. Splay the 
        node to the root 
        2. Detach the left and right subtrees from the node.
        3. Find the maximum node in the left subtree, splay it to the root of the left 
        subtree, and attach the right subtree to it. If there is no left subtree, set the 
        right subtree as the new root. 

        Time complexity: O(log n)
        """
        node = self.search(key)
        if node is None:
            return
        self._splay(node)

        if node.left is not None:
            x = node.left
            x.parent = None
        else:
            x = None
        
        if node.right is not None:
            y = node.right
            y.parent = None
        else:
            y = None

        if x is not None:
            maximum = x
            while maximum.right is not None:
                maximum = maximum.right
            self._splay(maximum)
            maximum.right = y
            if y is not None:
                y.parent = maximum
            self.root = maximum
        else:
            self.root = y
            
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.key, end = ' ')
            self.inorder(node.right)

if __name__ == "__main__":
    tree = SplayTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(25)
    tree.insert(5)

    print("Inorder traversal of the tree:")
    tree.inorder(tree.root)
    print()

    print("Searching for key 25:")
    found_node = tree.search(25)
    if found_node:
        print(f"Found key {found_node.key} and splayed to the root.")
    else:
        print("Key not found.")

    print("Inorder traversal after splaying key 25:")
    tree.inorder(tree.root)
    print()

    print("Deleting key 20:")
    tree.delete(20)

    print("Inorder traversal after deletion:")
    tree.inorder(tree.root)
    print()