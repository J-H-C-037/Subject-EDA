def quicksort(data):
    return _quicksort(data, 0, len(data)-1)

def _quicksort(data, left, right):
    i = left
    j = right
    m = (left + right) // 2
    p = data[m]#pivot element in the middle
    while i <= j: #while left index < right index
        while data[i] < p:
            i += 1
        while data[j] > p:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
    if left < j: #sort left list
        _quicksort(data, left, j)
    if i < right: #sort right list
        _quicksort(data, i, right)
    return data

l = quicksort([2,3254,234,234,23,4,3,2,1])



print(l)