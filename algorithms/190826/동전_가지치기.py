coin = [6, 4, 1]        # 오름차순보다 내림차순이 최적해를 더 빨리 찾음
choose = [0] * 100
MIN = 0xffffff


def coinChange(k, n):   # k: 선택한 동전의 수, n: 거스름돈 금액
    if k >= MIN: return
    if n == 0:
        global MIN
        MIN = min(k, MIN)
        for i in range(k):
            print(choose[i], end=' ')
        print()
        return
    for c in coin:
        if c > n: continue
        choose[k] = c
        coinChange(k + 1, n - c)


coinChange(0, 8)
