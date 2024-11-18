class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None
        self.parent = None
        self.sum = key

class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, k, node):
        if node is None or node.key == k:
            return node
        if k < node.key:
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

    def update_sum(self, node):
        if node:
            node.sum = node.key
            if node.left:
                node.sum += node.left.sum
            if node.right:
                node.sum += node.right.sum

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
        self.update_sum(y)
        self.update_sum(x)

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
        self.update_sum(x)
        self.update_sum(y)

        return y
    
    def insert(self, key):
        p = self.find(key, self.root)
        new_node = AVLNode(key)

        if p is None:
            self.root = new_node
        elif key < p.key:
            p.left = new_node
            new_node.parent = p
        elif key > p.key:
            p.right = new_node
            new_node.parent = p
        else:
            return
        self.rebalance(new_node)

    def rebalance_right(self, node):
        m = node.left
        if self.get_height(m.right) > self.get_height(m.left):
            self.rotate_left(m)
        self.rotate_right(node)
        self.adjust_height(node)
        self.adjust_height(m)
        self.update_sum(node)
        self.update_sum(m)

    def rebalance_left(self, node):
        m = node.right
        if self.get_height(m.left) > self.get_height(m.right):
            self.rotate_right(m)
        self.rotate_left(node)
        self.adjust_height(node)
        self.adjust_height(m)
        self.update_sum(node)
        self.update_sum(m)

    def rebalance(self, node):
        while node:
            self.adjust_height(node)
            self.update_sum(node)
            if self.get_height(node.left) > self.get_height(node.right) + 1:
                self.rebalance_right(node)
            elif self.get_height(node.right) > self.get_height(node.left) + 1:
                self.rebalance_left(node)
            node = node.parent

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
        """
        Deletes a node from the AVL tree.
        
        If the node has no children, this function calls _remove_leaf to remove the node.
        If the node has one child, this function calls _remove_node_with_one_child to remove the node.
        If the node has two children, this function finds the successor of the node (the node with the smallest key greater than the node's key), replaces the node's key with the successor's key, and recursively deletes the successor.
        
        Args:
            node (AVLNode): The node to be deleted.
            
        Returns:
            None
        """
        if node.left is None and node.right is None:
            self._remove_leaf(node)
        elif node.left is None:
            self._remove_node_with_one_child(node, node.right)
        elif node.right is None:
            self._remove_node_with_one_child(node, node.left)
        else:
            successor = self.min_value_node(node.right)
            node.key = successor.key
            self._delete_node(successor)
            return
        self.rebalance(node.parent)

    def _remove_leaf(self, node):
        """
        Remove a leaf node from the tree.

        Args:
            node (AVLNode): The leaf node to be removed.

        Returns:
            None
        """
        parent = node.parent
        # if node is the root, set the root to None
        if parent is None:
            self.root = None
        elif node == parent.left:
            parent.left == None
        else:
            parent.right = None
        # set the parent of the removed node to None
        node.parent = None

    def _remove_node_with_one_child(self, node, child):
        parent = node.parent
        
        # checks if the node being removed is the root of the tree 
        if parent is None:
            self.root = child
        elif node == parent.left:
            parent.left = child
        else:
            parent.right = child
        if child:
            child.parent = parent
        node.parent = node.right = node.left = None

    def range_sum(self, left, right):
        def sum_less_than(k):
            total = 0
            node = self.root
            while node:
                if k <= node.key:
                    if k == node.key:
                        if node.left:
                            total += node.left.sum
                        total += node.key
                    node = node.left
                else:
                    if node.left:
                        total += node.left.sum
                    total += node.key
                    node = node.right

            return total
        
        return sum_less_than(right) - sum_less_than(left-1)
    
class RangeSumSet:
    def __init__(self):
        self.tree = AVLTree()
        self.values = set()

    def add(self, value):
        if value not in self.values:
            self.values.add(value)
            self.tree.insert(value)

    def remove(self, value):
        if value in self.values:
            self.values.remove(value)
            self.tree.delete(value)

    def find(self, value):
        return value in self.values
    
    def sum_range(self, left, right):
        return self.tree.range_sum(left, right)
    
def process_input():
    M = 1000000001
    range_sum_set = RangeSumSet()
    operations = []
    last_sum = 0

    n = int(input())
    for _ in range(n):
        query = input().split()
        op = query[0]
        if op in ['+', '-', '?']:
            x = (int(query[1]) + last_sum) % M
            operations.append((op, x))
        elif op == 's':
            l = (int(query[1]) + last_sum) % M
            r = (int(query[2]) + last_sum) % M
            operations.append((op, l, r))
            last_sum = range_sum_set.sum_range(l, r)
    
    return operations

def generate_output(operations):
    M = 1000000001
    range_sum_set = RangeSumSet()
    last_sum = 0
    output = []

    for op in operations:
        if op[0] == '+':
            range_sum_set.add(op[1])
        elif op[0] == '-':
            range_sum_set.remove(op[1])
        elif op[0] == '?':
            if range_sum_set.find(op[1]):
                output.append("Found")
            else:
                output.append("Not found")

        elif op[0] == 's':
            l, r = op[1], op[2]
            last_sum = range_sum_set.sum_range(l, r)
            output.append(str(last_sum))

    return output

def main():
    operations = process_input()
    output = generate_output(operations)
    for line in output:
        print(line)

if __name__ == "__main__":
    main()