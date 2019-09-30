import sys; sys.stdin = open('5201_input.txt', 'r')

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())    # N: 컨테이너 수, M: 트럭 수
    wages = list(map(int, input().split()))  # N개 화물의 무게
    volumes = list(map(int, input().split()))   # M개 트럭의 적재용량
    ans = 0
    for i in range(M):
        result = 0  # ans 에 현재 트럭에 적재된 화물 무게를 저장
        for wage in wages:  # 화물 각각의 무게
            if volumes[i] >= wage >= result:   # i번 트럭의 용량이 화물의 무게보다 크고, 무게가 현재 트럭에 저장된 화물 무게 보다 클 때
                result = wage   # 저장된 화물을 지금 비교하는 화물로 바꿈
        if result != 0:  # 적재된 화물이 있을 때
            wages.remove(result)    # 무게 리스트에서 결과 지우기
        ans += result   # ans 에 현재 적재된 화물 무게 추가
    print('#{}'.format(TC), end=' ')
    print(ans)
