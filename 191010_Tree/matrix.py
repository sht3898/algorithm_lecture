row = []
col = []


def matrix(start, end):
    if start == end: return 0
    MIN = 0xfffff
    for k in range(start, end):
        left = matrix(start, k)
        right = matrix(k + 1, end)
        if MIN > left + right + row[start]*col[k]*col[end]:
            MIN = left + right + row[start] * col[k] * col[end]

    return MIN
