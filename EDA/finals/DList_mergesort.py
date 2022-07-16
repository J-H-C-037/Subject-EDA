
from dlist import DList

def mergeSort(l):
    if l is None or len(l) == 0:
        return None

    if len(l) == 1:
        return l

    l1,l2 = split(l)

    sorted1 = mergeSort(l1)
    sorted2 = mergeSort(l2)
    return merge(sorted1,sorted2)

def split(l):

    l1,l2 = DList(), DList()

    node = l.head
    i = 0

    while node:
        if i < len(l) // 2:
            l1.addLast(node.elem)
        else:
            l2.addLast(node.elem)
        i += 1
        node = node.next
    return l1,l2

def merge(l1,l2):

    node1 = l1.head
    node2 = l2.head
    l = DList()

    while node1 and node2:

        if node1.elem < node2.elem:
            l.addLast(node1.elem)
            node1 = node1.next
        else:
            l.addLast(node2.elem)
            node2 = node2.next

    while node1:
        l.addLast(node1.elem)
        node1 = node1.next

    while node2:
        l.addLast(node2.elem)
        node2 = node2.next

    return l

l = DList()

for i in [6,4,2,1,1,2,3,4,5,6]:
    l.addLast(i)

l = mergeSort(l)

print(l)



