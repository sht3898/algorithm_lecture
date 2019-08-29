import sys; sys.stdin = open('부분집합_input.txt', 'r')


def subset(k, n, cnt, cur_sum): # cnt: 현재 선택한 원소수, cur_sum: 원소들합
    global N, K
    if cnt > N or cur_sum > K: return 0
    if k == n:
        if cnt == N and cur_sum == K: return 1
        else: return 0
    ret = 0
    subset(k + 1, n, cnt + 1, cur_sum + k)    # 왼쪽
    subset(k + 1, n, cnt, cur_sum + k)    # 오른쪽
    return ret


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    print('#{} {}'.format(tc, subset(1, 13, 0, 0)))