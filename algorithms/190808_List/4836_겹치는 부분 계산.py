import sys
sys.stdin = open('draw.txt', 'r')

tc = int(input())

for t in range(tc):
    time = int(input())
    arr = []
    result_list = []
    count = 0
    for idx in range(time):
        arr.append(list(map(int, input().split())))
    # 결과 리스트를 저장할 빈 리스트 생성
    for _ in range(10):
        result_list.append(['']*10)
    # 리스트를 순회하며 red와 blue를 분리하여 각각 값을 결과 리스트에 저장
    for idx1 in arr:
        if idx1[4] == 1:
            for number in range(idx1[0], idx1[2]+1):
                for number2 in range(idx1[1], idx1[3]+1):
                    result_list[number][number2] += 'red'
        elif idx1[4] == 2:
            for number in range(idx1[0], idx1[2]+1):
                for number2 in range(idx1[1], idx1[3]+1):
                    result_list[number][number2] += 'blue'
    
    # 결과 리스트에 저장된 값이 redblue거나 bluered이면 count의 값을 1을 늘림
    for num1 in result_list:
        for num2 in num1:
            if num2 == 'redblue' or num2 == 'bluered':
                count += 1

    print('#{} {}'.format(t + 1, count))
