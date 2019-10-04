import sys; sys.stdin = open('5205_input.txt', 'r')


def quickSort(arr, lo, hi):
    if lo < hi:
        i, j = lo, hi

        while i < j:
            while i <= hi and arr[i] <= arr[lo]:
                i += 1

            while arr[j] > arr[lo]:
                j -= 1

            if i >= j: break

            arr[i], arr[j] = arr[j], arr[i]

        arr[lo], arr[j] = arr[j], arr[lo]

        quickSort(arr, lo, j - 1)
        quickSort(arr, j + 1, hi)


for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, N-1)
    print('#{} {}'.format(TC, arr[N//2]))
