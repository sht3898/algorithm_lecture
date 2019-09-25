import sys; sys.stdin = open('15655_input.txt', 'r')

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
check = [0] * 10001
arr = []


def solve(k, s):
    if k == M:
        print(*arr)
        return
    for i in range(s, len(numbers)):
        num = numbers[i]
        if not check[num]:
            check[num] = 1
            arr.append(num)
            solve(k+1, i)
            check[num] = 0
            arr.pop()


solve(0, 0)
