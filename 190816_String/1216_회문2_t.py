import sys
sys.stdin = open('회문2.txt', 'r')

for tc in range(1, 11):
    N = int(input()) # 회문길이
    arr = [input() for _ in range(100)]

    ans = 1 # 지금까지 찾은 최대 길이
    for idx in range(100):
        for s in range(100):
            for e in range(99, s, -1):
                L = e - s + 1
                if L <= ans: break
                for i in range(L//2):
                    if arr[idx][s + i] != arr[idx][e-i]: break
                else:
                    ans = L
                if L <= ans: break
                for i in range(L//2):
                    if arr[s+i][idx] != arr[e-i][idx]: break
                else:
                    ans = L
    print('#{} {}'.format(tc, ans))