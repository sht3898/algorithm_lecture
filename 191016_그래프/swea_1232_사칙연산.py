import sys; sys.stdin = open('1232_input.txt', 'r')


def calc(v):
    if len(T[v]) == 2:
        return int(T[v][1])
    left = calc(int(T[v][2]))
    right = calc(int(T[v][3]))

    if T[v][1] == '+':
        return left + right
    elif T[v][1] == '-':
        return left - right
    elif T[v][1] == '*':
        return left * right
    else:
        return left // right


for TC in range(1, 11):
    N = int(input())
    T = [[]]
    for i in range(N):
        T.append(list(input().split()))

    print('#{} {}'.format(TC, calc(1)))
