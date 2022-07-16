# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root=self._insert(self._root,elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance1(node, elem)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance2(node, elem)

        return node

    def _rebalance1(self, node: BinaryNode, elem) -> BinaryNode:
        """ gets node and balances it"""

        # Step 3 - Get the balance factor
        balance = self.getBalance(node)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and elem < node.left.elem:
            return self.rightRotate(node)

        # Case 2 - Right Right
        if balance < -1 and elem > node.right.elem:
            return self.leftRotate(node)

        # Case 3 - Left Right
        if balance > 1 and elem > node.left.elem:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Case 4 - Right Left
        if balance < -1 and elem < node.right.elem:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node
    def _rebalance2(self, node: BinaryNode, elem) -> BinaryNode:
        # If the tree has only one node,
        # simply return it
        if node is None:
            return node
        # Step 3 - Get the balance factor
        balance = self.getBalance(node)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)

        # Case 2 - Right Right
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)

        # Case 3 - Left Right
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Case 4 - Right Left
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def getBalance(self, root):
        if not root:
            return 0

        return self._height(root.left) - self._height(root.right)

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2
        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Return the new root
        return y


