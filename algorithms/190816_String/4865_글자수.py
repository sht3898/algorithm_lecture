import sys; sys.stdin = open('4865_input.txt', 'r')

T = int(input())

for TC in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    str1 = set(str1)
    counts = []
    for i in str1:
        counts.append(str2.count(i))
    print('#{} {}'.format(TC, max(counts)))
