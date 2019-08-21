import sys
sys.stdin = open('sum.txt', 'r')

tc = int(input())

for idx in range(tc):
    n ,m = map(int, input().split())
    numbers = list(map(int, input().split()))
    lists = []
    result = 0
    for i in range(m, n+1):
        sum = 0
        for i2 in range(-m, 0):
            sum += numbers[i+i2]
        lists.append(sum)
        result = max(lists) - min(lists)
    print('#{} {}'.format(idx+1, result))

    # 앞의 것을 빼고 뒤의 것을 더하는 방법도 생각해 볼 수 있음
