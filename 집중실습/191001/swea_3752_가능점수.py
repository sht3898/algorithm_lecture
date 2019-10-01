import sys
sys.stdin = open('3752_input.txt', 'r')


def solve(k, s):        # k: 트리의 높이, s: 지금까지의 점수의 합
    global cnt
    if visited[k][s] == 1:  # 방문한 값이면 바로 리턴해서 빠져나옴(가지치기)
        return
    visited[k][s] = 1   # 방문하지 않았으므로 방문 표시
    if k == N:  # 트리의 높이가 끝까지 갔으면 개수 cnt 를 1 증가
        cnt += 1
    else:
        solve(k + 1, s)             # k 번 높이에서 왼쪽 방문할 때(값 선택을 안함)
        solve(k + 1, s + arr[k])    # k 번 높이에서 오른쪽 방문할 때(값 선택)


for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [[0] * (N * 101) for _ in range(N + 1)]   # k번 높이에서 s 값이 있는지 확인
    cnt = 0
    solve(0, 0)
    print('#{} {}'.format(TC, cnt))
