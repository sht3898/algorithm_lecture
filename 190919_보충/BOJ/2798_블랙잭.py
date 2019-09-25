import sys; sys.stdin = open('2798_input.txt', 'r')


N, M = map(int, input().split())
cards = list(map(int, input().split()))
check = [0] * 300000
now_sum = 0
max_sum = 0


def solve(k):
    global now_sum, max_sum
    if k == 3:
        if M - max_sum >= M - now_sum:
            max_sum = now_sum
        return
    for i in cards:
        if not check[i]:
            check[i] = 1
            now_sum += i
            if now_sum <= M:
                solve(k+1)
            check[i] = 0
            now_sum -= i


solve(0)
print(max_sum)