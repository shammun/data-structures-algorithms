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
        """
        Perform a right rotation on the given node x.
        This is the Zig operation in Splay Tree terminology.
        """
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:  # x is root
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _left_rotate(self, y):
        """
        Perform a left rotation on the given node x.
        This is the Zag operation in Splay Tree terminology.
        """
        x = y.right
        y.right = x.left
        if x.left:
            x.left.parent = y
        x.parent = y.parent
        if not y.parent:  # y is root
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.left = y
        y.parent = x

    def _splay(self, x):
        """
        Splay the given node x to the root of the tree.
        This involves a series of rotations to bring x to the root.
        """
        while x.parent:
            print(f"Splaying node {x.key}")  # Track the node being splayed
            if not x.parent.parent:
                # Zig or Zag step
                if x == x.parent.left:
                    self._right_rotate(x.parent)
                else:
                    self._left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # Zig-Zig step
                self._right_rotate(x.parent.parent)
                self._right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # Zag-Zag step
                self._left_rotate(x.parent.parent)
                self._left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.right:
                # Zig-Zag step
                self._right_rotate(x.parent)
                self._left_rotate(x.parent)
            else:
                # Zag-Zig step
                self._left_rotate(x.parent)
                self._right_rotate(x.parent)

    def insert(self, key):
        """
        Insert a new key into the Splay Tree.
        After insertion, the new node is splayed to the root.
        """
        print(f"Inserting {key}")  # Track insertions
        node = Node(key)
        y = None
        x = self.root

        while x:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if not y:
            self.root = node  # tree was empty
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self._splay(node)

    def search(self, key):
        """
        Search for a key in the Splay Tree.
        If found, the node is splayed to the root and returned.
        If not found, return None.
        """
        print(f"Searching for {key}")  # Track searches
        x = self.root
        while x:
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
        Remove the node with the given key from the Splay Tree.

        1. Search for the Node to Delete. Return if the node doesn't exist. Splay the 
        node to the root 
        2. Detach the left and right subtrees from the node.
        3. Find the maximum node in the left subtree, splay it to the root of the left 
        subtree, and attach the right subtree to it. If there is no left subtree, set the 
        right subtree as the new root. 

        Time complexity: O(log n)
        """
        print(f"Deleting {key}")  # Track deletions
        node = self.search(key)
        if not node:
            return
        self._splay(node)

        left_subtree = node.left
        if left_subtree:
            left_subtree.parent = None
        
        right_subtree = node.right
        if right_subtree:
            right_subtree.parent = None

        if left_subtree:
            max_left = left_subtree
            while max_left.right:
                max_left = max_left.right
            self._splay(max_left)
            max_left.right = right_subtree
            if right_subtree:
                right_subtree.parent = max_left
            self.root = max_left
        else:
            self.root = right_subtree

    def inorder(self, node):
        """
        Perform an inorder traversal of the tree starting from the given node.
        """
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

if __name__ == "__main__":
    tree = SplayTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(25)
    tree.insert(5)

    print("\nInorder traversal of the tree:")
    tree.inorder(tree.root)
    print()

    print("\nSearching for key 25:")
    found_node = tree.search(25)
    if found_node:
        print(f"Found key {found_node.key} and splayed to the root.")
    else:
        print("Key not found.")

    print("\nInorder traversal after splaying key 25:")
    tree.inorder(tree.root)
    print()

    print("\nDeleting key 20:")
    tree.delete(20)

    print("\nInorder traversal after deletion:")
    tree.inorder(tree.root)
    print()