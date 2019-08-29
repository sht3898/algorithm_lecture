memo = [-1] * (101)

def fibo(n):
    if n == 0 or n == 1:
        return n
    if memo[n] != -1:
        return memo[n]

    memo[n] =  fibo(n - 1) + fibo(n - 2)
    return memo[n]

print(fibo(40))