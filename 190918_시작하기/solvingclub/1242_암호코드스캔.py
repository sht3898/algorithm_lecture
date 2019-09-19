import sys; sys.stdin = open('1242_input.txt', 'r')

# P = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3, (1, 1, 3, 2): 4, (1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7, (1, 2, 1, 3): 8, (3, 1, 1, 2): 9}
P = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    def find():
        for i in range(N):
            j = M-1
            while j >= 0:
                if arr[i][j] == '1' and arr[i-1][j] == '0':
                    pwd = []
                    for _ in range(8):
                        c2 = c3 = c4 = 0
                        while arr[i][j] == '0': j = j - 1
                        while arr[i][j] == '1': c4, j = c4 + 1, j - 1
                        while arr[i][j] == '0': c3, j = c3 + 1, j - 1
                        while arr[i][j] == '1': c2, j = c2 + 1, j - 1
                        MIN = min(c2, c3, c4)
                        pwd.append(P[(c2//MIN, c3//MIN, c4//MIN)])

                    b = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                    a = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                    if (a * 3 + b) % 10 == 0:
                        return a + b
                    return 0
                j -= 1
    print('#{} {}'.format(TC, find()))
