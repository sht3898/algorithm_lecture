import sys; sys.stdin = open('2115_input.txt', 'r')

for TC in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)