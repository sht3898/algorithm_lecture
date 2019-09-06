import sys; sys.stdin = open('4880_input.txt', 'r')


def win(a, b):
    if (cards[a-1] == 1 and cards[b-1] == 3) or (cards[a-1] == 1 and cards[b-1] == 1):
        return a
    elif (cards[a-1] == 2 and cards[b-1] == 1) or (cards[a-1] == 2 and cards[b-1] == 2):
        return a
    elif (cards[a-1] == 3 and cards[b-1] == 2) or (cards[a-1] == 3 and cards[b-1] == 3):
        return a
    return b


def winner(start, end):
    if start == end:
        return start
    a = winner(start, (start+end)//2)
    b = winner((start+end)//2 + 1, end)
    return win(a, b)


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    start = 1
    end = n
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, winner(1, end)))
