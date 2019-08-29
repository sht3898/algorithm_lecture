import sys; sys.stdin = open('4047_input.txt')


t = int(input())

for tc in range(1, t+1):
    arr = input()
    cards = []
    stack = []
    numbers = [13] * 4
    error = 0
    S = ['S0' + str(i) for i in range(1, 10)]
    S += ['S' + str(i) for i in range(10, 14)]
    D = ['D0' + str(i) for i in range(1, 10)]
    D += ['D' + str(i) for i in range(10, 14)]
    H = ['H0' + str(i) for i in range(1, 10)]
    H += ['H' + str(i) for i in range(10, 14)]
    C = ['C0' + str(i) for i in range(1, 10)]
    C += ['C' + str(i) for i in range(10, 14)]
    while arr:
        cards.append(arr[:3])
        arr = arr[3:]
    for i in cards:
        if i not in stack:
            if i in S:
                numbers[0] -= 1
                stack.append(i)
            elif i in D:
                numbers[1] -= 1
                stack.append(i)
            elif i in H:
                numbers[2] -= 1
                stack.append(i)
            elif i in C:
                numbers[3] -= 1
                stack.append(i)
        elif i in stack:
            error = 1
            break

    numbers = map(str, numbers)
    if error:
        print('#{} ERROR'.format(tc))
    else:
        print('#{} {}'.format(tc, ' '.join(numbers)))
