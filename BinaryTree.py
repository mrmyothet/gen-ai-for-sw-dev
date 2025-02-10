import threading


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.height = 1  # Needed for AVL balancing
        self.val = key


class BinaryTree:
    def __init__(self):
        self.root = None
        self.lock = threading.Lock()  # Thread safety

    def insert(self, key):
        with self.lock:
            if self.root is None:
                self.root = TreeNode(key)
            else:
                self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.val:
            node.left = self._insert(node.left, key)
        elif key > node.val:
            node.right = self._insert(node.right, key)
        else:
            return node  # Ignore duplicates

        # Update height and balance tree
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _balance(self, node):
        balance = self._get_balance(node)

        if balance > 1:  # Left Heavy
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:  # Right Heavy
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)


# Example usage
bt = BinaryTree()
for value in [8, 3, 10, 1, 6, 4, 7]:
    bt.insert(value)

print("Inorder traversal of the balanced binary tree:")
bt.inorder(bt.root)
