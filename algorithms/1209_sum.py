import sys
sys.stdin = open('sum.txt', 'r')

for tc in range(10):
    t = input()
    # 이중 배열로 저장
    numbers = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []  # 합계 리스트 저장
    
    # 가로 합
    for idx in range(100):
        sum_list.append(sum(numbers[idx]))

    # 대각선 합
    for idx in range(100):
        same_list = []
        for idx2 in range(100):
            if idx+idx2 == 100:
                same_list.append(numbers[idx][idx2])
        sum_list.append(sum(same_list))

    # 세로 합
    for idx in range(100):
        height_list = []
        for idx2 in range(100):
            height_list.append(numbers[idx2][idx])
        sum_list.append(sum(height_list))

    print('#{} {}'.format(t, max(sum_list)))