import sys; sys.stdin = open('5108_input.txt', 'r')
from collections import deque

T = int(input())

for TC in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = deque(map(int, input().split()))
    for _ in range(M):
        idx, num = map(int, input().split())
        arr.insert(idx, num)
    print('#{} {}'.format(TC, arr[L]))
