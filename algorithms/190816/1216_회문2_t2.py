import sys
sys.stdin = open('회문2.txt', 'r')

for tc in range(1, 11):
    N = int(input()) # 회문길이
    arr = [input() for _ in range(100)]
    print(arr)

    ans = 1 # 지금까지 찾은 최대 길이
    for idx in range(100):
        for x in range(100): # x => 기준 위치
            # 길이가 짝수
            l, r, cnt = x, x + 1, 0
            while l >=0 and r < 100:
                if arr[idx][l] != arr[idx][r]: break
                l, r, cnt = l - 1, r + 1, cnt + 2
            ans = max(ans, cnt)

            l, r, cnt = x, x + 1, 0
            while l >= 0 and r < 100:
                if arr[idx][l] != arr[r][idx]: break
                l, r, cnt = l - 1, r + 1, cnt + 2
            ans = max(ans, cnt)

            # 길이가 홀수 => 이 부분은 수정 필요
            l, r, cnt = x - 1, x + 1, 1
            while l >= 0 and r < 100:
                if arr[idx][l] != arr[idx][r]: break
                l, r, cnt = l - 1, r + 1, cnt + 2
            ans = max(ans, cnt)

            l, r, cnt = x - 1, x + 1, 1
            while l >= 0 and r < 100:
                if arr[idx][l] != arr[r][idx]: break
                l, r, cnt = l - 1, r + 1, cnt + 2
            ans = max(ans, cnt)

    print('#{} {}'.format(tc, ans))