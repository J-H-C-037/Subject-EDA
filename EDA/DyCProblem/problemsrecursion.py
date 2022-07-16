
def mim(list,min = None):
    if len(list) == 0:
        return min

    if min == None:
        min = list[0]
    elif list[0] < min:
        min = list[0]

    return mim(list[1:],min)


def palindrome(str):
    if str[0] == str[-1]:
        if len(str) <= 2:
            return True
        return palindrome(str[1:-1])
    else:
        return False

def sum(num, total = 0):

    total += num % 10

    if num < 10:
        return total
    else:
        return sum(num//10, total)


def checkSort(l, prev = None):

    if len(l) <= 1:
        return True

    prev = l[0]

    if l[1] >= prev:
        return checkSort(l[1:],prev)
    else:
        return False