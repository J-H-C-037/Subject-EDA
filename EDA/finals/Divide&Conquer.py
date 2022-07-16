import sys


def find_num(sorted_l, num, pos = 0):
    if num not in sorted_l:
        return None
    return _find_num(sorted_l, num, pos)

def _find_num(sorted_l, num, pos = 0):
    mid = (len(sorted_l)//2)

    if sorted_l[mid] > num:
        pos = find_num(sorted_l[:mid], num, pos)
    elif sorted_l[mid] < num:
        pos = find_num(sorted_l[mid:], num, pos + mid)
    else:
        pos += mid

    return pos

def last_uppercase(str, lastupcase = None):

    if len(str) == 0 or str is None:
        return None

    if str[-1].isupper():
        return str[-1]

    return last_uppercase(str[:-1], lastupcase)


def occurence(s, c):
    if len(s) == 0 or s is None:
        return 0
    count = 0
    mid = len(s)//2
    if c == s[mid]:
        count += 1

    return count + occurence(s[:mid], c) + occurence(s[mid+1:], c)





def findMax(data):
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]

    return max(findMax(data[:len(data)//2]), findMax(data[len(data)//2:]))


print(findMax([]))

def binarySearch(data, x):
    mid = len(data)//2

    if len(data) == 0:
        return False

    if data[mid] == x:
        return True
    elif data[mid] > x:
        return binarySearch(data[:mid],x)
    else:
        return binarySearch(data[mid+1:],x)


print(binarySearch([],0))

def mergeSort(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l

    mid = len(l)//2

    return merge(mergeSort(l[:mid]), mergeSort(l[mid:]))

def merge(l1, l2):

    l = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1

    while i < len(l1):
        l.append(l1[i])
        i += 1

    while j < len(l2):
        l.append(l2[j])
        j += 1

    return l

print(mergeSort([1,6,2,4,7,4,7,0,9]))

def quickSort(data):

    return _quickSort(data, 0, len(data)-1)

def _quickSort(data, left, right):

    m = (left + right)//2
    i = left
    j = right

    while i <= j:
        while data[i] < data[m]:
            i += 1
        while data[j] > data[m]:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1

    if i < right:
        _quickSort(data, i, right)
    if j > left:
        _quickSort(data, left, j)

    return data

print(quickSort([1,23,5,12,5,1,0]))

def occurence(str: str, c:str,count:int = 0):
    if len(str) == 0:
        return count

    mid = len(str)//2

    if str[mid] == c:
        count += 1

    count = occurence(str[:mid], c, count)
    count = occurence(str[mid+1:], c, count)

    return count

print(occurence("abcdaaeaf", "b"))

"""
Con dos parámetros 

def count(s,c):
    if s is None or len(s)==0:
        return 0
        
    m=len(s)//2
    result=0
    
    if s[m]==c:
        result +=1
    count1=count(s[0:m],c)
    count2=count(s[m+1:],c)
    return result + count1+count2

"""


def longest_s(ar:list):
    if len(ar) == 0:
        return ""
    if len(ar) == 1:
        return ar[0]

    mid = len(ar)//2

    left = longest_s(ar[:mid])
    right = longest_s(ar[mid:])

    if len(left) > len(right):
        return left
    else:
        return right


print(longest_s(["abd", "LK","ADFADSFF", "VDSVAFD"]))

def short(l:list):
    if len(l) == 0:
        return l

    l3 = []

    mid = len(l)//2
    if len(l[mid]) <= 2:
        l3.append(l[mid])

    l1 = short(l[:mid])
    l2 = short(l[mid + 1:])

    return l3 + l1 + l2

print(short(["abd", "LK","ADFADSFF", "VDSVAFD", "A", "B", ",a"]))

def l_multiples(l, z):
    if len(l) == 0 or l is None:
        return []
    mid = len(l)//2
    result = []
    if l[mid] % z == 0:
        result.append(l[mid])

    left = l_multiples(l[:mid],z)
    right = l_multiples(l[mid +1:],z)

    return left + right + result

print(l_multiples([1,3,324,123,123,4,12,3], 3))


def smallest(l):
    if len(l) == 0 or l is None:
        return None
    if len(l) == 1:
        return l[0]

    mid = len(l)//2

    return min(smallest(l[:mid]), smallest(l[mid:]))


print(smallest([1,2,3,5,435123,0,-132, -999]))

def lowest_odd_even(l):
    if len(l) == 0 or l is None:
        return None

    return(lowest_odd(l), lowest_even(l))

def lowest_odd(l):
    if len(l) == 1:
        if l[0] % 2== 1:
            return l[0]
        else:
            return sys.maxsize

    mid = len(l)//2

    return min(lowest_odd(l[:mid]), lowest_odd((l[mid:])))


def lowest_even(l):
    if len(l) == 1:
        if l[0] % 2 == 0:
            return l[0]
        else:
            return sys.maxsize

    mid = len(l) // 2

    return min(lowest_even(l[:mid]), lowest_even((l[mid:])))


print(lowest_odd_even([1,2,3,5,435123,0,-132, -999]))



# FIND THE lOWEST EVEN AND LOWEST ODD
def findLowestEvenOdd(A):
    if A == None or len(A) == 0:
        return None, None

    if len(A) == 1:
        if A[0] % 2 == 0:
            return A[0], None
        else:
            return None, A[0]

    m = len(A) // 2
    part1 = A[0:m]
    part2 = A[m:]

    even1, odd1 = findLowestEvenOdd(part1)
    even2, odd2 = findLowestEvenOdd(part2)

    if even1 != None and even2 != None:
        even = min(even1, even2)
    elif even1 != None:
        even = even1
    else:
        even = even2

    if odd1 != None and odd2 != None:
        odd = min(odd1, odd2)
    elif odd1 != None:
        odd = odd1
    else:
        odd = odd2

    return even, odd


data = [1, -12, 10, 5, 7]
print("\nfindLowestEvenOdd({})={}".format(data, findLowestEvenOdd(data)))

def last_occurrence(a: list, x: int) -> int:
    return _last_occurrence(a, x, -sys.maxsize, 0)

def _last_occurrence(a, x, last, pos):
    if len(a) == 0 or a is None:
        return last

    mid = len(a)//2

    if a[mid] == x:
        last = max(last, pos + mid)
    if len(a) == 1:
        return last

    return max(_last_occurrence(a[:mid], x, last, pos), _last_occurrence(a[mid+1:], x, last, pos + mid+1))

print(last_occurrence([1,2,34,5,21,1],1))

"""

def last_occurrence(a: list, x: int) -> int:
    if a is None or len(a) == 0:
        return -1 
    return _first_occurrence(a, x, 0, len(a)-1)

def _last_occurrence(a: list, x: int, start: int, end: int) -> int:
    if start == end:
        if a[start] == x:
            return start
        else:
            return -1
    if start < end:
        m = (start + end) // 2
        index1 = _last_occurrence(a, x, start, m)
        index2 = _last_occurrence(a, x, m+1, end)
        
        return max(index1, index2)
            
    return -1
    
"""

def findMaxMin(l):
    if len(l) == 0 or l is None:
        return
    if len(l) == 1:
        return l[0],l[0]

    mid = len(l) //2

    min1, max1 = findMaxMin(l[:mid])
    min2, max2 = findMaxMin(l[mid:])

    return min(min1, min2), max(max1,max2)


print(findMaxMin([11,2,3,2143,123,12,3,1]))

import random
def smallest_out(l):

    if len(l) == 0 or l is None:
        return None
    return _smallest_out(l, 0)

def _smallest_out(l,min):

    if len(l) == 1:
        if min == l[0]:
            return min +1
        return min


    mid = len(l)//2

    min1 = _smallest_out(l[:mid],min)
    return _smallest_out(l[mid:],min1)


print(smallest_out([0,1,2,23,234,235,236,]))

data = []
n = random.randint(0, 15)

for i in range(n):
    v = random.randint(0, 5)
    if v not in data:
        data.append(v)

data.sort()


print("smallest_out({}) = {}".format(data, smallest_out(data)))
