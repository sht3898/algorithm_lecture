import sys; sys.stdin = open('5203_input.txt', 'r')

for TC in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    print(*arr)
