arr = [69, 10, 30, 2, 16, 8, 31, 22]


def quickSort(lo, hi):
    if lo >= hi: return
    i, j = lo, hi   # arr[lo]: 피봇
    while i < j:
        while i <= hi and arr[lo] >= arr[i]: i += 1
        while arr[lo] < arr[j]: j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]   # 피봇을 있어야 할 위치로

    quickSort(lo, j-1)
    quickSort(j+1, hi)


print(arr)
quickSort(0, len(arr)-1)
print(arr)
