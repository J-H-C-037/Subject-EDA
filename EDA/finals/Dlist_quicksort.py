from dlist import DList


class DList2(DList):

    def quickSortDL(self):
        self._quickSort(0, self.size-1)

    def _quickSort(self, left, right):

        i = left
        j = right
        m = (i+j) //2

        first = self.head

        for n in range(i):
            first = first.next

        mid = self.head

        for r in range(m):
            mid = mid.next

        x = mid.elem

        last = self.head
        for s in range(j):
            last = last.next

        while i <= j:
            while first.elem < x:
                first = first.next
                i += 1
            while last.elem > x:
                last = last.prev
                j -= 1
            if i <= j:
                first.elem, last.elem = last.elem, first.elem
                first = first.next
                last = last.prev
                i += 1
                j -= 1

        if left < j:
            self._quickSort(left,j)
        if i < right:
            self._quickSort(i, right)

example = DList2()

for i in [12,23,123,324,1,12,3,2,4]:
    example.addLast(i)

example.quickSortDL()
print(example)

import random

L = DList2()

for i in range(16):
    L.addLast(random.randint(0, 100))

print(L)

L.quickSortDL()

print(L)
