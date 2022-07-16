from graph import Graph


class Graph2(Graph):

    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""

        if (start or end) not in self._vertices.keys():  # Return 0 if start of end do not exist
            return 0

        # Dictionaries which save the distance and if a node's visited or not
        visited = {}
        distance = {}
        for i in self._vertices.keys():  # False and 0 at beginning for all ertices
            visited[i] = False
            distance[i] = 0

        # Breadth-first traversal
        queue = []
        queue.append(start)
        distance[start] = 0
        visited[start] = True

        while queue:
            s = queue.pop(0)  #Pop queue's first element and look for its adjacent vertices
            for adj in self._vertices[s]:
                if visited[adj.vertex] == False:
                    queue.append(adj.vertex)  # append vertex's adjacent vertex if not visited
                    visited[adj.vertex] = True  # The vertex won't be visited again
                    distance[adj.vertex] = distance[s] + 1 #increase the distance
                if adj.vertex == end: #if we found the vertex, stop
                    return distance[end]
        return 0 #return distance 0 if end not found

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""

        # Vertices remain the same
        vertices = []
        for i in self._vertices.keys():
            vertices.append(i)
        transpose = Graph2(vertices)

        # Reverse the edeges
        for i in vertices:
            for j in self._vertices[i]:
                transpose.add_edge(j.vertex, i, j.weight)

        return transpose

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        # Dictionary that save the distance and if a node is visited or not

        visited = {}

        first = list(self._vertices.keys())[0] #first node of the graph

        for v in self._vertices.keys(): #all false at the beginning
            visited[v] = False

        self.DFS(first, visited) #depth-first traversal to see if we can reach all the nodes from the first node
        if any(visited[i] == False for i in visited.keys()):
            return False #if any of the node cannot be reached from the first node, it is not strongly connected

        gr = self.transpose() #we repeat the same procedure for the transpose of the graph

        for v in self._vertices.keys():
            visited[v] = False

        gr.DFS(first, visited) #we start from the same node used above, this is important to find out if it is strongly connected

        if any(visited[i] == False for i in visited.keys()):
            return False

        return True #if all the nodes can be reached from the same node of the graph and its transpose, it is strongly connected

    # Depth-First Traversal

    def DFS(self, v, visited):
        visited[v] = True

        for i in self._vertices[v]:
            if visited[i.vertex] == False:
                self.DFS(i.vertex, visited)