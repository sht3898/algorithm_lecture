N = 8
visit = [0] * N     # 순열
cols = [0] * N      # 열의 위치 저장(0 ~ N - 1 순열)
ans = 0         # 가능한 경우의 수


def Possible(k, c): # k번 퀸의 위치(k, c)
    for i in range(k):  # i번 퀸의 위치(i, cols[i])
        if k - i == abs(c - cols[i]): return False
    return True


def nQueen(k):  # k번 퀸의 열값 결정
    if k == N:
        global ans
        ans += 1
    else:
        for i in range(N):
            if visit[i]: continue
            if not Possible(k, i): continue # k번의 퀸의 위치
            visit[i] = 1
            cols[k] = i
            nQueen(k+1)
            visit[i] = 0
