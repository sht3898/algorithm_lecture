# N = 3   # (0, 1, 2)
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             print(i, j, k)

# N = 3   # 중복불가순열
# for i in range(N):
#     for j in range(N):
#         if i == j: continue
#         for k in range(N):
#             if k == i or k == j: continue
#             print(i, j, k)


# N = 3   # 중복불가순열
# visit = [0] * 3 # 방문 기록 남기기
# for i in range(N):
#     if visit[i]: continue
#     visit[i] = 1
#     # ----------------------------
#     for j in range(N):
#         if visit[j]: continue
#         visit[j] = 1
#         # ----------------------------
#         for k in range(N):
#             if visit[k]: continue
#             visit[k] = 1
#             print(i, j, k)
#             visit[k] = 0
#         # ----------------------------
#         visit[j] = 0
#     # ----------------------------
#     visit[i] = 0

order = []  # 3C2
visit = [0] * 3
N = 3


def perm(k, n):
    if k == n:
        print(order)
        return
    for i in range(N):
        if visit[i]: continue
        visit[i] = 1
        order.append(i)
        perm(k+1, n)
        visit[i] = 0
        order.pop()
        perm(k+1, n)


perm(0, N)
