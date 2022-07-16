from re import I
from slist import SList
from slist import SNode
import sys


class SList2(SList):

    def sumLastN(self, n):

        if n < 0:  # No result if n is negative
            return None

        inode = self._head
        sum = 0

        for i in range(self._size):  # Go through each node's position
            if i >= (self._size - n):  # Once reached 'size-n' position, sums the 'N' lasts elements
                sum += inode.elem
            inode = inode.next

        return sum

    def insertMiddle(self, elem):

        if self._size == 0:  # If empty, add one with 'addFirst"
            self.addFirst(elem)
            return

        # Set mid position, 'size//2' for even list and 'size//2 +1' for odd list
        mid = self._size // 2
        if self._size % 2 != 0:
            mid += 1

        node = self._head
        for i in range(mid - 1):  # Find mid position
            node = node.next

        newnode = SNode(elem)  # Create new element's node

        # Insert it into the list
        newnode.next = node.next
        node.next = newnode
        self._size += 1

    def insertList(self, inputList, start, end):

        if not 0 <= start <= end < self._size:  # No result if inputs are not valids
            return

        # Find the node before 'start' node

        node = self._head
        for i in range(start - 1):
            node = node.next

        # Go through nodes between 'start' - 'end ' and stop at the first node after 'end' node

        node2 = node.next
        for i in range(end - start):
            node2 = node2.next

        if start == 0:  # Check if 'start ' is the head of the list
            self._head = node2  # If so, the node after end will be the head
        else:
            node.next = node2.next  # If not, just connect both nodes
            # (Every nodes between them will disapear)

        node = self._head  # Find 'start' prev node position again
        for i in range(start - 1):
            node = node.next

        temp = node

        newnode = inputList._head

        if start == 0:  # If 'start" is the head of the list, the nodes of the inputList is inserted at the beginning
            self._head = newnode
            # New nodes will be added since head position and them connect the last added to the beginning node of the old list
            for i in range(inputList._size - 1):
                newnode = newnode.next
            newnode.next = temp
        else: #inputList is inserted at the middle
            temp1 = node.next
            node.next = newnode
            while node.next: #go to the end of the inputList after connect it to the first half part of the self.list
                node = node.next

            node.next = temp1

        self._size = self._size + inputList._size - (end -start +1) #renew the size of the list

    def reverseK(self, k):  #
        if self._head == None:  # No result if the list's empty
            return

        current = self._head

        # guardar el next original de actual
        # cambiar next de actual a prev
        # guardar el actual como prev
        # actualizar el atual como next orginal de actual

        for i in range(self._size // k + 1):  # Number of times reversing each subgroup
            count = 0
            prev = None
            first_time = True

            # example: [0, 1, 2], k = 2

            while current and (count % k != 0 or first_time):
                first_time = False
                next = current.next  # 1 -> 2, 2 -> None, None
                current.next = prev  # 0-> None, 1 -> 0 -> None, 2 -> None
                prev = current  # 0 -> None, 1-> 0 -> None, 2
                current = next  # 1 -> 2, 2 -> None, None
                count += 1

            if i == 0:  # If reverse the first subgroup, we set the 'head'
                self._head = prev  # 1 -> 0 -> None
            else: #for the rest of the cases, we connect them to the last node of the previous subgroups
                node = self._head
                while node.next:
                    node = node.next

                node.next = prev  # , 1 -> 0 -> 2 -> None

    def reverse(self):  # Funtion that return a new reversed list

        l = SList2()
        node = self._head

        while node:
            l.addFirst(node.elem)
            node = node.next

        return l

    def maximumPair(self):

        if self._size == 0:  # No result if list's empty
            return

        max, current, node = 0, 0, self._head  # 'current' will be compared with 'max'

        node2 = self.reverse()._head  # Returns a reversed list's head (with previous defined reverse function)

        times = self._size // 2  # Number of pairs, plus one if 'size' is odd
        if self._size % 2 == 1:
            times += 1

        # It goes through two list simultaneously
        for i in range(times):  # According to the number of pairs, the process repeats 'times' times
            if i == times - 1 and self._size % 2 == 1:  # If one node left and the list is odd, current's value is this node's elements
                current = node.elem
            else:  # Sum the equidistant elements to 'current'
                current += node.elem
                current += node2.elem

            if current >= max:  # If the sum is bigger than 'max', save 'current' as new 'max'
                max = current

            node, node2 = node.next, node2.next  # Move to next node
            current = 0  # Reset to 0

        return max  # When loop ends, return the max saved