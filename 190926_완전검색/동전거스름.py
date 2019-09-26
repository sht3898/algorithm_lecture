coins = [6, 4, 1]
choose = []
MIN = 0xffffff


def coinChange(k, n):   # k: 선택한 동전수, n: 거스름돈 금액
    # if n < 0: return
    global MIN
    if k >= MIN: return
    if n == 0:
        if MIN > k:
            MIN = k
            print(MIN, choose)
    else:
        for coin in coins:
            if coin > n: continue
            choose.append(coin)
            coinChange(k+1, n - coin)
            choose.pop()


coinChange(0, 8)


def coinChange2(n): # 매개변수, 문제의 크기(식별), 반환값 : 문제의 해
    if n == 0: return 0
    MIN = 0xfffffff
    for coin in coins:
        if coin > n:continue
        ret = coinChange2(n - coin) + 1
        if ret < MIN: MIN = ret

    return MIN


print(coinChange2(8))

memo = [-1] * 100
def coinChange3(n): # 매개변수, 문제의 크기(식별), 반환값 : 문제의 해
    if n == 0: return 0
    if memo[n] != -1: return memo[n]
    MIN = 0xfffffff
    for coin in coins:
        if coin > n:continue
        ret = coinChange3(n - coin) + 1
        if ret < MIN: MIN = ret
    memo[n] = MIN
    return MIN


print(coinChange3(80))
