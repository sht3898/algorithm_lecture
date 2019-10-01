import sys; sys.stdin = open('5202_input.txt', 'r')


for TC in range(1, int(input())+1):
    N = int(input())
    works = [0] * N
    for i in range(N):      # works 에 데이터를 입력받아 저장
        works[i] = list(map(int, input().split()))
    for i in range(N):      # 끝나는 시간을 기준으로 내림차순 정렬
        for j in range(i, N):
            if works[i][1] > works[j][1]:
                works[i], works[j] = works[j], works[i]
    result = []
    visited = [0] * N   # 방문을 나타냄
    visited[0] = 1  # 첫 데이터 방문 표시
    result.append(works[0]) # 결과에 저장
    while True:     # 조건 반복
        for i in range(N):  # N만큼 반복하면서
            if result[-1][-1] > works[i][0]:    # 저장된 마지막 작업의 끝나는 시간이 현재 작업의 시작 시간보다 크면
                visited[i] = 1  # visited[i]를 방문으로 바꿈
        if 0 not in visited:    # 모든 작업을 끝냈으면 종료
            break

        index = 0
        value = 0xfffffff
        for i in range(N):  # N 만큼 반복하면서
            if visited[i] == 0 and result[-1][-1] <= works[i][0] and works[i][1] < value:
                # 방문하지 않았고, 저장된 마지막 작업의 끝나는 시간보다 현재 작업의 시간 시간이 크고, 현재 작업의 끝나는 시간이 value 보다 작을때
                index = i   # index 를 i로 설정
                value = works[i][0]  # value 는 현재 작업의 시작 시간으로 바꿈

        result.append(works[index])

    print('#{} {}'.format(TC, len(result)))
