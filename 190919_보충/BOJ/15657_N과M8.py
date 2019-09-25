import sys; sys.stdin = open('15655_input.txt', 'r')

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = []


def solve(k, s):
    if k == M:
        print(*arr)
        return
    for i in range(s, len(numbers)):
        num = numbers[i]
        arr.append(num)
        solve(k+1, i)
        arr.pop()


solve(0, 0)
