import sys; sys.stdin = open('1242_input.txt', 'r')
import pprint

NUM = {'3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4, '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9}


def password(arr):
    n = len(arr)
    prev = arr[0]
    cnt = 1
    result = ''
    for i in range(1, n):
        if arr[i] == prev:
            cnt += 1
        else:
            result += str(cnt)
            cnt = 1
        prev = arr[i]
    result += str(cnt)
    return result


T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(N, M)
