import sys

class MyGraph:
    def __init__(self,n):
        self.vertices = {}
        for i in range(n):
            self.vertices[i] = []

    def addConnection(self, i,j):
        if (i and i) in self.vertices.keys():
            self.vertices[i].append(j)
            self.vertices[j].append(i)
        else:
            print("VERTEX DOES NOT EXIST")

    def dijkstra(self,start):

        visited = {}
        previous = {}
        distances = {}

        for v in self._vertices.keys():
            visited[v] = False
            previous[v] = None
            distances[v] = sys.maxsize

        distances[start] = 0

        for n in range(len(self._vertices)):
            u = self.minDistance(distances, visited)
            visited[u] = True

            for adj in self._vertices[u]:
                i = adj._vertex
                w = adj._weight

                if visited[i] == False and distances[i] > distances[u] + w:
                    distances[i] = distances[u] + w
                    previous[i] = u

        return distances, previous

    def minDistance(self, distances, visited):
        min = sys.maxsize

        for vertex in self.vertices.keys():
            if distances[vertex] <= min and visited[vertex] == False:
                min = distances[vertex]  # update the new smallest
                min_vertex = vertex  # update the index of the smallest

        return min_vertex

    def minimumPath(self, start, end):

        print("Mininum path from ", start, " to ", end)

        if (start or end) not in self.vertices.keys():
            return None, None

        distances, previous = self.dijkstra(start)
        if distances[end] == sys.maxsize:
            print("There is not path from {} to {}".format(start, end))
            return None, sys.maxsize

        minimum_path = []
        prev = previous[end]
        while prev != None:
            minimum_path.insert(0, prev)
            prev = previous[prev]

        minimum_path.append(end)

        return minimum_path, distances[end]

    def possible_paths(self, start, end):
        if start not in self.vertices.keys():
            return None
        if end not in self.vertices.keys():
            return None

        visited = {}
        for i in self.vertices.keys():
            visited[i] = False

        l_total = []
        self._possible_paths(start, end, visited, [], l_total)
        return l_total

    def _possible_paths(self, v, end, visited, l, l_total):

        visited[v] = True
        l.append(v)

        if v == end:
            l_total.append(l.copy())
        for adj in self.vertices[v]:
            if visited[adj] is False:
                self._possible_paths(adj, end, visited, l, l_total)
        l.pop()
        visited[v] = False

g = MyGraph(5)
g.addConnection(0, 2)  # A:0,  B:1
g.addConnection(0, 3)  # A:0,  C:2
g.addConnection(2, 4)  # A:0,  E:5
g.addConnection(2, 3)  # B:1,  D:4
g.addConnection(2, 1)  # C:2,  B:1
g.addConnection(4,2)

print(g.possible_paths(0, 2))