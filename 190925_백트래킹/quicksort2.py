arr = [69, 10, 30, 2, 16, 8, 31, 22]


def quicksort(lo, hi):
    if lo >= hi: return
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] < arr[hi]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[hi] = arr[hi], arr[i]

    quicksort(lo, i-1)
    quicksort(i+1, hi)


print(*arr)
quicksort(0, len(arr)-1)
print(*arr)
