import sys; sys.stdin = open('7465_input.txt', 'r')


for TC in range(1, int(input())+1):
    N, M = map(int, input().split())

    p = [x for x in range(N + 1)]       # 1 ~ N, make-set(모든 설정)

    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])  # path-compression
        return p[x]
    ans = N         # 집합의 수 => 연결 컴포넌트의 수
    for _ in range(M):
        u, v = map(int, input().split())
        a = find_set(u); b = find_set(v)
        if a != b:
            p[b] = a
            ans -= 1
    print('#{} {}'.format(TC, ans))
