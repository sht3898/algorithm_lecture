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
            for j in range(0, len(one)-2):
                if one[j+1] - one[j] == 1:
                    one_cnt += 1
                if one_cnt >= 3:
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
            for j in range(0, len(two) - 2):
                if two[j + 1] - two[j] == 1:
                    two_cnt += 1
                if two_cnt >= 3:
                    ans = 2
                    break
            for k in two_set:
                if two.count(k) >= 3:
                    ans = 2
                    break
    print('#{} {}'.format(TC, ans))
