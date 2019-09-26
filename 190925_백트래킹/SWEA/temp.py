import sys; sys.stdin = open('5186_input.txt', 'r')

for TC in range(1, int(input())+1):
    N = float(input())
    cnt = 0
    result = ''
    while True:
        next_num = N * 2
        result += str(int(next_num))
        N = next_num - int(next_num)
        cnt += 1
        if N == 0:
            break
        if cnt > 12:
            break
    print('#{}'.format(TC), end=' ')
    if cnt <= 12:
        print('{}'.format(result))
    else:
        print('overflow')
