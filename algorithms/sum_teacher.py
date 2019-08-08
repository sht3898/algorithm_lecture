import sys
sys.stdin = open('sum.txt', 'r')

for tc in range(10):
    t = input()
    # 이중 배열로 저장
    arr = [list(map(int, input().split())) for _ in range(100)]
    Max = 0

    # 행 우선 순회
    for i in range(100):
        S = 0
        for j in range(100):
            S += arr[i][j]
        Max = max(Max, S)
    # 열 우선 순회
    for i in range(100):
        S = 0
        for j in range(100):
            S += arr[j][i]
        Max = max(Max, S)
    # 대각 순회
    S = 0
    for i in range(100):
        S += arr[i][99-i]
    Max = max(Max, S)

    print('#{} {}'.format(t, Max))