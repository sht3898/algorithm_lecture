import sys
sys.stdin = open('hwoi.txt', 'r')

tc = int(input())

for t in range(tc):
    arr = list(input())
    N = len(arr)
    # 아래와 같은 슬라이싱으로 뒤집을 수 있음
    reverse = arr[::-1]
    # print(arr)
    # print(reverse)
    result = 0
    # for i in range(N):
    #     reverse.append(arr[N-1-i])
    if arr == reverse:
        result = 1
    print('#{} {}'.format(t+1, result))