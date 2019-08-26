import sys; sys.stdin = open('부분집합_input.txt', 'r')
bits = [0] * 12


def subset(k, n):
    global N, K, ans
    if k == n:
        for i in range(N):
            if bits[i]:
                cnt, S = cnt + 1, S + (i + 1)
        if cnt == N and S == K:
            ans += 1
    else:
        bits[k] = 1;  subset(k + 1, n)    # 왼쪽
        bits[k] = 0;  subset(k + 1, n)    # 오른쪽


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    ans = 0
    subset(0, 12)
    print('#{} {}'.format(tc, ans))