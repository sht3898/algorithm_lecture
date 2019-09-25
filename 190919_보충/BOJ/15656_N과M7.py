import sys; sys.stdin = open('15654_input.txt', 'r')

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
arr = []


def solve(k):
    if k == M:
        print(*arr)
        return
    for i in range(len(numbers)):
        num = numbers[i]
        arr.append(num)
        solve(k+1)
        arr.pop()


solve(0)
