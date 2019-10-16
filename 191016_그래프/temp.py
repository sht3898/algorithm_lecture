import sys; sys.stdin = open('1232_input.txt', 'r')


def calc(v):
    if len(T[v]) == 2:
        return int(T[v][1])
    l = calc(int(T[v][2]))
    r = calc(int(T[v][3]))

    if T[v][1] == '+':
        return l + r
    elif T[v][1] == '-':
        return l - r
    elif T[v][1] == '*':
        return l * r
    else:
        return l // r


for TC in range(1, 11):
    N = int(input())
    T = [[]]
    for i in range(N):
        T.append(list(input().split()))

    print('#{} {}'.format(TC, calc(1)))