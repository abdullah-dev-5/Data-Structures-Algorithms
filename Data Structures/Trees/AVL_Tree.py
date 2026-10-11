
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0

        return (
            self.get_height(node.left)
            - self.get_height(node.right)
        )

    def right_rotate(self, y):
        x = y.left
        subtree = x.right

        x.right = y
        y.left = subtree

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        x.height = 1 + max(
            self.get_height(x.left),
            self.get_height(x.right)
        )

        return x

    def left_rotate(self, x):
        y = x.right
        subtree = y.left

        y.left = x
        x.right = subtree

        x.height = 1 + max(
            self.get_height(x.left),
            self.get_height(x.right)
        )

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        return y

    def insert(self, root, key):
        # 1. Normal BST insertion
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)

        elif key > root.key:
            root.right = self.insert(root.right, key)

        else:
            return root  # Ignore duplicates

        # 2. Update height
        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        # 3. Calculate balance factor
        balance = self.get_balance(root)

        # 4. Handle four imbalance cases

        # Left Left (LL)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right (RR)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right (LR)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left (RL)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

# Create the AVL tree
tree = AVLTree()
root = None

values = [10, 20, 30, 40, 50, 25]

for value in values:
    root = tree.insert(root, value)

print("Inorder traversal:")
tree.inorder(root)
print()

print("Preorder traversal:")
tree.preorder(root)
print()

print("Postorder traversal:")
tree.postorder(root)
print()