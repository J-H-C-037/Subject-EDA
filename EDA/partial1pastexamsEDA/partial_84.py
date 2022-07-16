"JIAHAO CHEN 89"
class SNode:
    def __init__(self, e, next=None):
        self.elem = e
        self.next = next

class MySList():

    def __init__(self):
        self._head = None
        self._tail = None

    def __str__(self):
        """Returns a string with the elements of the list"""
        ###This functions returns the same format used
        ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        ###[1], [3, 4, 5]
        nodeIt = self._head
        result = '['
        while nodeIt:
            result += str(nodeIt.elem) + ", "
            nodeIt = nodeIt.next

        if len(result) > 1:
            result = result[:-2]

        result += ']'
        return result

    def append(self, e):
        """Adds a new element, e, at the end of the list"""
        # create the new node
        newNode = SNode(e)
        # the last node must point to the new node
        # now, we must update the tail reference
        if self._head == None:
            self._head = newNode
        else:
            self._tail.next = newNode

        self._tail = newNode

    def isSorted(self):
        "returns True if self is sorted"
        if self._head == None:
            return True
        else:
            node1 = self._head
            node2 = node1.next
            while node2:
                if node1.elem > node2.elem:
                    return False
                node1 = node2
                node2 = node2.next

        return True

    def merge(self, other):
        """
        1º check if both lists are ordered or not. If not -> return None
        2º Remove duplicate of both lists
        3º merge them

        """
        yes1 = False
        yes2 = False

        if self._head != None:
            node1 = self._head
            # check if the list is ordered
            while node1.next:
                if node1.next.elem > node1.elem:
                    node1 = node1.next
                elif node1.next.elem == node1.elem:  # if duplicate, remove them
                    node1.next = node1.next.next
                else:
                    return None  # the list is not ordered
            yes1 = True

        if other._head != None:
            node2 = other._head

            # check if the second list is ordered
            while node2.next:
                if node2.next.elem > node2.elem:
                    node2 = node2.next
                elif node2.next.elem == node2.elem:  # if duplicate, remove them
                    node2.next = node2.next.next
                else:
                    return None  # the list is not ordered
            yes2 = True

        if yes1 and yes2:

            # merge both lists
            sl = MySList()
            node1 = self._head
            node2 = other._head
            inode = None

            while node1 and node2:
                if node1.elem < node2.elem:
                    if sl._head == None:
                        sl._head = node1
                        inode = sl._head
                    else:
                        inode.next = node1
                        inode = inode.next
                    node1 = node1.next
                elif node1.elem > node2.elem:
                    if sl._head == None:
                        sl._head = node2
                        inode = sl._head
                    else:
                        inode.next = node2
                        inode = inode.next
                    node2 = node2.next

                elif node1.elem == node2.elem:
                    if sl._head == None:
                        sl._head = node1
                        inode = sl._head
                    else:
                        inode.next = node1
                        inode = inode.next
                    node1 = node1.next
                    node2 = node2.next

            if node1:
                if inode.elem < node1.elem:
                    inode.next = node1
            elif node2:
                if inode.elem < node2.elem:
                    inode.next = node2
            return sl

        elif yes1:
            return self
        elif yes2:
            return other
        else:
            return self

    ...


import random

if __name__ == '__main__':
    # Please, uncomment the code for test each function
    l2 = MySList()

    for i in range(10):
        l2.append(random.randint(0, 20))
    print(l2)

    l3 = MySList()
    for i in range(10):
        l3.append(i)

    print('l2:', str(l2))
    print('l3:', str(l3))

    print("List merged:", str(l2.merge(l3)))
    print("List merged:", str(l3.merge(l2)))

    data = []
    for i in range(5):
        x = random.randint(0, 10)
        if x not in data:
            data.append(x)

    data.sort()
    l2 = MySList()
    for x in data:
        l2.append(x)

    data = []
    for i in range(7):
        x = random.randint(0, 10)
        if x not in data:
            data.append(x)

    data.sort()
    l3 = MySList()
    for x in data:
        l3.append(x)

    print('l2:', str(l2))
    print('l3:', str(l3))
    print("List merged:", str(l2.merge(l3)))
    print("List merged:", str(l3.merge(l2)))
