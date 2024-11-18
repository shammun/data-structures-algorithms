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
        """
        Right rotation (Zig operation) on node x.

        This involves rearranging the tree such that x's left child y becomes the
        new root of the subtree, and x becomes the right child of y. This is used
        to splay the tree, which involves moving recently accessed nodes to the
        root of the tree. This makes future searches for the node faster.

        :param x: The node to rotate.
        """
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:  # x is root
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _left_rotate(self, x):
        # Zag operation (left rotation)
        """
        Left rotation (Zag operation) on node x.

        This involves rearranging the tree such that x's right child y becomes the
        new root of the subtree, and x becomes the left child of y. This is used
        to splay the tree, which involves moving recently accessed nodes to the
        root of the tree. This makes future searches for the node faster.

        :param x: The node to rotate.
        """
        # Perform right rotation
        y = x.right  # Set y as the right child of x
        x.right = y.left  # The left subtree of y becomes the right subtree of x
        if y.left is not None:
            y.left.parent = x  # Update parent of y's left child
        y.parent = x.parent  # y's new parent is x's old parent

        # Update the parent's child pointer
        if x.parent is None:  # x was the root
            self.root = y  # y becomes the new root
        elif x == x.parent.left:
            x.parent.left = y  # y becomes left child of x's parent
        else:
            x.parent.right = y  # y becomes right child of x's parent

        # Finish the rotation
        y.left = x  # x becomes left child of y
        x.parent = y  # Update x's parent to y

    def _splay(self, x):
        while x.parent is not None:
            if x.parent.parent is None:
                # Zig or Zag: when x's parent is the root
                if x.parent.left == x:
                    self._right_rotate(x.parent)  # Zig
                else:
                    self._left_rotate(x.parent)  # Zag
            elif x.parent.left == x and x.parent.parent.left == x.parent:
                # Zig-Zig: when x and its parent are both left children
                self._right_rotate(x.parent.parent)
                self._right_rotate(x.parent)
            elif x.parent.right == x and x.parent.parent.right == x.parent:
                # Zag-Zag: when x and its parent are both right children
                self._left_rotate(x.parent.parent)
                self._left_rotate(x.parent)
            elif x.parent.left == x and x.parent.parent.right == x.parent:
                # Zag-Zig: when x is a left child and its parent is a right child
                self._left_rotate(x.parent)  # Left rotate on y (x's parent)
                self._right_rotate(x.parent.parent)  # Right rotate on z (x's grandparent)
            elif x.parent.right == x and x.parent.parent.left == x.parent:
                # Zig-Zag: when x is a right child and its parent is a left child
                self._right_rotate(x.parent)  # Right rotate on y (x's parent)
                self._left_rotate(x.parent.parent)  # Left rotate on z (x's grandparent)

    def insert(self, key):
        """
        Inserts a new node with the given key into the splay tree.

        The insert method adds a new node with the given key into the Splay Tree. After 
        inserting the node, it performs a splay operation to bring the newly inserted node to 
        the root, which ensures that frequently accessed nodes are closer to the root.

        Time complexity: O(log n)
        """
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

    # The search method finds the node with a given key in the Splay Tree. 
    # If the node is found, the method splays the found node to the root. 
    # If the key doesn't exist in the tree, the method returns None.
    def search(self, key):
        """
        Finds the node with a given key in the Splay Tree. If the node is found, 
        the method splays the found node to the root. If the key doesn't exist in 
        the tree, the method returns None.

        Time complexity: O(log n)
        """
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

    # The delete method removes the node with a given key from the Splay Tree.
    # 1. Search and splay the node to be deleted to the root. This step simplifies the 
    # rest of the deletion process by isolating the left and right subtrees.
    # 2. Detach the left and right subtrees from the node.
    # 3. Find the maximum node in the left subtree, splay it to the root of the left 
    # subtree, and attach the right subtree to it. If there is no left subtree, set the 
    # right subtree as the new root.
    # 4. Set the new root of the tree, which will either be the maximum node from the 
    # left subtree or the right subtree.
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
        # 1. Search for the Node to Delete. Return if the node doesn't exist. Splay the 
        # node to the root 
        node = self.search(key)
        if node is None:
            return

        self._splay(node)

        # 2. Detach the left and right subtrees from the node.
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

        # 3. Find the maximum node in the left subtree, splay it to the root of the left 
        # subtree, and attach the right subtree to it. If there is no left subtree, set the 
        # right subtree as the new root. 
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
            print(node.key, end=' ')
            self.inorder(node.right)

# Example usage:
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
