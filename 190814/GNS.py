import sys
sys.stdin = open('GNS.txt', 'r')

tc = int(input())

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(tc):
    test, n = input().split()
    arr = list(input().split())
    result = []
    print(test)
    for idx in numbers:
        cnt = arr.count(idx)
        for _ in range(cnt):
            result.append(idx)
    print(*result)