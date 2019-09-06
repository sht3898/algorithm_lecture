import sys; sys.stdin = open('문제2.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    sum_list = [[0]*(m-k+1) for _ in range(n-k+1)]
    max_num = 0

    for i in range(0, n-k+1):
        for j in range(0, m-k+1):
            for a in range(k):
                for b in range(k):
                    x = arr[i+a][j+b]
                    if a == 0 or a == k-1:
                        sum_list[i][j] += x
                    else:
                        if b == 0 or b == k-1:
                            sum_list[i][j] += x
    for num in sum_list:
        for num2 in num:
            if num2 >= max_num:
                max_num = num2

    print('#{} {}'.format(tc, max_num))