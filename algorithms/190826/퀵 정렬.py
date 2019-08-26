arr = [6, 4, 2, 5, 1, 9, 2, 11, 8, 7]


def quicksort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quicksort(a, begin, p-1)
        quicksort(a, p+1, end)


def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R):
            L += 1
        while(a[R] >= a[pivot] and L < R):
            R -= 1
        if L < R:
            if L == pivot:  pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R


quicksort(arr, 0, len(arr)-1)
print(arr)