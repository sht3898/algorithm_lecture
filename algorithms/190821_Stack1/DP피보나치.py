memo = [-1] * (101)

def fibo(n):
    memo[0], memo[1] = 0, 1

    for i in range(2, n + 1):  # --> 문제를 식별하는 값
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

print(fibo(40))