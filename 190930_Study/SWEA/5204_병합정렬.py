import sys; sys.stdin = open('5204_input.txt', 'r')


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    left, right = [], []
    left_lst, right_lst = lst[:N//2], lst[N//2:]
    for x in left_lst:
        left.append(x)
    for y in right_lst:
        right.append(y)
    merge_sort(left)
    merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
        return result


for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr)
    print(arr)