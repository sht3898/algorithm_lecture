# import sys; sys.stdin = open('1220_input.txt', 'r')
import sys; sys.stdin = open('1220.txt', 'r')

# for tc in range(1, 11):
for tc in range(1, 2):
    n = int(input())
    arr = []
    # 테이블 배치 생성
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    count = 0

    for y in range(n):
        check = 0  # 교착이 있나 확인
        for x in range(n):
            if arr[x][y] == 0:
                continue  # 빈칸이 있나 체크
            elif check == 0 and arr[x][y] == 2:
                continue
            elif check == 1 and arr[x][y] == 2:
                count += 1
                check = 0
            elif arr[x][y] == 1:
                check = 1

    print('#{} {}'.format(tc, count))
