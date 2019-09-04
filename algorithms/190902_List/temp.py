import collections
def bfs(N):  # 수빈위치
   global K  # 목표위치
   # K = 21
   if N == K:
       return 0
   if N == 0:
       return K
   visit[N] = True
   dq = collections.deque()
   dq.append(N)
   while dq:
       cur = dq.popleft()  # 수빈위치
       job[2] = cur
       for i in range(3):
           if 0 <= cur + job[i] < 100001 and not visit[cur + job[i]]:
               if cur + job[i] == K:
                   return D[cur] + 1
               visit[cur + job[i]] = True
               dq.append(cur + job[i])
               D[cur + job[i]] = D[cur] + 1
#
# N, K = map(int, input().split())  # N:현재숫자, K:목표숫자
# N, K = min(N, K), max(N, K)
N, K = 3, 20
job = [1, -1, N]  # 연산작업 +1, -1, *2
visit = [False] * 100001
D = [0] * 100001  # 연산 횟수, 거리
print(bfs(N))