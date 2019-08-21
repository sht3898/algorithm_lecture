import sys
sys.stdin = open('sum.txt', 'r')

tc = int(input())

for idx in range(tc):
    arr = list(range(1, 13))
    n = len(arr)
    N, K = map(int, input().split())
    count = [0] * tc
    for i in range(1 << n):
        result = []
        for j in range(n):
            if i & (1 << j):
                result.append(arr[j])
        if len(result) == N and sum(result) == K:
            count[idx] += 1
    print('#{} {}'.format(idx+1, count[idx]))
