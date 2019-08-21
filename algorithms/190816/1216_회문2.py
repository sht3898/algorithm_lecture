import sys
sys.stdin = open('회문2.txt', 'r')

for t in range(1, 11):
    n = input()
    count = 0
    words = [input() for _ in range(100)]
    reverse = []

    for i in range(100):
        for j in range(100):
            for k in range(100):
                if words[i][j:k+1] == words[i][j:k+1][::-1]:
                    if len(words[i][j:k+1]) > count:
                        count = len(words[i][j:k+1])

    for y in range(100):
        word = ''
        for x in range(100):
            word += words[x][y]
        reverse.append(word)

    for i in range(100):
        for j in range(100):
            for k in range(100):
                if reverse[i][j:k+1] == reverse[i][j:k+1][::-1]:
                    if len(reverse[i][j:k+1]) > count:
                        count = len(reverse[i][j:k+1])

    print('#{} {}'.format(n, count))