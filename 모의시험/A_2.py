import sys; sys.stdin = open('A_2.txt', 'r')
import pprint

# 0: 상, 1: 하, 2: 좌, 3: 우

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    location = []
    for i in arr:
        location.append([i[0], i[1]])
    for _ in range(10):
        for i in range(n):
            if arr[i][2] == 0:
                location[i][0] += 0.5
            elif arr[i][2] == 1:
                location[i][0] -= 0.5
            elif arr[i][2] == 2:
                location[i][1] -= 0.5
            elif arr[i][2] == 3:
                location[i][1] += 0.5
        for j in range(n):
            print(location.count(location[j]))
            # if location.count(location[j]) > 1:
            #     count += 1
            #     location.pop(j)
    print(count)
