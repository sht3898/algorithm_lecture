import sys; sys.stdin = open('5432_input.txt', 'r')

T = int(input())


for TC in range(1, T+1):
    arr = list(input())
    print(*arr)
