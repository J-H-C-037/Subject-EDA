from SList import SNode, SList


class SList2(SList):

    def delete_last(self, c):
        if self.head is None:
            return None

        node = self.head
        current_count = 0
        last_count = 0

        while node:
            if node.elem == c:
                last_count = current_count
            node = node.next
            current_count += 1

        node = self.head

        for i in range(last_count - 1):
            node = node.next

        if node == self.head:
            self.head = node.next
        else:
            node.next = node.next.next


example = SList2()

for i in [1, 6, 2, 3, 4, 5, 6, 6, 7, 6]:
    example.addLast(i)

example.delete_last(1)
print(example)


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, u):
        if u not in self.vertices:
            self.vertices[u] = []

    def addEdge(self, u, v):
        if u not in self.vertices:
            self.addVertex(u)
        if v not in self.vertices[u]:
            self.vertices[u].append(v)

    def breadth(self, v):
        if v not in self.vertices.keys():
            return

        visited = {}

        for i in self.vertices.keys():
            visited[i] = False

        queue = []
        queue.append(v)
        visited[v] = True

        while queue:
            t = queue.pop(0)
            print(t, end = " ")
            for j in self.vertices[t]:
                if visited[j] is False:
                    visited[j] = True
                    queue.append(j)


example = Graph()

for i in [1, 2,3,4]:
    example.addVertex(i)


for i,j in [(1,4), (1,3), (4,3)]:
    example.addEdge(i,j)

example.breadth(1)
