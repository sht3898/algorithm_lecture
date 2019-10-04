import sys; sys.stdin = open('5203_input.txt', 'r')


for TC in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    one, two = [], []
    ans = 0
    for i in range(len(arr)):
        one_cnt, two_cnt = 0, 0
        if ans == 1 or ans == 2:
            break
        if i % 2 == 0:
            one.append(arr[i])
            one.sort()
            one_set = set(one)
            one_set = list(one_set)
            for j in range(0, len(one_set)-2):
                if one_set[j+2] - one_set[j+1] == 1 and one_set[j+1] - one_set[j] == 1:
                    ans = 1
                    break
            for k in one_set:
                if one.count(k) >= 3:
                    ans = 1
                    break
        else:
            two.append(arr[i])
            two.sort()
            two_set = set(two)
            two_set = list(two_set)
            for j in range(0, len(two_set)-2):
                if two_set[j + 2] - two_set[j + 1] == 1 and two_set[j + 1] - two_set[j] == 1:
                    ans = 2
                    break
            for k in two_set:
                if two.count(k) >= 3:
                    ans = 2
                    break
    print('#{} {}'.format(TC, ans))
