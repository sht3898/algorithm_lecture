import sys; sys.stdin = open('5120_input.txt', 'r')
from LinkedList import Node, List

T = int(input())

for TC in range(1, T+1):
    N, M, K = map(int, input().split())     # N: 숫자 개수, M: 지정 위치로부터의 칸, K:반복횟수
    arr = list(map(int, input().split()))
    print(N, M, K)
    print(arr)
    for i in range(1, K+1):
        if i*M < N:
            left, right = arr[i*M-1], arr[i*M]
            arr.insert(i*M, left+right)
        else:
            left, right = arr[(i*M) % N-1], arr[(i*M) % N]
            if i*M == N:
                arr.append(left+right)
            else:
                arr.insert((i*M) % N, left+right)
        N += 1
        print(i, i*M, len(arr), arr)
    # print(arr[::-1])
    print()