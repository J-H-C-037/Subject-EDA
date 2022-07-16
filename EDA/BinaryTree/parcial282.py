from typing import Tuple


class MyNode:
    def __init__(self, elem: int, node_left: 'MyNode' = None, node_right: 'MyNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right


class MyBST:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def add(self, elem: int) -> None:
        if self._root is None:
            self._root = MyNode(elem)  # if tree is empty, new node will be the root
            return  # we can leave!!!

        node = self._root  # to search the place
        not_exist = True
        while not_exist and node:
            if elem < node.elem:
                if node.left is None:  # this is the place to insert it
                    node.left = MyNode(elem)
                    not_exist = False
                else:
                    node = node.left
            elif elem > node.elem:
                if node.right is None:  # this is the place to insert it
                    node.right = MyNode(elem)
                    not_exist = False
                else:
                    node = node.right
            elif elem == node.elem:
                print('duplicate elements not allowed!!', elem, node.elem)
                not_exist = False

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: MyNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)


    def get_average_range(self, start: int, end: int) -> float:
        """returns the average of the elements that are
        between start and end. O(n)"""

        sum = 0
        nodes = 0
        sum, nodes = self._get_average_range(self._root, sum, nodes, start, end)

        if sum == 0 or start > end:
            return None

        return sum/nodes

        """
        
        #añadimos excepciones
        if end < start:
            return None

        list = []
        #creamos una función recursiva que guarde los elementos que estén en el rango
        self._get_average_range(start, end, list, self._root)

        sum = 0
        if len(list) == 0:
            return None
        else:
            for elemento in list:
                sum += elemento

        #calculamos la media
        return sum/len(list)
        """

    def _get_average_range(self, node, sum, nodes, start, end): #función recursiva para recorrer el árbol
        if node:
            if start <= node.elem <= end:
                sum += node.elem
                nodes += 1
            sum, nodes = self._get_average_range(node.left, sum, nodes, start, end)
            sum, nodes = self._get_average_range(node.right, sum, nodes, start, end)
        return sum,nodes






        """
        if node:
            #subárbol izq
            self._get_average_range(start, end, list, node.left)
            if start <= node.elem <= end: #si se encuentra en el intervalo, lo guardamos en la lista
                list.append(node.elem)
            #subárbol derecho
            self._get_average_range(start, end, list, node.right)
        """


if __name__ == "__main__":
    aux = MyBST()
    for x in [46, 11, 81, 51, 56, 94, 5, 20]:
        aux.add(x)

    aux.draw()
    pos1, pos2 = 5, 80

    print('get_average_range({}, {}) = {}'.format(pos1, pos2, aux.get_average_range(pos1, pos2)))
