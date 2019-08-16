import sys
sys.stdin = open('팰린드롬1.txt', 'r')

tc = int(input())

for t in range(1, tc+1):
    word = input()
    for i in range(len(word)//2):
        if word[i] != '?' and word[len(word)-i-1] != '?' and word[i] != word[len(word)-i-1]:
            print('#{} Not exist'.format(t))
            break
    else:
        print('#{} Exist'.format(t))