import sys; sys.stdin = open('5122_input.txt', 'r')

T = int(input())

for TC in range(1, T+1):
    N, M, L = map(int, input().split())  # 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L
    arr = list(map(int, input().split()))
    for _ in range(M):
        i = list(input().split())
        if i[0] == 'I':
            arr.insert(int(i[1]), int(i[2]))
        elif i[0] == 'D':
            arr = arr[:int(i[1])] + arr[int(i[1])+1:]
        else:
            arr[int(i[1])] = int(i[2])
    print('#{}'.format(TC), end=' ')
    if len(arr) >= L:
        print(arr[L])
    else:
        print(-1)
