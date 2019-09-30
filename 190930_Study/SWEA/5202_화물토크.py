import sys; sys.stdin = open('5202_input.txt', 'r')


for TC in range(1, int(input())+1):
    N = int(input())
    works = [0] * N
    for i in range(N):
        works[i] = list(map(int, input().split()))
    for i in range(N):
        for j in range(i, N):
            if works[i][1] > works[j][1]:
                works[i], works[j] = works[j], works[i]
    result = []
    visited = [0] * N
    visited[0] = 1
    result.append(works[0])
    while True:
        for i in range(N):
            if result[-1][-1] > works[i][0]:
                visited[i] = 1
        if not 0 in visited:
            break

        index = 0
        value = 0xfffffff
        for i in range(N):
            if visited[i] == 0 and result[-1][-1] <= works[i][0] and works[i][1] < value:
                index = i
                value = works[i][0]

        result.append(works[index])

    print('#{} {}'.format(TC, len(result)))
