import sys; sys.stdin = open('1865_input.txt', 'r')

for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

