import sys
sys.stdin = open('input.txt', 'r')  # input을 읽어와서 한줄씩 읽음

for t in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))

    num = 0
    for i in range(n-4):
        big = max(arr[i], arr[i+1], arr[i+3], arr[i+4])
        if arr[i+2] > big:
            num += arr[i+2] - big
    print('#{} {}'.format(t, num))