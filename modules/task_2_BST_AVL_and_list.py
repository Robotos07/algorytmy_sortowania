import data_generator;
import time;
import file;

tab = []
r = data_generator.generate_random_array(30000,1000,100000)

for x in r:
    if x not in tab:
        tab.append(x)

print('li')

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

        return node

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

        return node

    def _min_value(self, node):
        current = node

        while current.left:
            current = current.left

        return current

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0

        return 1 + max(self._height(node.left), self._height(node.right))

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

list_create_t = []
bst_create_t = []

list_search_t = []
bst_search_t = []

list_delete_t = []
bst_delete_t = []

bst_h = []
avl_h = []

for n in tab:

    data = tab

    linked_list = SortedLinkedList()

    start = time.perf_counter()

    for x in data:
        linked_list.insert_sorted(x)

    end = time.perf_counter()

    list_create_t.append(end - start)

    bst = BST()

    start = time.perf_counter()


    for i, x in enumerate(data, start=1):
        bst.insert(x)
        bst_h.append((bst.height()))

    end = time.perf_counter()

    bst_create_t.append(end - start)

    start = time.perf_counter()

    for x in data:
        linked_list.search(x)

    end = time.perf_counter()

    list_search_t.append(end - start)

    start = time.perf_counter()

    for x in data:
        bst.search(x)

    end = time.perf_counter()

    bst_search_t.append(end - start)

    start = time.perf_counter()

    while linked_list.head:
        linked_list.delete_first()

    end = time.perf_counter()

    list_delete_t.append(end - start)

    start = time.perf_counter()

    sorted_data_desc = sorted(data, reverse=True)

    for x in sorted_data_desc:
        bst.delete(x)

    end = time.perf_counter()

    bst_delete_t.append(end - start)

    bst2 = BST()

    for x in data:
        bst2.insert(x)

    bst_h.append(bst2.height())

    inorder_data = bst2.inorder()

    avl = AVLTree()

    def build_balance(arr):
        if not arr:
            return

        mid = len(arr) // 2

        avl.insert(arr[mid])

        build_balance(arr[:mid])
        build_balance(arr[mid + 1:])

    build_balance(inorder_data)

    avl_h.append(avl.height())

i = 1000
points = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000, 30000]

for element in list_create_t:
    if i in points:
        file.save_data([element], 'list_create_t')
    i=i+1000

for element in list_search_t:
    if i in points:
        file.save_data([element], 'list_search_t')
    i=i+1000
    

for element in list_delete_t:
    if i in points:
        file.save_data([element], 'list_delete_t')
    i=i+1000

for element in bst_create_t:
    if i in points:
        file.save_data([element], 'bst_create_t')
    i=i+1000

for element in bst_search_t:
    if i in points:
        file.save_data([element], 'bst_search_t')
    i=i+1000

for element in bst_delete_t:
    if i in points:
        file.save_data([element], 'bst_delete_t')
    i=i+1000

for element in bst_h:
    if i in points:
        file.save_data([element], 'bst_h')
    i=i+1000

for element in avl_h:
    if i in points:
        file.save_data([element], 'avl_h')
    i=i+1000