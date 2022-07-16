import unittest # package that contains the classes t

# from parcial282_sol import MyBST
from parcial282 import MyBST


class Test(unittest.TestCase):
    """
    - test1: tree.get_average_range(0,5) = 0
    - test2: tree.get_average_range(5,0) = 0
    - test3: tree.get_average_range(1,4) = 0
    - test4: tree.get_average_range(95,100) = 0
    - test5: tree.get_average_range(21,45) = 0
    - test6: tree.get_average_range(57,80) = 0
    - test7: tree.get_average_range(4,100)
    - test8: tree.get_average_range(10,81)
    - test9: tree.get_average_range(12,81)
    - test_10: tree.get_average_range(4,50)
    - test_11: tree.get_average_range(50, 90)
    - test_12: tree.get_average_range(5, 10)
    """
    mark = 0

    def setUp(self) -> None:
        self.tree = MyBST()
        self.data = [46, 11, 81, 51, 56, 94, 5, 20]
        for x in self.data:
            self.tree.add(x)
        # self.tree.draw()

    def test1(self) -> None:
        print("test1: tree.get_average_range(0,5)")
        input_tree = MyBST()
        # print('Input tree:')
        # input_tree.draw()
        expected = None
        result = input_tree.get_average_range(0, 4)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.5

    def test2(self) -> None:
        print("\ntest2: tree.get_average_range(5,0)")
        # print('Input tree:')
        # self.tree.draw()
        expected = None
        result = self.tree.get_average_range(5, 0)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.5

    def test3(self) -> None:
        print("\ntest3: tree.get_average_range(1,4)")
        # print('Input tree:')
        # self.tree.draw()
        expected = None
        result = self.tree.get_average_range(1, 4)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.5

    def test4(self) -> None:
        print("\ntest4: tree.get_average_range(95,100)")
        # print('Input tree:')
        # self.tree.draw()
        expected = None
        result = self.tree.get_average_range(95, 100)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.5

    def test5(self) -> None:
        print("\ntest5: tree.get_average_range(21,45)")
        # print('Input tree:')
        # self.tree.draw()
        expected = None
        result = self.tree.get_average_range(21, 45)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.75

    def test6(self) -> None:
        print("\ntest6: tree.get_average_range(57,80)")
        # print('Input tree:')
        # self.tree.draw()
        expected = None
        result = self.tree.get_average_range(57, 80)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.75

    def test7(self) -> None:
        print("\ntest7: tree.get_average_range(4,100)")
        # print('Input tree:')
        # self.tree.draw()
        expected = sum(self.data) / len(self.data)
        result = self.tree.get_average_range(4, 100)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 1.5

    def test8(self) -> None:
        print("\ntest8: tree.get_average_range(10,81)")
        # print('Input tree:')
        # self.tree.draw()
        aux = [11, 20, 46, 51, 56, 81]
        expected = sum(aux) / len(aux)
        result = self.tree.get_average_range(10, 81)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 2

    def test9(self) -> None:
        print("\ntest9: tree.get_average_range(12,81)")
        # print('Input tree:')
        # self.tree.draw()
        aux = [20, 46, 51, 56, 81]
        expected = sum(aux) / len(aux)
        result = self.tree.get_average_range(12, 81)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 2

    def test_10(self) -> None:
        print("\ntest_10: tree.get_average_range(4, 50)")
        # print('Input tree:')
        # self.tree.draw()
        aux = [5, 11, 20, 46]
        expected = sum(aux) / len(aux)
        result = self.tree.get_average_range(4, 50)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 2

    def test_11(self) -> None:
        print("\ntest_11: tree.get_average_range(50, 90)")
        # print('Input tree:')
        # self.tree.draw()
        aux = [51, 56, 81]
        expected = sum(aux) / len(aux)
        result = self.tree.get_average_range(50, 90)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 2

    def test_12(self) -> None:
        print("\ntest_12: tree.get_average_range(5, 10)")
        # print('Input tree:')
        # self.tree.draw()
        aux = [5]
        expected = sum(aux) / len(aux)
        result = self.tree.get_average_range(5, 10)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 2

    def test_z(self):
        print("Nota provisional:", Test.mark)


if __name__ == "__main__":
    unittest.main()
