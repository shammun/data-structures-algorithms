import sys

MOD = 1000000001

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.sum = key  # sum of all nodes in the subtree rooted at this node

class SplayTree:
    def __init__(self):
        self.root = None

    def _update_sum(self, node):
        if node:
            node.sum = node.key
            if node.left:
                node.sum += node.left.sum
            if node.right:
                node.sum += node.right.sum

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        self._update_sum(x)
        self._update_sum(y)

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        self._update_sum(x)
        self._update_sum(y)

    def _splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left:
                    self._rotate_right(x.parent)
                else:
                    self._rotate_left(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self._rotate_right(x.parent.parent)
                self._rotate_right(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self._rotate_left(x.parent.parent)
                self._rotate_left(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.right:
                self._rotate_right(x.parent)
                self._rotate_left(x.parent)
            else:
                self._rotate_left(x.parent)
                self._rotate_right(x.parent)
        self._update_sum(x)

    def find(self, key):
        if not self.root:
            return None
        x = self.root
        while x:
            if key == x.key:
                self._splay(x)
                return x
            elif key < x.key:
                if not x.left:
                    self._splay(x)
                    return None
                x = x.left
            else:
                if not x.right:
                    self._splay(x)
                    return None
                x = x.right
        return None

    def split(self, key):
        node = self.find(key)
        if not node:
            return self.root, None
        right = node.right
        node.right = None
        if right:
            right.parent = None
        self._update_sum(node)
        return node, right

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return
        node = self.find(key)
        if node and node.key == key:
            return
        new_node = Node(key)
        if not node:
            new_node.left = self.root
            if self.root:
                self.root.parent = new_node
            self.root = new_node
        elif key < node.key:
            new_node.left = node.left
            new_node.right = node
            if node.left:
                node.left.parent = new_node
            node.left = None
            node.parent = new_node
        else:
            new_node.right = node.right
            new_node.left = node
            if node.right:
                node.right.parent = new_node
            node.right = None
            node.parent = new_node
        self.root = new_node
        self._update_sum(self.root)

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        while left.right:
            left = left.right
        self._splay(left)
        left.right = right
        if right:
            right.parent = left
        self._update_sum(left)
        return left

    def delete(self, key):
        node = self.find(key)
        if not node or node.key != key:
            return
        left = node.left
        right = node.right
        if left:
            left.parent = None
        if right:
            right.parent = None
        if left:
            self.root = self.merge(left, right)
        else:
            self.root = right

    def sum(self, l, r):
        # Step 1: Split at `l`
        left, middle = self.split(l)
        # Step 2: Split the **right** subtree at `r + 1`
        right, _ = self.split(r + 1, middle.right)  # Discard the returned node
        # Step 3: Sum is the total sum in the middle subtree
        total_sum = middle.sum if middle else 0
        # Step 4: Merge the trees back
        self.root = self.merge(self.merge(left, middle), right)
        return total_sum

def process_queries():
    tree = SplayTree()
    last_sum = 0
    n = int(input())
    results = []

    for _ in range(n):
        query = input().split()
        if query[0] == '+':
            x = (int(query[1]) + last_sum) % MOD
            tree.insert(x)
        elif query[0] == '-':
            x = (int(query[1]) + last_sum) % MOD
            tree.delete(x)
        elif query[0] == '?':
            x = (int(query[1]) + last_sum) % MOD
            result = "Found" if tree.find(x) else "Not found"
            results.append(result)
        elif query[0] == 's':
            l = (int(query[1]) + last_sum) % MOD
            r = (int(query[2]) + last_sum) % MOD
            if l > r:
                l, r = r, l  # Ensure that l <= r for valid range
            current_sum = tree.sum(l, r)
            results.append(str(current_sum))
            last_sum = current_sum % MOD

    return results

if __name__ == "__main__":
    sys.setrecursionlimit(10**5)
    results = process_queries()
    for result in results:
        print(result)