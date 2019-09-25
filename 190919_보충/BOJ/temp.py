import sys; sys.stdin = open('15649_input.txt', 'r')

N, M = map(int, input().split())
solve = [0] * N
arr = []


# 4번
def solve(k, s):
    if k == M:
        print(*arr)
        return
    for i in range(N):
        arr.append(i+1)
        solve(k+1, i)
        arr.pop()


solve(0, 0)


# 3번
# def solve(k):
#     if k == M:
#         print(*arr)
#         return
#     for i in range(N):
#         arr.append(i+1)
#         solve(k+1)
#         arr.pop()
#
#
# solve(0)


# 2번
# def solve(k, s):
#     if k == M:
#         print(*arr)
#         return
#     for i in range(s, N):
#         if not check[i]:
#             check[i] = 1
#             arr.append(i+1)
#             solve(k+1, i)
#             check[i] = 0
#             arr.pop()
#
#
# solve(0, 0)


# 1번
# def solve(k):
#     if k == M:
#         print(*arr)
#         return
#     for i in range(N):
#         if not check[i]:
#             check[i] = 1
#             arr.append(i+1)
#             solve(k+1)
#             check[i] = 0
#             arr.pop()
#
#
# solve(0)
