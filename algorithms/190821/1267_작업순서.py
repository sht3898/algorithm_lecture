import sys; sys.stdin = open('1267_input.txt', 'r')

for tc in range(1, 11):
    v, e = map(int, input().split())
    arr = []
    route = list(map(int, input().split()))
    for i in range(0, len(route)+1, 2):
        arr.append([route[i], route[i+1]])
    print(arr)