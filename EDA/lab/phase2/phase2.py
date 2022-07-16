from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def _rebalance(self, node: BinaryNode) -> BinaryNode:

        # If tree has one node, just return it
        if node is None:
            return node

        # Get the balance factor of the node and its children's
        balanceF = self.BalanceFactor(node)
        left_BF = self.BalanceFactor(node.left)
        right_BF = self.BalanceFactor(node.right)

        # Simple right rotation
        if balanceF > 1 and left_BF >= 0:
            return self.rightRot(node)

        # Simple Left Rotation
        if balanceF < -1 and right_BF <= 0:
            return self.leftRot(node)

        # Left-Right Rotation
        if balanceF > 1 and left_BF < 0:
            node.left = self.leftRot(node.left)
            return self.rightRot(node)

        # Right-Left Rotation
        if balanceF < -1 and right_BF > 0:
            node.right = self.rightRot(node.right)
            return self.leftRot(node)

        return node

    def BalanceFactor(self, node):  # Obtain the balance factor of the node
        if not node:
            return 0

        return self._height(node.left) - self._height(node.right)

    # Rotations
    # Node becomes its child's child
    # Node's child becomes node's parent

    def leftRot(self, node):  # Left Rotation
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        return newRoot

    def rightRot(self, node):  # Right rotation
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        return newRoot