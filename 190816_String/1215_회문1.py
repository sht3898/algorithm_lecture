import sys
sys.stdin = open('회문1.txt', 'r')

for t in range(10):
    n = int(input())
    words = []
    reverse = []
    count = 0

    for _ in range(8):
        words.append(input())

    for y in range(8):
        word = ''
        for x in range(8):
            word += words[x][y]
        reverse.append(word)

    for a in range(len(words)):
        for b in range(len(words[0])+1-n):
            if words[a][b:b+n] == words[a][b:b+n][::-1]:
                count += 1

    for a in range(len(reverse)):
        for b in range(len(reverse[0])+1-n):
            if reverse[a][b:b+n] == reverse[a][b:b+n][::-1]:
                count += 1

    print('#{} {}'.format(t+1, count))

