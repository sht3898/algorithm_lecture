arr = [6, 4, 2, 5, 1, 9, 2, 11, 8, 7]


def getMin(lo, hi):             # lo: 범위의 시작, hi: 범위 끝
    if lo == hi:
        return arr[lo]

    return min(arr[hi], getMin(lo, hi - 1))


print(getMin(0, len(arr) - 1))



# def getMin(lo, hi):             # lo: 범위의 시작, hi: 범위 끝
#     if lo == hi:
#         return arr[lo]
#
#     mid = (lo + hi) >> 1
#
#     return min(getMin(lo, mid), getMin(mid + 1, hi))
#
#
# print(getMin(0, len(arr) - 1))