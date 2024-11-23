# data_structures.py

class DataStructures:
    """
    ### Data Structure-Based Algorithms:
    1. Binary Search Tree (BST)
    2. AVL Tree & Red-Black Tree
    3. Hashing (Chaining, Open Addressing)
    4. Fenwick Tree / Binary Indexed Tree
    5. Segment Tree
    6. Union-Find (Disjoint Set Union)
    7. Heap
    """
    
    # Binary Search Tree (BST)
    class BSTNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
    
    
    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, root, key):
            """Inserts a new node with the given key into the BST."""
            if root is None:
                return DataStructures.BSTNode(key)  # Use DataStructures.BSTNode
            if key < root.key:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
            return root

        def inorder(self, root):
            """Inorder traversal of the BST."""
            if root is not None:
                self.inorder(root.left)
                print(root.key, end=" ")
                self.inorder(root.right)

        def search(self, root, key):
            """Search for a key in the BST."""
            if root is None or root.key == key:
                return root
            if key < root.key:
                return self.search(root.left, key)
            return self.search(root.right, key)
    
    
    # AVL Tree (Self-Balancing BST)
    class AVLTreeNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1  # height of node
    
    
    class AVLTree:
        def __init__(self):
            self.root = None

        def height(self, node):
            """Returns the height of the node."""
            return node.height if node else 0

        def balance_factor(self, node):
            """Returns the balance factor of the node."""
            return self.height(node.left) - self.height(node.right)

        def right_rotate(self, y):
            """Performs a right rotation."""
            x = y.left
            T2 = x.right
            x.right = y
            y.left = T2
            y.height = max(self.height(y.left), self.height(y.right)) + 1
            x.height = max(self.height(x.left), self.height(x.right)) + 1
            return x

        def left_rotate(self, x):
            """Performs a left rotation."""
            y = x.right
            T2 = y.left
            y.left = x
            x.right = T2
            x.height = max(self.height(x.left), self.height(x.right)) + 1
            y.height = max(self.height(y.left), self.height(y.right)) + 1
            return y

        def insert(self, root, key):
            """Inserts a new key into the AVL tree and balances the tree."""
            if not root:
                return DataStructures.AVLTreeNode(key)  # Corrected reference

            if key < root.key:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)

            root.height = 1 + max(self.height(root.left), self.height(root.right))
            balance = self.balance_factor(root)

            # Balancing the tree
            if balance > 1 and key < root.left.key:
                return self.right_rotate(root)
            if balance < -1 and key > root.right.key:
                return self.left_rotate(root)
            if balance > 1 and key > root.left.key:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
            if balance < -1 and key < root.right.key:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

            return root

        def inorder(self, root):
            """Inorder traversal of the AVL tree."""
            if root is not None:
                self.inorder(root.left)
                print(root.key, end=" ")
                self.inorder(root.right)
    
    
    # Hashing (with Chaining and Open Addressing)
    class HashTableChaining:
        def __init__(self, size):
            self.size = size
            self.table = [[] for _ in range(size)]

        def hash_function(self, key):
            """Returns hash index."""
            return key % self.size

        def insert(self, key):
            """Inserts key into the hash table."""
            index = self.hash_function(key)
            self.table[index].append(key)

        def search(self, key):
            """Search for a key in the hash table."""
            index = self.hash_function(key)
            return key in self.table[index]

        def delete(self, key):
            """Deletes a key from the hash table."""
            index = self.hash_function(key)
            if key in self.table[index]:
                self.table[index].remove(key)
    
    
    class HashTableOpenAddressing:
        def __init__(self, size):
            self.size = size
            self.table = [None] * size

        def hash_function(self, key):
            """Returns hash index."""
            return key % self.size

        def insert(self, key):
            """Inserts key into the hash table using linear probing."""
            index = self.hash_function(key)
            while self.table[index] is not None:
                index = (index + 1) % self.size
            self.table[index] = key

        def search(self, key):
            """Search for a key in the hash table."""
            index = self.hash_function(key)
            while self.table[index] is not None:
                if self.table[index] == key:
                    return True
                index = (index + 1) % self.size
            return False

        def delete(self, key):
            """Deletes a key from the hash table."""
            index = self.hash_function(key)
            while self.table[index] is not None:
                if self.table[index] == key:
                    self.table[index] = None
                    return True
                index = (index + 1) % self.size
            return False
    
    
    # Fenwick Tree / Binary Indexed Tree (BIT)
    class FenwickTree:
        def __init__(self, size):
            """Fenwick Tree (Binary Indexed Tree) initialization."""
            self.size = size
            self.tree = [0] * (size + 1)

        def update(self, index, delta):
            """Updates the Fenwick Tree at a specific index."""
            while index <= self.size:
                self.tree[index] += delta
                index += index & -index

        def query(self, index):
            """Returns the sum of elements from 1 to index."""
            result = 0
            while index > 0:
                result += self.tree[index]
                index -= index & -index
            return result
    
    
    # Segment Tree
    class SegmentTree:
        def __init__(self, arr):
            """Segment Tree initialization."""
            self.n = len(arr)
            self.tree = [0] * (2 * self.n)

            # Build the tree
            for i in range(self.n):
                self.tree[self.n + i] = arr[i]
            for i in range(self.n - 1, 0, -1):
                self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

        def update(self, index, value):
            """Updates the value at a specific index."""
            index += self.n
            self.tree[index] = value
            while index > 1:
                index //= 2
                self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

        def query(self, left, right):
            """Queries the sum in the range [left, right]."""
            left += self.n
            right += self.n
            result = 0
            while left <= right:
                if left % 2 == 1:
                    result += self.tree[left]
                    left += 1
                if right % 2 == 0:
                    result += self.tree[right]
                    right -= 1
                left //= 2
                right //= 2
            return result
    
    
    # Union-Find / Disjoint Set Union (DSU)
    class UnionFind:
        def __init__(self, n):
            """Union-Find (Disjoint Set Union) initialization."""
            self.parent = list(range(n))
            self.rank = [1] * n

        def find(self, x):
            """Find the representative of the set that contains x."""
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            """Union the sets containing x and y."""
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1
    
    
    # Heap
    class Heap:
        def __init__(self):
            """Min-Heap initialization."""
            self.heap = []

        def heapify_up(self, index):
            """Heapify operation to maintain the heap property (min-heap)."""
            while index > 0 and self.heap[(index - 1) // 2] > self.heap[index]:
                self.heap[(index - 1) // 2], self.heap[index] = self.heap[index], self.heap[(index - 1) // 2]
                index = (index - 1) // 2

        def heapify_down(self, index):
            """Heapify operation to maintain the heap property (min-heap)."""
            size = len(self.heap)
            while index * 2 + 1 < size:
                left = 2 * index + 1
                right = 2 * index + 2
                smallest = index

                if left < size and self.heap[left] < self.heap[smallest]:
                    smallest = left
                if right < size and self.heap[right] < self.heap[smallest]:
                    smallest = right
                if smallest != index:
                    self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                    index = smallest
                else:
                    break

        def insert(self, value):
            """Insert a value into the heap."""
            self.heap.append(value)
            self.heapify_up(len(self.heap) - 1)

        def extract_min(self):
            """Extract the minimum value from the heap (min-heap)."""
            if len(self.heap) == 0:
                return None
            min_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heapify_down(0)
            return min_value

        def get_min(self):
            """Get the minimum value from the heap (min-heap)."""
            if len(self.heap) == 0:
                return None
            return self.heap[0]
    
    
    # Main function to test the data structure algorithms
    @staticmethod
    def main():
        # Test Binary Search Tree (BST)
        bst = DataStructures.BinarySearchTree()
        root = None
        keys = [20, 8, 22, 4, 12, 10, 14]
        for key in keys:
            root = bst.insert(root, key)
        print("BST Inorder Traversal:")
        bst.inorder(root)  # Expected output: 4 8 10 12 14 20 22
        print()

        # Test AVL Tree
        avl = DataStructures.AVLTree()
        root = None
        keys = [10, 20, 30, 15, 25]
        for key in keys:
            root = avl.insert(root, key)
        print("AVL Tree Inorder Traversal:")
        avl.inorder(root)  # Expected output: 10 15 20 25 30
        print()

        # Test HashTable with Chaining
        hash_table_chain = DataStructures.HashTableChaining(10)
        hash_table_chain.insert(10)
        hash_table_chain.insert(20)
        hash_table_chain.insert(15)
        print("Hash Table with Chaining Search (10):", hash_table_chain.search(10))  # Expected output: True
        print("Hash Table with Chaining Search (25):", hash_table_chain.search(25))  # Expected output: False
        print()

        # Test HashTable with Open Addressing
        hash_table_open = DataStructures.HashTableOpenAddressing(10)
        hash_table_open.insert(10)
        hash_table_open.insert(20)
        hash_table_open.insert(15)
        print("Hash Table with Open Addressing Search (10):", hash_table_open.search(10))  # Expected output: True
        print("Hash Table with Open Addressing Search (25):", hash_table_open.search(25))  # Expected output: False
        print()

        # Test Fenwick Tree / Binary Indexed Tree
        fenwick_tree = DataStructures.FenwickTree(5)
        fenwick_tree.update(1, 5)
        fenwick_tree.update(2, 3)
        fenwick_tree.update(3, 7)
        print("Fenwick Tree Query (1):", fenwick_tree.query(1))  # Expected output: 5
        print("Fenwick Tree Query (2):", fenwick_tree.query(2))  # Expected output: 8
        print("Fenwick Tree Query (3):", fenwick_tree.query(3))  # Expected output: 15
        print()

        # Test Segment Tree
        arr = [1, 3, 5, 7, 9, 11]
        seg_tree = DataStructures.SegmentTree(arr)
        print("Segment Tree Query (1, 3):", seg_tree.query(1, 3))  # Expected output: 15
        seg_tree.update(1, 10)
        print("Segment Tree Query (1, 3) after update:", seg_tree.query(1, 3))  # Expected output: 22
        print()

        # Test Union-Find / Disjoint Set Union (DSU)
        uf = DataStructures.UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(3, 4)
        print("Union-Find Find (0):", uf.find(0))  # Expected output: 1
        print("Union-Find Find (3):", uf.find(3))  # Expected output: 4
        print("Union-Find Find (2):", uf.find(2))  # Expected output: 1
        print()

        # Test Heap (Min-Heap)
        heap = DataStructures.Heap()
        heap.insert(3)
        heap.insert(1)
        heap.insert(5)
        heap.insert(2)
        print("Heap Extract Min:", heap.extract_min())  # Expected output: 1
        print("Heap Get Min:", heap.get_min())  # Expected output: 2


if __name__ == "__main__":
    DataStructures.main()
