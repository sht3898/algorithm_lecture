import sys; sys.stdin = open('5105_input.txt', 'r')


t = int(input())
for tc in range(1, t+1):
    n = int(input())

    maze = []
    visit = [[0 for i in range(n)] for j in range(n)]
