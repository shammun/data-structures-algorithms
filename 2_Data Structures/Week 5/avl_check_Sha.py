
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

    def next(self, node):
        if node.right is not None:
            return self.left_descendant(node.right)
        else:
            return self.right_ancestor(node)

    def left_descendant(self, node):
        if node.left is None:
            return node
        else:
            return self.left_descendant(node.left)

    def right_ancestor(self, node):
        if node.parent is None:
            return None
        if node.key < node.parent.key:
            return node.parent
        else:
            return self.right_ancestor(node.parent)

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
        self.print_tree_inorder(new_node)

    def delete(self, k):
      # Find the node to delete
      N = self.find(k, self.root)
      if N is None:
          return  # Node not found

      # Keep track of the node from which to start rebalancing
      rebalance_node = N.parent

      # Case 1: Node has no children
      if N.left is None and N.right is None:
          if N.parent is None:
              self.root = None
          elif N == N.parent.left:
              N.parent.left = None
          else:
              N.parent.right = None

      # Case 2: Node has only left child
      elif N.right is None:
          if N.parent is None:
              self.root = N.left
              N.left.parent = None
          elif N == N.parent.left:
              N.parent.left = N.left
              N.left.parent = N.parent
          else:
              N.parent.right = N.left
              N.left.parent = N.parent

      # Case 3: Node has only right child
      elif N.left is None:
          if N.parent is None:
              self.root = N.right
              N.right.parent = None
          elif N == N.parent.left:
              N.parent.left = N.right
              N.right.parent = N.parent
          else:
              N.parent.right = N.right
              N.right.parent = N.parent

      # Case 4: Node has both children
      else:
          X = self.next(N)
          N.key = X.key
          # Recursively delete X
          self.delete(X.key)
          return  # Rebalancing will be handled by the recursive call

      # Clean up references from the deleted node
      N.parent = N.left = N.right = None

      # Rebalance the tree
      self.rebalance(rebalance_node)



    def replace_node(self, node, new_node):
        if node.parent is None:
            self.root = new_node
        elif node == node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        if new_node is not None:
            new_node.parent = node.parent



    def rotate_right(self, x):
        p = x.parent
        y = x.left
        b = y.right

        y.parent = p
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y

        x.parent = y
        y.right = x

        if b is not None:
            b.parent = x
        x.left = b

        self.adjust_height(x)
        self.adjust_height(y)
        
    def rotate_left(self, x):
        p = x.parent
        y = x.right
        b = y.left

        y.parent = p
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y

        x.parent = y
        y.left = x

        if b is not None:
            b.parent = x
        x.right = b

        self.adjust_height(x)
        self.adjust_height(y)


    def adjust_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

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
        p = node.parent
        if self.get_height(node.left) > self.get_height(node.right) + 1:
            self.rebalance_right(node)
        if self.get_height(node.right) > self.get_height(node.left) + 1:
            self.rebalance_left(node)
        self.adjust_height(node)
        if p is not None:
            self.rebalance(p)

    # Additional AVLTree methods...

    def print_tree_inorder(self, node):
        if node is not None:
            self.print_tree_inorder(node.left)
            print(node.key, end=" ")
            self.print_tree_inorder(node.right)

avl_tree = AVLTree()

avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)
#avl_tree.insert(40)
#avl_tree.insert(50)
#avl_tree.insert(25)

#avl_tree.delete(30)
avl_tree.print_tree_inorder(avl_tree.root)