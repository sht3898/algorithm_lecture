import sys
sys.stdin = open('5204_input.txt', 'r')


def merge(left, right):
    global cnt

    left_n, right_n = len(left), len(right)     # 왼쪽 길이, 오른쪽 길이
    result = [0] * (left_n + right_n)       # 결과를 저장
    left_i, right_i = 0, 0      # 왼쪽 인덱스, 오른쪽 인덱스
    i = 0       # 인덱스

    if left[-1] > right[-1]:        # 왼쪽 끝값이 오른쪽 끝값보다 크면
        cnt += 1        # cnt 1 증가

    while left_i < left_n and right_i < right_n:    # 왼(오른)쪽 인덱스가 왼(오른)쪽 길이보다 작을때
        if left[left_i] <= right[right_i]:
            result[i] += left[left_i]
            i += 1
            left_i += 1
        else:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    if left_i != left_n:
        while left_i != left_n:
            result[i] += left[left_i]
            i += 1
            left_i += 1

    if right_i != right_n:
        while right_i != right_n:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    return result


def merge_sort(lst):    # 끝까지 쪼개서 결합
    if len(lst) <= 1:   # 길이 1이면 lst 반환
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print('#{} {} {}'.format(TC, arr[N//2], cnt))
