import sys; sys.stdin = open('10163_input.txt', 'r')

N = int(input())
maps = [[0] * 101 for _ in range(101)]
count = [0] * (N+1)

for num in range(1, N+1):
    arr = list(map(int, input().split()))
    x, y, width, height = arr[0], arr[1], arr[2], arr[3]
    for i in range(x, x+width):
        for j in range(y, y+height):
            maps[i][j] = num

for row in maps:
    for idx in range(1, N+1):
        count[idx] += row.count(idx)

for result in count[1:]:
    print(result)