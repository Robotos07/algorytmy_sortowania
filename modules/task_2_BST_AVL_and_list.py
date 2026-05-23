import sys
sys.setrecursionlimit(100000)

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, value):
        new_node = ListNode(value)

        if self.head is None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        while current.next and current.next.value < value:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def search(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def delete_first(self):
        if self.head:
            self.head = self.head.next

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return BSTNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

        return node

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def height(self):
        return self.get_height(self.root)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self._search(node.left, value)

        return self._search(node.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)

        elif value > node.value:
            node.right = self._delete(node.right, value)

        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = self._min_value(node.right)

            node.value = successor.value

            node.right = self._delete(node.right, successor.value)

        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

        return node

    def _min_value(self, node):
        current = node

        while current.left:
            current = current.left

        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def height(self):
        return self.get_height(self.root)