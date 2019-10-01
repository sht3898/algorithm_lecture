import sys; sys.stdin = open('1247_input.txt', 'r')

for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    company = arr[:2]
    home = arr[2:4]
    customers = []
    for i in range(N):
        customers.append([arr[2*i+4], arr[2*i+5]])
    print(customers)