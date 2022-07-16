# -*- coding: utf-8 -*-
"""Graph-AdjacencyMatrixWD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PEeQwNhJ4ocaW_C_BqG2BqUXUopW6X7t

# Adjacency Matrix for any kind of graph

This implementation allows us to represent any kind of graph: weighted, unweighted, directed or undirected.
"""


class Graph(object):
    """This is an implementation for an unweighted and undirected graph based on an adjacency matrix"""

    def __init__(self, vertices, directed=False):
        """This constructors gets a Python list of vertices and creates an empty adjacency matrix.
        It also gets directed (by default False). Its value is True, it means that the
        graph will be directed.  """
        # labels is the set of vertices, for example, A, B, C, D...

        self._vertices = vertices
        self._directed = directed
        N = len(vertices)
        # we initializae the matrix with 0s
        self._matrix = [[None for i in range(N)] for j in range(N)]

    def _index(self, v):
        """gets a vertex and returs its index. If v does not exist,
		it shows an error message and returns -1"""
        try:
            index = self._vertices.index(v)
        except:
            print(v, ' is not a vertex!!!')
            index = -1
        return index

    def addEdge(self, start, end, w=1):
        """gets two vertices and adds an edge from start to end. w is the weight
        of the edge (start,end). If it is ommited, its value es 1"""
        # first, we get their indeces
        i, j = self._index(start), self._index(end)
        if i == -1:
            print('[addEdge]: {} does not exist!!!'.format(start))
            return
        if j == -1:
            print('[addEdge]: {} does not exist!!!'.format(end))
            return
        # now, we modify its element in the matrix
        self._matrix[i][j] = w
        if not self._directed:
            self._matrix[j][i] = w

        print('[addEdge]: ({},{}) was added!!!'.format(start, end))

    def containEdge(self, start, end):
        """checks if the edge from start to end exists."""
        i, j = self._index(start), self._index(end)
        if i == -1:
            print('[containEdge]: {} does not exist!!!'.format(start))
            return False
        if j == -1:
            print('[containEdge]: {} does not exist!!!'.format(end))
            return False

        return self._matrix[i][j] != None

    def removeEdge(self, start, end):
        """removes the edge from start to end. It must
        modify its corresponding element in the matrix to 0."""
        i, j = self._index(start), self._index(end)
        if i == -1:
            print('[removeEdge]: {} does not exist!!!'.format(start))
            return
        if j == -1:
            print('[removeEdge]: {} does not exist!!!'.format(end))
            return

        self._matrix[i][j] == None
        if not self._directed:
            self._matrix[j][i] == None

    def __str__(self):
        """returns the matrix"""
        result = ' '
        # the first row are the vertices
        for l in self._vertices:
            result += '  ' + l

        result += '\n'

        for i, row in enumerate(self._matrix):
            result += self._vertices[i] + ' ' + str(row) + '\n'

        return result


"""Now, we use the implementation to represent this directed and unweighted graph:


<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Directed_graph%2C_cyclic.svg/900px-Directed_graph%2C_cyclic.svg.png' width='35%'/>
"""
if __name__ == '__main__':
    labels = ['A', 'B', 'C', 'D', 'E', 'F']

    g = Graph(labels)

    # Now, we add the edges
    g.addEdge('A', 'B')  # A->B
    g.addEdge('B', 'C')  # B->C
    g.addEdge('C', 'E')  # C->E
    g.addEdge('D', 'B')  # D->B
    g.addEdge('E', 'D')  # E->D
    g.addEdge('E', 'F')  # E->D

    print(g)

    """We use the implementation to represent an undirected graph without weights :


    <img src='https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png' width='35%'/>
    """

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph(labels, False)
    g.addEdge('A', 'B')  # A:0, B:1
    g.addEdge('A', 'C')  # A:0, C:2
    g.addEdge('A', 'E')  # A:0, E:5
    g.addEdge('B', 'D')  # B:1, D:4
    g.addEdge('B', 'E')  # C:2, B:1
    # g.addEdge('A','H',8)

    print(g)

    """Now, we use the implementation to represent a directed and weighted graph: 

    <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>
    """

    labels = ['A', 'B', 'C', 'D', 'E']

    g = Graph(labels)

    # Now, we add the edges
    g.addEdge('A', 'C', 12)  # A->(12)C
    g.addEdge('A', 'D', 60)  # A->(60)D
    g.addEdge('B', 'A', 10)  # B->(10)A
    g.addEdge('C', 'B', 20)  # C->(20)B
    g.addEdge('C', 'D', 32)  # C->(32)D
    g.addEdge('E', 'A', 7)  # E->(7)A

    print(g)

    print('containEdge(C,B)', g.containEdge('C', 'B'))
    print()
    g.removeEdge('C', 'B')

    print(g)