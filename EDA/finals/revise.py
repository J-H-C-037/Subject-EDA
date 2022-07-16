from graph import Graph
import sys
import copy

from dlist import DList

class MyGraph(Graph):


    def minimumDistance(self, visited, distances):

        min = sys.maxsize
        min_vertex = None
        for adj in self._vertices.keys():
            if visited[adj] is False and distances[adj] < min:
                min = distances[adj]
                min_vertex = adj

        return min_vertex

    def dijkstra(self, start, end):

        visited, distances, previous = {},{},{}

        for i in self._vertices:
            visited[i], distances[i], previous[i] = False, sys.maxsize, None

        distances[start] = 0

        for i in range(len(self._vertices)):
            v = self.minimumDistance(visited,distances)

            visited[v] = True

            if v == end:
                return previous

            for adj in self._vertices[v]:
                if visited[adj.vertex] is False and distances[v] + 1 < distances[adj.vertex]:
                    distances[adj.vertex] = v + 1
                    previous[adj.vertex] = v
        return previous

    def minimumPath(self, start, end):
        previous = self.dijkstra(start, end)

        v = end
        path = [end]
        while previous[v] != None:
            path.append(previous[v])
            v = previous[v]

        print(path)

    def bfs(self, origin, end):
        visited, distances = {},{}

        for i in self._vertices:
            visited[i], distances[i] = False, 0

        distances[origin] = 0
        
        q = [origin]

        while len(q) != 0:
            v = q.pop(0)
            for adj in self._vertices[v]:
                if visited[adj.vertex] is False:
                    visited[adj.vertex] = True
                    distances[adj.vertex] = distances[v] +1
                    q.append(adj.vertex)
                if adj.vertex == end:
                    return distances[end]

    def dfs(self, v, end, visited, l, l_total):

        visited[v] = True
        l.append(v)

        if v == end:
            l_total.append(l.copy())
        for adj in self._vertices[v]:
            if visited[adj.vertex] is False:
                self.dfs(adj.vertex, end, visited, l, l_total)

        l.pop()
        visited[v] = False

    def possible_paths(self, start, end):

        if (start or end) not in self._vertices.keys():
            return None

        l_total = []
        visited = {}
        for i in self._vertices.keys():
            visited[i] = False

        self.dfs(start, end, visited,[], l_total)
        return l_total


g = MyGraph([0,1,2,3,4])
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(2, 1)
g.add_edge(4,2)
g.add_edge(0,1)


g.minimumPath(0,4)

print(g.bfs(0,4))

print(g.possible_paths(0,1))

class DList2(DList):

    def quickSort(self):

        self._quickSort(0, self.size-1)

    def _quickSort(self, left, right):

        i = left
        j = right
        node1 = self.head
        node2 = self.head

        mid = self.head

        for i in range ((i+j)//2):
            mid = mid.next

        for n in range(i):
            node1 = node1.next

        for n in range(j):
            node2 = node2.next


        while i <= j:

            while node1.elem < mid.elem:
                node1 = node1.next
                i += 1
            while node2.elem > mid.elem:
                node2 = node2.prev
                j -= 1
            if i <= j:
                node1.elem, node2.elem = node2.elem, node1.elem
                node1 = node1.next
                node2 = node2.prev
                i += 1
                j -= 1

        if i < right:
            self._quickSort(i, right)
        if left < j:
            self._quickSort(left, j)

    def split(self, data):
        d1,d2 = DList2(), DList2()

        i = 0
        mid = len(data)//2

        node = data.head
        while node:
            if i < mid:
                d1.addLast(node.elem)
            else:
                d2.addLast(node.elem)
            node = node.next
            i += 1
        return d1,d2

    def mergeSort(self):
        return self._mergeSort(self)

    def _mergeSort(self, data):
        if len(data) == 0 or data is None:
            return None
        if data.size == 1:
            return data

        l1,l2 = self.split(data)

        sorted1 = self._mergeSort(l1)
        sorted2 = self._mergeSort(l2)
        return self.merge(sorted1, sorted2)

    def merge(self, d1, d2):

        d = DList2()

        node1 = d1.head
        node2 = d2.head

        while node1 and node2:
            if node1.elem <= node2.elem:
                d.addLast(node1.elem)
                node1 = node1.next
            else:
                d.addLast(node2.elem)
                node2 = node2.next

        while node1:
            d.addLast(node1.elem)
            node1 = node1.next
        while node2:
            d.addLast(node2.elem)
            node2 = node2.next

        return d

d = DList2()

for i in [1,5,2,5,6,7,0]:
    d.addLast(i)
