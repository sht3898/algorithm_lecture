import sys; sys.stdin = open('5099_input.txt', 'r')

T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())    # N: 화덕의 크기, M: 피자의 크기
    arr = list(map(int, input().split()))   # 피자의 목록 받아오기
    pizza = [[arr[i], i+1] for i in range(N)]   # 치즈의 높이와 인덱스 번호를 pizza 에 저장

    i = 0   # 인덱스 번호 비교를 위한 변수
    while len(pizza) > 1:  # pizza 의 길이가 1보다 클 때
        pizza[0][0] //= 2   # pizza 의 첫번째 원소를 2로 나눔

        if pizza[0][0] == 0:    # pizza 의 치즈의 높이가 0일때
            if N < M - i:   # 화덕의 크기보다 남은 피자의 크기가 클 때
                pizza.pop(0)    # pizza 의 첫 번째 원소를 삭제함
                pizza.append([arr[N + i], N + i + 1])   # pizza 에 아직 추가되지 않는 피자를 추가함
                i += 1  # 비교하기 위한 인덱스 번호를 1 늘림
            elif N >= M - i:    # 화덕의 크기가 남은 피자의 크기보다 클 때
                pizza.pop(0)    # 피자를 삭제하기(남은 피자가 1이 될 때까지)
        else:
            pizza.append(pizza.pop(0))  # pop 했던 피자를 다시 추가하여 화로에 있는 피자가 모두 비교되게함

    print('#{} {}'.format(TC, pizza[0][1]))
