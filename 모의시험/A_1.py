import sys; sys.stdin = open('A_1.txt', 'r')

def back(cards, cnt):
    global Min
    if cnt > 5 or cnt > Min:
        return
    if cards == cards_s or cards = cards_r:
        Min = min(Min, cnt)
    else:
        for i in range(1, N):
            cards_c = suffle(cards, i)
            back(cards_ cnt+1)


def shuffle(cards, x):
    new_cards = [0] * N
    if x < N//2:
        j = 0
        for i in range(N):
            if i < N//2 - x or i >= N//2 + x:
                new_cards[i] = cards[i]
            else:
                if j % 2:
                    new_cards[i] = cards[N//2-x+j//2]
                    j += 1
                else:
                    new_cards[i] = cards[N // 2 + j // 2]