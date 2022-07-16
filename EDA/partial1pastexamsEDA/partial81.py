#JIAHAO CHEN

import random

class DNode:
    def __init__(self, elem, next=None, prev=None):
        self.elem = elem
        self.next = next
        self.prev = prev

class MyDList():

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def append(self, e):
        """Add a new element, e, at the end of the list"""
        # create the new node
        newNode = DNode(e)

        if self._size == 0:
            self._head = newNode
        else:
            newNode.prev = self._tail
            self._tail.next = newNode

        # update the reference of head to point the new node
        self._tail = newNode
        # increase the size of the list
        self._size += 1

    def __len__(self):
        return self._size

    def __str__(self):
        """Returns a string with the elements of the list"""
        nodeIt = self._head
        result = '['
        while nodeIt:
            result += str(nodeIt.elem) + ", "
            nodeIt = nodeIt.next

        if len(result) > 1:
            result = result[:-2]

        result += ']'
        return result

    def removeMultiplesOf(self, e):
        current = self._tail

        eliminate = False

        while current:
            if current.elem % e == 0:
                if eliminate:
                     if current.elem == self._head.elem:
                         self._head = current.next
                     else:
                         current.prev.next = current.next
                         current.next.prev = current.prev
                else:
                    if current.elem == e:
                        eliminate = True
            current = current.prev






l = MyDList()

l.append(1)
l.append(10)
l.append(8)
l.append(15)
l.append(10)
l.append(1)


print(l)
l.removeMultiplesOf(1)
print(l)