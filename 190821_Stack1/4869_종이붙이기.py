import sys; sys.stdin = open('4869_input.txt', 'r')


def paper(x):
    if x == n:
        return 1
    if x > n:
        return 0
    return paper(x+10) + paper(x+20)*2


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    print('#{} {}'.format(tc, paper(0)))
