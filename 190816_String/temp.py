import sys
sys.stdin = open('회문.txt', 'r')

tc = int(input())

for t in range(1, tc+1):
    m, n = map(int, input().split())
    words = []
    reverse = []
    result = ''
    wd = ''

    for _ in range(m):
        words.append(input())

    for w in words:
        wd += w
    for a in range(n):
        pass

    for y in range(m):
        word = ''
        for x in range(n):
            word += words[x][y]
        reverse.append(word)

    for idx in words:
        if idx == idx[::-1]:
            result = idx
    for idx2 in reverse:
        if idx2 == idx2[::-1]:
            result = idx2

    print('#{} {}'.format(t+1, result))