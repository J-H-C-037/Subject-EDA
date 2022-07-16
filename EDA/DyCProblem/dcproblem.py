# JIAHAO CHEN G89 100472232

import sys


def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""

    # if list empty or a is not a list or x is not int
    # (as specified in the heading of the function (line 5),
    # x has to be an int), return

    if type(a) != list or len(a) == 0 or type(x) != int:
        return -1, -1

    sol1, sol2 = _find_first_last(a, x, 0)

    # if sol1 is the maximum value, that means that x hasn't been found
    if sol1 == sys.maxsize:
        return -1, -1
    else:
        return sol1, sol2


def _find_first_last(a: list, x: int, start_in: int) -> (int, int):
    # start is useful to count the index of x in the original a

    # base case when a has 1 element
    # we stop the recursion and
    # compare if the element is x

    if len(a) == 1:
        if a[0] == x:
            return start_in, start_in
        # if a[0] is not x, we return +inf and -inf
        return sys.maxsize, -sys.maxsize

    mid: int = len(a) // 2

    # divide

    first1, last1 = _find_first_last(a[:mid], x, start_in)
    first2, last2 = _find_first_last(a[mid:], x, start_in + mid)

    # conquer
    # return minimum and maximum

    return min(first1, first2), max(last1, last2)


if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)

    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4  # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
