import sys
sys.stdin = open('sample_input.txt', 'r')

tc = int(input())
for i in range(tc):
    cn = input()
    numbers = list(map(int, input().split()))
    max = min = numbers[0]
    for number in numbers:
        if number > max:
            max = number
        if number < min:
            min = number
    print('#{} {}'.format(i+1, max-min))