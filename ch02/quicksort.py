S = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def quicksort(low, high):
    if high > low:
        pivotpoint = partition(low, high)
        quicksort(low, pivotpoint)
        quicksort(pivotpoint+1, high)


def partition(low, high):
    pivotitem = S[low]
    j = low
    for i in range(low+1, high):
        if S[i] < pivotitem:
            j = j + 1
            temp = S[i]
            S[i] = S[j]
            S[j] = temp
    pivotpoint = j
    temp = S[low]
    S[low] = S[pivotpoint]
    S[pivotpoint] = temp
    return pivotpoint

quicksort(0, 9)
print(S)