import sys; sys.stdin = open('1244_input.txt', 'r')

N = int(input())
switch = list(map(int, input().split()))
switch = [0] + switch
student = int(input())

for _ in range(1, student+1):
    gender, number = map(int, input().split())
    number = number
    if gender == 1:
        for i in range(1, number+1):
            if 0 <= number*i <= N:
                if switch[number*i] == 0:
                    switch[number*i] = 1
                else:
                    switch[number*i] = 0
    elif gender == 2:
        for i in range(number+1):
            if switch[number+i] == switch[number-i]:
                if switch[number+i] == 1:
                    switch[number+i] = 0
                    switch[number-i] = 0
                elif switch[number+i] == 0:
                    switch[number+i] = 1
                    switch[number-i] = 1
            else:
                break

switch = switch[1:]
switch = map(str, switch)
print(' '.join(switch))