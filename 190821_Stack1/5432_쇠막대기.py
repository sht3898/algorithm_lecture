import sys; sys.stdin = open('5432_input.txt', 'r')


T = int(input())

for TC in range(1, T+1):
    arr = input()

    ans = 0
    stick = 0
    last = 0

    for token in arr:
        if token == '(':
            stick += 1
            last = 0
        else:
            if last == 0:
                stick -= 1
                ans += stick
                last = 1
            else:
                stick -= 1
                ans += 1
    print('#{}'.format(TC), end=' ')
    print(ans)
