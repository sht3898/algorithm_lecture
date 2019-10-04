import sys
sys.stdin = open('5204_input.txt', 'r')


def mergeSort(lo, hi):
    global result
    if lo == hi:
        return
    mid = (lo + hi - 1) >> 1    # 2로 나눔
    mergeSort(lo, mid)      # 왼쪽을 정렬시킴
    mergeSort(mid + 1, hi)  # 오른쪽을 정렬시킴
    i, j, k = lo, mid + 1, lo
    if arr[mid] > arr[hi]:
        result += 1
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            k, i = k + 1, i + 1
        else:
            tmp[k] = arr[j]
            k, j = k + 1, j + 1
    while i <= mid:
        tmp[k] = arr[i]
        k, i = k + 1, i + 1
    while j <= hi:
            tmp[k] = arr[j]
            k, j = k + 1, j + 1
    for i in range(lo, hi + 1):
        arr[i] = tmp[i]


for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    result = 0
    mergeSort(0, N - 1)
    print('#{} {} {}'.format(TC, arr[N//2], result))
