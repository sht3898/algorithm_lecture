import sys
sys.stdin = open('수련회.txt', 'r')

tc = int(input())

for t in range(1, tc+1):
    students = int(input())
    room = [0] * 401
    for _ in range(students):
        a, b = list(map(int, input().split()))
        if b % 2 == 1:
            b = b + 1
        if a > b:
            for i in range(b, a+1):
                room[i] += 1
        else:
            for i in range(a, b+1):
                room[i] += 1
    result = max(room)
    print('#{} {}'.format(t, result))
