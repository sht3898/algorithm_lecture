import sys
sys.stdin = open('align.txt', 'r')

tc = int(input())

for t in range(tc):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    result = []
    for _ in range(5):
        result.append(arr[-1])
        arr = arr[:-1]
        result.append(arr[0])
        arr = arr[1:]
    answer = ''
    for num in result:
        answer += str(num)+' '
    answer = answer[:-1]
    print('#{} {}'.format(t+1, answer))