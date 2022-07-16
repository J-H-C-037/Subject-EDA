#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SNode:
    def __init__(self, e, next_node=None):
        self.elem = e
        self.next = next_node

class MyList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def append(self, e):
        """ adds e at the end of the list"""
        new_node = SNode(e)
        if self._head is None:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def __len__(self):
        return self._size

    def __str__(self):
        """Returns a string with the elements of the list"""
        node = self._head
        result = '['
        while node:
            result += str(node.elem) + ", "
            node = node.next

        if len(result) > 1:
            result = result[:-2]

        result += ']'
        return result

    def removeMultiplesOf(self, e):
        """searches the first occurrence of e at the list, and remove
         all multiples for e that happen after the first occurrence"""

        if self._head == None:
            return

        first_ocur = False

        node = self._head

        while node.next:
            if node.elem == e:
                first_ocur = True
            if node.next.elem % e == 0 and first_ocur:
                node.next = node.next.next
                self._size -= 1
            else:
                node = node.next

if __name__ == '__main__':
    l = MyList()
    for i in [2, 6, 3, 2, 6, 6, 4, 7, 9, 2, 2, 1, 1, 3, 3, 3, 2, 4, 9]:
        l.append(i)

    print('before removeMultiplesOf(2)', str(l))
    l.removeMultiplesOf(2)

    print('after removeMultiplesOf(2)', str(l))
