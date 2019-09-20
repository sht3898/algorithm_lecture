# order = []  # 3C2
# visit = [0] * 3
# N = 3
#
#
# def perm(k, n):
#     if k == n:
#         print(order)
#         return
#     for i in range(N):
#         if visit[i]: continue
#         visit[i] = 1
#         order.append(i)
#         perm(k+1, n)
#         visit[i] = 0
#         order.pop()
#         perm(k+1, n)
#
#
# perm(0, N)


arr = 'ABCDE'
N, R = 5, 3 # {0, 1, 2, 3, 4}
choose = []


def comb(k, s):     # 선택할 요소의 시작값
    if k == R:      # 모두 선택
        print(choose)
        return

    for i in range(s, N):
        choose.append(i)
        comb(k + 1, i + 1)
        choose.pop()


comb(0, 0)
