# -*- coding: utf-8 -*-

from bintree import BinaryNode
from bintree import BinaryTree


class BinarySearchTree(BinaryTree):

    def search(self, elem: object) -> BinaryNode:
        """Returns the node whose elem is elem"""
        return self._search(self._root, elem)

    def _search(self, node: BinaryNode, elem: object) -> BinaryNode:
        """Recursive function"""
        if node is None or node.elem == elem:
            return node
        elif elem < node.elem:
            return self._search(node.left, elem)
        elif elem > node.elem:
            return self._search(node.right, elem)

    def searchit(self, elem: object) -> BinaryNode:
        """iterative function"""
        node = self._root
        while node:
            if node.elem == elem:
                # we have found it!!! we can return it and leave the function
                return node

            if elem < node.elem:
                node = node.left
            else:
                node = node.right
        return node

    def insert(self, elem: object) -> None:
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return BinaryNode(elem)

        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:
            # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node

    def minimum(self, node:BinaryNode = None) -> BinaryNode:
        if node == None:
            node = self._root

        return self._minimum_node(node)

    def _minimum_node(self, node: BinaryNode) -> BinaryNode:
        """returns the  node with the smallest elem
        in the subtree node.
        This is the node that is furthest to the left"""

        if node.left is None:
            return node.elem

        return self._minimum_node(node.left)

    def maximum(self, node: BinaryNode = None) -> BinaryNode:
        if node == None:
            node = self._root

        return self._maximum_node(node)

    def _maximum_node(self, node: BinaryNode) -> BinaryNode:
        """returns the  node with the smallest elem
        in the subtree node.
        This is the node that is furthest to the left"""

        if node.right is None:
            return node.elem

        return self._maximum_node(node.right)

    def remove(self, elem: object) -> None:
        # update the root with the new subtree after remove elem
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """It recursively searches the node. When the node is
        found, the node has to be removed"""
        ...

        return node


if __name__ == "__main__":

    aux = BinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux.insert(x)
        # aux.draw()

    aux.draw()
    print("after remove 80 (a leaf)")
    aux.remove(80)
    aux.draw()
    print()

    tree = BinarySearchTree()
    for x in [18, 11, 23, 5, 15, 20, 24, 9, 15, 22, 21, 6, 8, 7]:
        tree.insert(x)
    tree.draw()
    print('size:', tree.size())
    print('height:', tree.height())

    tree.remove(18)
    print("after remove 18 (root), replaced with its successor 20")
    tree.draw()

    tree.remove(7)
    print("after remove 7 (a leaf)")
    tree.draw()

    tree.remove(8)
    print("after remove 8 (a leaf)")
    tree.draw()

    tree.remove(5)
    print("after remove 5 (only a child), replaced with its child: 9")
    tree.draw()

    tree.remove(9)
    print("after remove 9 (only a child), replaced with its left child: 6")
    tree.draw()

    tree.remove(11)
    print("after remove 11 (two children), replaced with its successor: 15")
    tree.draw()

    tree.remove(20)
    print("after remove 20 (root), two children, replaced with its successor: 21")
    tree.draw()

    tree.remove(15)
    print("after remove 15 (only left child) -> 6")
    tree.draw()

    tree.remove(6)
    print("after remove 6 (a leaf)")
    tree.draw()

    tree.remove(8)
    print("after remove 8 (does not exist)")
    tree.draw()

    tree.remove(24)
    print("after remove 24 (a leaf)")
    tree.draw()
    print()

    for x in [5, 10, 15, 20]:
        tree.insert(x)
    print("after insert 5,10,15,20")
    tree.draw()

    tree.remove(23)
    print("after remove 23, only a left child -> 22")
    tree.draw()

    # remove a root, with only the left child
    tree.remove(22)
    print("after remove 22 (a leaf)")
    tree.draw()
    # remove a root, with only the right child
    print("after remove 5 (only a right child) ->10")
    tree.remove(5)
    tree.draw()

    print("after remove 21 (root with only a left child) -> 10")
    tree.remove(21)
    tree.draw()
