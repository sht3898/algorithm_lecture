import sys
sys.stdin = open('bingo.txt', 'r')

arr = []
speak = []
result = [[0]*5 for _ in range(5)]
count = 0


for _ in range(5):
    arr.append(list(map(int, input().split())))

for _ in range(5):
    speak += list(map(int, input().split()))

for num in speak:
    bingo = 0
    count += 1
    for a in range(5):
        for b in range(5):
            if arr[a][b] == num:
                result[a][b] = 1

    # 가로
    # for width in result:
    #     if sum(width) == 5:
    #         bingo += 1
    for a in range(5):
        temp = 0
        for b in range(5):
            temp += result[a][b]
        if temp == 5:
            bingo += 1

    # 세로
    for a in range(5):
        temp = 0
        for b in range(5):
            temp += result[b][a]
        if temp == 5:
            bingo += 1

    # 대각선
    temp2 = 0
    for idx in range(5):
        for idx2 in range(5):
            if idx + idx2 == 4:
                temp2 += result[a][b]
        if temp2 == 5:
            bingo += 1
    # print(result)

    if bingo >= 3:
        print(count)
        break
