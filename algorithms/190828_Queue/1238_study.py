import sys; sys.stdin = open('1238_input.txt', 'r')


def bfs(v):
    q.append(v)
    visited[v] = 1
    result = []
    last = []
    while q:
        for _ in range(len(q)):     # 현재 단계에 있는 큐를 모두 반복하기 위함
            temp = q.pop(0)
            for w in numbers[temp]:
                if not visited[w]:
                    q.append(w)
                    visited[w] = 1
                    result.append(w)    # 현재 단계에 있는 번호를 모두 저장
        if result:      # 반복이 끝날때까지 last 에 result 를 저장하는 과정을 반복
            last = result   # 마지막에 연락을 받을 번호 저장
            result = []
    return max(last)    # 마지막에 저장된 번호 중 가장 큰 숫자 반환


for TC in range(1, 11):
    L, V = map(int, input().split())
    arr = list(map(int, input().split()))
    N = max(arr)
    numbers = [[] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    q = []
    for i in range(L//2):
        numbers[arr[2*i]].append(arr[2*i+1])
    print('#{} {}'.format(TC, bfs(V)))
