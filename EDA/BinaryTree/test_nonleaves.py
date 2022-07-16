from problemasBST import BST2
import unittest


class Test(unittest.TestCase):
    # variable estática para almacenar la nota
    nota = 0

    def setUp(self):
        values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
        self.bst1 = BST2()
        for x in values:
            self.bst1.insert(x)

        # self.bst1.draw()

        values = [12, 16, 19, 20, 4, 14, 2, 18, 10, 8, 24, 6, 1, 13]
        self.bst2 = BST2()
        for x in values:
            self.bst2.insert(x)

        # self.bst2.draw()

    def test_printNota(self):
        print('\n\n*************************')
        print("\nNota Final:", Test.nota)
        print('*************************')

    def test1_getNonLeaves(self):
        print('Case 1: tree is empty')
        tree = BST2()
        self.assertEqual(len(tree.getNonLeaves()), 0, "Fail: list should be empty")
        print('\t\t nota += 1')
        Test.nota += 1

    def test2_getNonLeaves(self):
        print('Case 2: tree only has one node')
        tree = BST2()
        tree.insert(10)
        self.assertEqual(len(tree.getNonLeaves()), 0, "Fail: list should be empty")
        print('\t\t nota += 2')
        Test.nota += 2

    def test3_getNonLeaves(self):
        print('Case 3: tree only has two nodes')
        tree = BST2()
        tree.insert(10)
        tree.insert(15)
        result = tree.getNonLeaves()
        print('result:  ', result)
        expected = [10]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [10]")
        print('\t\t nota += 1')
        Test.nota += 1

    def test4_getNonLeaves(self):
        print('Case 4: tree only has three nodes and no left subtree')
        tree = BST2()
        tree.insert(10)
        tree.insert(15)
        tree.insert(20)
        result = tree.getNonLeaves()
        print('result:  ', result)
        expected = [15, 10]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [15,10]")
        print('\t\t nota += 2')
        Test.nota += 2

    def test5_getNonLeaves(self):
        print('Case 5: tree only has three nodes and no right subtree')
        tree = BST2()
        tree.insert(20)
        tree.insert(15)
        tree.insert(10)
        result = tree.getNonLeaves()
        print('result:  ', result)
        expected = [20, 15]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [20,15]")
        print('\t\t nota += 2')
        Test.nota += 2

    def test6_getNonLeaves(self):
        print('Case 6: tree is balanced and only has three nodes')
        tree = BST2()
        tree.insert(15)
        tree.insert(10)
        tree.insert(20)
        result = tree.getNonLeaves()
        print('result:  ', result)
        expected = [15]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [10]")
        print('\t\t nota += 2')
        Test.nota += 2

    def test7_getNonLeaves(self):
        print('Case 7: tree only has two nodes')
        result = self.bst1.getNonLeaves()
        print('result:  ', result)
        expected = [40, 36, 30, 25, 20, 10]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [40, 36, 30, 25, 20, 10]")
        print('\t\t nota += 5')
        Test.nota += 5

    def test8_getNonLeaves(self):
        print('Case 7: tree only has two nodes')
        result = self.bst2.getNonLeaves()
        print('result:  ', result)
        expected = [20, 19, 16, 14, 12, 10, 8, 4, 2]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [20, 19, 16, 14, 12, 10, 8, 4, 2]")
        print('\t\t nota += 5')
        Test.nota += 5

    # Comentar para usarlo en spyder



unittest.main(argv=['first-arg-is-ignored'], exit=False)

# Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()

