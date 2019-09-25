import sys; sys.stdin = open('5185_input.txt', 'r')

for TC in range(1, int(input())+1):
    N, num = input().split()
    num = '0x'+num
    binary = int(num, 16)
    final = format(binary, 'b')
    print('#{}'.format(TC), end=' ')
    if len(final) != 4*int(N):
        print('0'*(4*int(N) - len(final)) + final)
    else:
        print(final)