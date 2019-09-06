import sys; sys.stdin = open('1244_input.txt', 'r')

N = int(input())
switch = list(map(int, input().split()))
switch = [0] + switch
student = int(input())

for _ in range(1, student+1):
    gender, number = map(int, input().split())
    number = number
    if gender == 1:
        for i in range(1, N+1):
            if 0 <= number*i <= N:
                if switch[number*i] == 0:
                    switch[number*i] = 1
                else:
                    switch[number*i] = 0
    else:
        for j in range(N):
            if 0 <= number + j <= N and 0 <= number - j <= N:
                if switch[number+j] == switch[number-j]:
                    if switch[number+j] == 0:
                        switch[number+j] = 1
                        switch[number+j] = 1
                    else:
                        switch[number+j] = 0
                        switch[number+j] = 0
            else:
                break


switch = switch[1:]
print(*switch)
