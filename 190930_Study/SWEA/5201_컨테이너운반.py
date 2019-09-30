import sys; sys.stdin = open('5201_input.txt', 'r')

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())    # N: 컨테이너 수, M: 트럭 수
    wages = list(map(int, input().split()))  # N개 화물의 무게
    volumes = list(map(int, input().split()))   # M개 트럭의 적재용량
    result = 0  # 결과를 저장할 값 
    wages.sort(reverse=True)    # 큰 것부터 정렬
    volumes.sort(reverse=True)
    while wages and volumes:    # 남은 화물과 트럭이 있으면
        if wages[0] <= volumes[0]:  # 첫째 화물 크기(가장 큰 화물)보다 첫째 트럭의 적재용량(가장 큰 트럭)이 크면
            result += wages.pop(0)     # result 에 첫째 화물의 크기를 더함   
            volumes.pop(0)  # 트럭 제거(한 트럭에 하나의 화물만 가능)
        else:
            wages.pop(0)    # 첫째 트럭에도 안들어가면 나머지 트럭에도 안들어감
    print('#{}'.format(TC), end=' ')
    print(result)