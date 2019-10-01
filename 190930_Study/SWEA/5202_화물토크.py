import sys; sys.stdin = open('5202_input.txt', 'r')


for TC in range(1, int(input())+1):
    N = int(input())
    works = [0] * N
    for i in range(N):      # works 에 데이터를 입력받아 저장
        works[i] = list(map(int, input().split()))
    
    print('#{}'.format(TC), end=' ')
    print()