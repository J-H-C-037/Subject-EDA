from bst import BinarySearchTree, BinaryNode
from dlist import DList, DNode

class DList2(DList):
    def addLast(self, e):
        newNode = DNode(e)
        if self.head is None:
            self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode

        self.tail = newNode
        self.size = self.size + 1

class Tree2(BinarySearchTree):

    def mirror(self):
        self._mirror(self._root)

    def _mirror(self, node):
        if node is None:
            return

        node.left, node.right = node.right, node.left
        node.left = self._mirror(node.left)
        node.right = self._mirror(node.right)

        


    def non_leaves(self):
        if self._root is None:
            return None

        return self._non_leaves(self._root, DList2())

    def _non_leaves(self, node: BinaryNode, l: DList2):
        if node.left == None and node.right == None:
             return

        if node.left != None:
            self._non_leaves(node.left, l)
        l.addLast(node.elem)
        if node.right != None:
            self._non_leaves(node.right, l)
        return l

    def kth_smallest(self, k):

        self._kth_smallest(0,self._root, k)

    def _kth_smallest(self, count, node, k):
        if node is None or count >= k:
            return count

        count = self._kth_smallest(count, node.left, k)

        if count < k:
            print("The "+ str(count + 1) + "st smallest element is " + str(node.elem))
            count += 1

        count = self._kth_smallest(count, node.right, k)
        return count

aux = Tree2()
for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
    aux.insert(x)

aux.draw()

print(aux.non_leaves())
aux.kth_smallest(4)

aux.mirror()
aux.draw()
