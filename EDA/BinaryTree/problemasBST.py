# -*- coding: utf-8 -*-

from bst import BinarySearchTree
from bst import BinaryNode
import queue

import sys


class BST2(BinarySearchTree):
    def minimum(self) -> object:

        """returns the smallest key of the tree. What is its temporal complexity?"""
        # Complexity: O(log n)
        if self._root is None:
            print('tree is empty')
            return None

        node = self._root
        while node.left:
            node = node.left

        return node.elem

    def minimum_rec(self) -> object:
        """recursive function to return the smallest elem"""
        return self._minimum_rec(self._root)

    def _minimum_rec(self, node: 'BSTNode') -> object:
        if node is None:
            return None  # base case
        elif node.left is None:
            return node.elem  # base case
        else:
            return self._minimum_rec(node.left)  # recursive case

    def maximum(self) -> object:
        """returns the greatest elem of the tree. What is its temporal complexity?"""
        # Complexity: O(log n)
        if self._root is None:
            print('tree is empty')
            return None

        node = self._root
        while node.right:
            node = node.right

        return node.elem

    def maximum_rec(self) -> object:
        """recursive function that returns the largest object"""
        return self._maximum_rec(self._root)

    def _maximum_rec(self, node: 'BSTNode') -> object:
        if node is None:
            return None  # base case
        elif node.right is None:
            return node.elem  # base case
        else:
            return self._maximum_rec(node.right)  # base recursive

    def sum_elems(self) -> object:
        """ returns the sum of all its elems. What is its temporal complexity?"""
        # Complexity: O(n), where n is the size of the tree.
        # The function has to visit all the nodes of the tree.
        return self._sum_elems(self._root)

    def _sum_elems(self, node: 'BSTNode') -> object:
        if node:
            return node.elem + self._sum_elems(node.left) + self._sum_elems(node.right)
        else:
            return 0

    def prints10(self) -> None:
        """prints the elems of those nodes whose grandparents' elems are multiply of 10
        What is its temporal complexity"""
        # Complexity: O(n), where n is the size of the tree.
        # The function has to visit all the nodes of the tree.
        self._prints10(self._root, None, None)

    def _prints10(self, node: 'BSTNode', parent: 'BSTNode', grand: 'BSTNode') -> None:
        if node:
            self._prints10(node.left, node, parent)
            if grand and grand.elem % 10 == 0:
                print(node.elem, end=' ')
            self._prints10(node.right, node, parent)

    def _maximum_node(self, node: 'BSTNode') -> 'BSTNode':
        """returns the node with the maximum elem in the subtree node.
        This is the node that is furthest to the right
        """
        max_node = node
        while max_node.right is not None:
            max_node = max_node.right
        return max_node

    def _remove(self, node: 'BSTNode', elem: object) -> 'BSTNode':
        if node is None:
            return None

        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # elem == node.elem
            if node.left is None and node.right is None:
                # node is a leave
                node = None
            elif node.left is None:  # only has the right child
                return node.right
            elif node.right is None:  # only has the left child
                return node.left
            else:  # elem == node.elem
                predecessor = self._maximum_node(node.left)
                print('predecessor: ', predecessor.elem)
                node.elem = predecessor.elem
                node.left = self._remove(node.left, predecessor.elem)

        return node

    def fe_size(self, elem: object) -> int:
        """gives an elem, and returns the size balance factor of
        its node """
        node = self.search(elem)
        return self._fe_size(node)

    def _fe_size(self, node: 'BSTNode') -> int:
        """returns the size balance factor of the input node"""
        if node is None:
            return 0
        else:
            return abs(self._size(node.left) - self._size(node.right))

    def is_size_balanced(self) -> bool:
        """return True if the tree is size balanced"""
        return self._is_size_balanced(self._root)

    def _is_size_balanced(self, node: 'BSTNode') -> bool:
        """returns True if the node is size balanced;
        a node is balanced if its size factor is <=1 and
        its two children are size balanced"""
        if node:
            return self._fe_size(node) <= 1 and \
                   self._is_size_balanced(node.left) and \
                   self._is_size_balanced(node.right)
        else:
            return True

    def fe_height(self, elem: object) -> int:
        """gives an elem, and returns the height balance factor of
        its node """
        node = self.search(elem)
        return self._fe_height(node)

    def _fe_height(self, node: 'BSTNode') -> int:
        """returns the height balance factor of the input node"""
        if node is None:
            return 0
        else:
            return abs(self._height(node.left) - self._height(node.right))

    def is_height_balanced(self) -> bool:
        """return True if the tree is height balance, that is,
        if its root is height balanced"""
        return self._is_height_balanced(self._root)

    def _is_height_balanced(self, node: 'BSTNode') -> bool:
        """return True if the node is balanced, False e.o.c
        A node is balanced if its height balance <=1 and
        its two children are height balanced"""
        if node:
            return self._fe_height(node) <= 1 and \
                   self._is_height_balanced(node.left) and \
                   self._is_height_balanced(node.right)
        else:
            return True


    def isBinarySearchTree(self):

        return self._isBST(self.root, -sys.maxsize, sys.maxsize)

    def _isBST(self, node, min_value, max_value):

        if not node:
            return True

        value = node.elem
        if value < min_value or value > max_value:
            return False

        return self._isBST(node.left, min_value, value) and self._isBST(node.right, value, max_value)

        """
        def isBynarySearchTree(self):
            return self._isBinarySearchTree(self._root)
    
        def _isBinarySearchTree(self, node):
            if node is not None:
                if node.left.elem > node.elem or node.right.elem < node.elem:
                    return False
    
                result = self._isBinarySearchTree(node.left) and self._isBinarySearchTree(node.right)
    
                if result == False:
                    return False
    
            return True
        """

    def closest(self,value):
        return self._closest(self, self._root ,value)

    def _closest(self, node, value):
        current = node.elem

        #Base case 1 (exact match, we return the same value)
        if current.elem == value:
            return value

        #Base case 2 (dead end)
        child = node.left if value < current.elem else node.right

        if not child:
            return current

        #Recursion

        #1. We get closest value from the child
        #2. We compare if current is closer than new found one

        found = self._closest(child, value)
        if abs(value-current) < abs(value-found):
            return current
        else:
            return found

    """
    def closest(self, value):
        return self._closest(self._root, value)

    def _closest(self, node, value):

        if node is None:
            return None

        if node.elem == value:
            return node.elem

        child = node.left if value < node.elem else child = node.right
        
        if not child:
            return node.elem

        x = self._closest(child, value)
        
        if abs(x - value) < abs(node.elem - value):
            return x
        else:
            return node.elem
    """

    def isSameStructure(self,tree):
        return self._isSameStructure(self._root, tree._root)
    def _isSameStructure(self,a,b):
        #1.both empty
        if (a == None and b == None):
            return True

        #2. both non-empty. compare them

        if (a != None and b != None):
            return self._isSameStructure(a.left, b.left) and self._isSameStructure(a.right, b.right)

        #3. one empty, one not. false
        return False

        # Recursive function to transform a BST to sum tree.
        # This function traverses the tree in reverse in order so that we have
        # visited all greater key nodes of the currently visited node
    """
    def isSameStructure(self, tree):
        return self._isSameStructure(tree._root)

    def _isSameStructure(self, node1, node2):

        if node1 and node2 is None:
            return True

        if node1 or node2 is None:
            return False

        return self._isSameStructure(node1.left, node2.left) and self._isSameStructure(node1.right, node2.right)
    """
    def sumTree(self,root, sum):

        if root is not None:
            # Recursion for right subtree
            sum = self.sumTree(root.right, sum) + root.elem
            # Store sum in current node
            root.elem = sum - root.elem
            # Recursion for left subtree
            sum = self.sumTree(root.left, sum)

        return sum

    # A utility function to print inorder traversal of a binary tree
    def printInorder(self,root):

        if root is not None:
            self.printInorder(root.left)
            print(root.elem, end=" ")
            self.printInorder(root.right)

    def lwc(self, a, b):
        """returns the lowest common ancestor of a and b"""
        nodeA = self.search(a)
        if nodeA == None:  # needed if node with value a does not exists
            return None

        nodeB = self.search(b)
        if nodeB == None:
            return None
        return self._lwc(self._root, nodeA, nodeB)

    def _lwc(self, node, nodeA, nodeB):
        if node == None:
            return None
        if nodeA.elem < node.elem and nodeB.elem < node.elem:
            return self._lwc(node.left, nodeA, nodeB)

        elif nodeA.elem > node.elem and nodeB.elem > node.elem:
            return self._lwc(node.right, nodeA, nodeB)
        else:
            return node.elem

    def checkCounsins(self,a,b):
        nodeA = self.search(a)
        if nodeA == None:  # needed if node with value a does not exists
            return None

        nodeB = self.search(b)
        if nodeB == None:
            return None
        return self._checkCounsins(self._root, nodeA, nodeB)

    def _checkCounsins(self, node, nodeA, nodeB):
        if node == None:
            return False
        if nodeA.elem < node.elem and nodeB.elem < node.elem:
            return self._checkCounsins(node.left, nodeA, nodeB)

        elif nodeA.elem > node.elem and nodeB.elem > node.elem:
            return self._checkCounsins(node.right, nodeA, nodeB)
        else:
            if self.depth(node,nodeA.elem) == 2 and self.depth(node,nodeB.elem) == 2:
                return True
            return False

    def depth(self, node: BinaryNode, elem: object, depth = 0) -> BinaryNode:
        """Recursive function"""
        if node is None or node.elem == elem:
            return depth
        elif elem < node.elem:
            depth += 1
            return self.depth(node.left, elem, depth)
        elif elem > node.elem:
            depth += 1
            return self.depth(node.right, elem, depth)


    def getNonLeaves(self):

        """
        return self._getNonLeaves(self._root)

        if each recursion result is independent from the result obtained from the previous revursion,
        we can just isolate the final data that is gonna be returned (in this case the list result)
        """


        result = []
        self._getNonLeaves(self._root, result)
        return result


    def _getNonLeaves(self, node, auxL):

        """

        if node is None:
            return auxL

        if node.right != None or node.left != None:
            self._getNonLeaves(node.right,auxL)
            auxL.append(node.elem)
            self._getNonLeaves(node.left,auxL)
        return auxL

        """

        if node!=None:
            self._getNonLeaves(node.right,auxL)
            if node.left!=None or node.right!=None:
                auxL.append(node.elem)
            self._getNonLeaves(node.left,auxL)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node == None:
            return -1

        return 1 + max(self._height(node.left), self._height(node.right))

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node == None:
            return 0

        return 1 + self._size(node.left) + self._size(node.right)

    #root <left> <right>
    def preorder(self):
        print('pre-order traversal')

        self._preorder(self.root)
        print()

    def _preorder(self, currentNode):
        if currentNode != None:
            print(currentNode.elem, end=' ')

        self._preorder(currentNode.leftChild)
        self._preorder(currentNode.rightChild)

    #<left> <right> root
    def postorder(self):
        print('post-order traversal')

        self._postorder(self.root)
        print()

    def _postorder(self, currentNode):
        if currentNode != None:
            self._postorder(currentNode.leftChild)

        self._postorder(currentNode.rightChild)
        print(currentNode.elem, end=' ')

    #<left> root <right>
    def inorder(self):
        print('in-order traversal')

        self._inorder(self.root)
        print()

    def _inorder(self, currentNode):
        if currentNode != None:
            self._inorder(currentNode.leftChild)

        print(currentNode.elem, end=' ')
        self._inorder(currentNode.rightChild)

    def levelorder(self):
        if self.root == None:
            print('tree is empty')

            return
        print('level-order traversal')
        q = queue.Queue()
        q.put(self.root)  # we save the root

        while q.empty() == False:
            current = q.get()  # dequeue
            print(current.elem, end=' ')
            if current.leftChild:
                q.put(current.leftChild)
            if current.rightChild:
                q.put(current.rightChild)
        print()

    def sumTree(self):
        return self._sumTree(self._root, 0)

    def _sumTree(self, node, sum):

        if node is not None:
            sum = self._sumTree(node.right, sum) + node.elem

            node.elem = sum - node.elem

            sum = self._sumTree(node.left, sum)

        return sum

    def printInorder(self):
        self._printInorder(self._root)

    def _printInorder(self, node):
        if node is not None:
            self.printInorder(node.left)
            print(node.elem, end = " ")
            self.printInorder(node.right)



if __name__ == "__main__":
    tree = BST2()
    for x in [50, 60, 30, 20, 24, 70, 66, 65, 10, 80, 21, 15, 35, 45, 22]:
        tree.insert(x)

    print('input tree:')
    tree.draw()

    print(tree.checkCounsins(24,10))
    """
    
    print()
    print('Minimum elem of the tree:', tree.minimum())
    print('Maximum elem of the tree:', tree.maximum())
    print('sum of all its elems:', tree.sum_elems())
    print("elems whose grandparents' elems are multiply of 10")
    tree.prints10()
    print()

    tree.remove(50)
    # 50 should have been replaced by 45 as root
    print('after remove 50')
    tree.draw()

    tree.remove(70)
    print('after remove 70')
    # 70 should have been replaced by 66 as root
    tree.draw()

    tree.remove(20)
    # 20 should have been replaced by 15 as root
    print('after remove 20')
    tree.draw()

    tree.insert(55)
    tree.insert(36)
    tree.insert(50)
    tree.insert(32)
    tree.insert(56)
    print('after insert 55,36,50,32,56')
    tree.draw()
    print()
    for x in [45, 60, 30, 15, 35, 10, 24, 21, 66, 80, 63, 55, 36, 50, 32, 56]:
        print('size-balanced factor of  {} is {}'.format(x, tree.fe_size(x)))
        print('height-balanced factor of  {} is {}'.format(x, tree.fe_height(x)))
        print()
    """
