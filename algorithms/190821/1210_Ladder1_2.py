import sys; sys.stdin = open('1210_input.txt', 'r')

for _ in range(10):
    t = input()
    ladders = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladders[99][i] == 2: