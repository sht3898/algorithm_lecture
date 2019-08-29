import sys; sys.stdin = open('5097_input.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(m):
        first = arr.pop(0)
        arr.append(first)
    print('#{} {}'.format(tc, arr[0]))
