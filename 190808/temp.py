import sys
sys.stdin = open('nasa.txt', 'r')

tc = int(input())

for t in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = arr
    result_list = []
    result = []
    answer = ''
    while len(arr2) > 0:
        result_list.append(arr2[:2])
        arr2 = arr2[2:]

    for i in range(len(result_list)):
        if arr.count(result_list[i][0]) % 2:
            first = result_list.pop(i)
        elif arr.count(result_list[i][1]) % 2:
            last = result_list.pop(i)
        else:
            if len(result) <= 0:
                result += result_list
            # else:



        # else:
        #     if len(result) <= 0:
        #         result += result_list[i]
        #     else:
        #         for j in range(i, len(result_list)):
        #             if result_list[j][0] == result[-1]:
        #                 result += result_list[j]

        # else:
        #     result += result_list[i]
        #     for j in range(i+1, len(result_list)):
        #         if result_list[j][0] == result_list[i][1]:
        #             result += result_list[j]
    # result = first + result
    print(result_list)
    print(result)
    for idx in result:
        answer += str(idx)+' '
    answer = answer[:-1]

    # print('#{} {}'.format(t+1, answer))
