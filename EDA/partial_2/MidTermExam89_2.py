#Jiahao Chen Group 89


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

    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: MyNode, elem: object) -> MyNode:
        if node is None:
            print(elem, ' not found')
            return node

        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # node.elem == elem, node is the node to remove!!!
            if node.left is None and node.right is None:
                # Case 1: node is a leave
                return None
            # Case 2: node only has a child, so the function has to return it
            if node.left is None:
                # It only has the right child
                return node.right
            elif node.right is None:
                # It only has the left child
                return node.left
            else:
                successor = self._minimum_node(node.right)
                node.elem = successor.elem
                node.right = self._remove(node.right, successor.elem)

        return node

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n')

    def _draw(self, prefix: str, node: MyNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def yearsRegistrationDiff(self, year1: str, year2: str) -> int:
        """Receives 2 years as input parameters and returns
        an integer with the difference between the number of clients
        registered in year1 and the number of clients registered in year2"""

        count1, count2 = 0, 0 #we set the initial value to 0

        count1, count2 = self._yearsRegistrationDiff(self._root, count1, count2, year1, year2)

        return count1 - count2

    def _yearsRegistrationDiff(self, node: MyNode, count1: int, count2:int, year1:str, year2:str):
        """
        #1º SOLUTION O(n)

        if node:
            if year1 == node.elem[:4]:
                count1 += 1
            if year2 == node.elem[:4]:
                count2 += 1
            count1, count2 = self._yearsRegistrationDiff(node.left, count1, count2, year1, year2)
            count1, count2 = self._yearsRegistrationDiff(node.right, count1, count2, year1, year2)
        return count1, count2

        """

        #Second Solution which skips some innecesary cases. Yet, it is still O(n) for time complexity

        if node: #If the node is not None we continues
            # If the client is registered in the same year, add 1 to count
            if year1 == node.elem[:4]:
                count1 += 1
            if year2 == node.elem[:4]:
                count2 += 1

            #We skip some subtrees if we can

            if int(year1) < int(node.elem[:4]) and int(year2) < int(node.elem[:4]): #If both years are smaller than the registration year of the client, we only check the left subtree
                count1, count2 = self._yearsRegistrationDiff(node.left, count1, count2, year1, year2)
            elif int(year1) > int(node.elem[:4]) and int(year2) > int(node.elem[:4]): #If both years are greater than the registration year of the client, we only check the right subtre
                count1, count2 = self._yearsRegistrationDiff(node.right, count1, count2, year1, year2)
            else: #for the rest of cases, check both subtrees
                count1, count2 = self._yearsRegistrationDiff(node.left, count1, count2, year1, year2)
                count1, count2 = self._yearsRegistrationDiff(node.right, count1, count2, year1, year2)

        return count1, count2 #return the counts

    """
    #3º Solution using lists (less space efficient)

    def yearsRegistrationDiff(self, year1: str, year2: str) -> int:

        list1 = []
        list2 = []
        self._yearsRegistrationDiff3(self._root, list1, list2, year1, year2)

        return len(list1) - len(list2)

    def _yearsRegistrationDiff(self, node, list1, list2, year1, year2):

        if node:  # If the node is not None we continues
            # If the client is registered in the same year, add 1 element to list
            if year1 == node.elem[:4]:
                list1.append(node.elem)
            if year2 == node.elem[:4]:
                list2.append(node.elem)

            if int(year1) < int(node.elem[:4]) and int(year2) < int(node.elem[:4]):  # If both years are smaller than the registration year of the client, we only check the left subtree
                list1, list2 = self._yearsRegistrationDiff(node.left, list1, list2, year1, year2)
            elif int(year1) > int(node.elem[:4]) and int(year2) > int(node.elem[:4]):  # If both years are greater than the registration year of the client, we only check the right subtre
                list1, list2 = self._yearsRegistrationDiff(node.right, list1, list2, year1, year2)
            else:  # for the rest of cases, check both subtrees
                list1, list2 = self._yearsRegistrationDiff(node.left, list1, list2, year1, year2)
                list1, list2 = self._yearsRegistrationDiff(node.right, list1, list2, year1, year2)

        return list1, list2  # return the lists
    """



if __name__ == "__main__":

    # case full binary tree True
    tree = MyBST()

    for x in ["202104271600", "202001231710", "202201230510", "202201231710", "202103031243", "201909211100",
              "202110221243", "201912031243", "202204271742", "202110031243"]:
        tree.add(x)

    tree.draw()
    print(tree.yearsRegistrationDiff("2021", "2022"))
    print(tree.yearsRegistrationDiff("2022", "2021"))
    print(tree.yearsRegistrationDiff("2021", "2020"))
    print(tree.yearsRegistrationDiff("2020", "2019"))
    print(tree.yearsRegistrationDiff("2019", "2018"))
    print(tree.yearsRegistrationDiff("2019", "2022"))


