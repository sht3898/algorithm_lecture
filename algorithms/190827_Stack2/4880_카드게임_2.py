import sys; sys.stdin = open('4880_input.txt', 'r')

win = {1:3, 2:1, 3:2}


def play(lo, hi):
    if lo == hi: return lo
    mid = (lo + hi) >> 1

    l = play(lo, mid)
    r = play(mid + 1, hi)

    if cards[l] == cards[r] or win[cards[l]] == cards[r]:
        return l

    return r


# def divide(lo, hi):
#     print(lo, ',', hi)
#     if lo == hi: return
#     mid = (lo + hi) >> 1
#     # 왼쪽 lo ~ mid, 오른쪽 mid + 1 ~ hi
#     divide(lo, mid)
#     divide(mid+1, hi)
#
#
# divide(0, 7)


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    start = 1
    end = n
    cards = list(map(int, input().split()))
    # print('#{} {}'.format(tc, winner(1, end)))
