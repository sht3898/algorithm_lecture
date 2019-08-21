import sys
sys.stdin = open('nasa.txt', 'r')

tc = int(input())

for t in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = arr
    # result = []
    result_list = []
    answer = ''

    while len(arr2) > 0:
        result_list.append(arr2[:2])
        arr2 = arr2[2:]

    for i in range(len(result_list)):
        if arr.count(result_list[i][0]) % 2:
            first = result_list[i]
        elif arr.count(result_list[i][1]) % 2:
            last = result_list[i]

    result = first

    i = 0
    while i < len(result_list):
        if result_list[i][0] == result[len(result)-1]:
            result += result_list[i]
            i = -1
        i += 1

    for num in result:
        answer += str(num) + ' '
    answer = answer[:-1]

    print('#{} {}'.format(t+1, answer))