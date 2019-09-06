import sys; sys.stdin = open('1224_input.txt', 'r')

icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}


for tc in range(1, 11):
    n = int(input())
    arr = input()
    numbers = []
    token = []
    stack = []
    for i in range(n):
        temp = arr[i]
        if temp.isdigit():
            numbers.append(temp)
        else:
            if not token:
                token.append(temp)
                continue
            else:
                if temp == ')':
                    while token[-1] != '(':
                        numbers.append(token.pop())
                    token.pop()

                elif icp[temp] > isp[token[-1]]:
                    token.append(temp)

                else:
                    while token and (icp[temp] <= isp[token[-1]]):
                        numbers.append(token.pop())
                    token.append(temp)

    for j in numbers:
        if j.isdigit():
            stack.append(j)
        else:
            num1, num2 = int(stack.pop()), int(stack.pop())
            if j == '+':
                stack.append(num1 + num2)
            elif j == '*':
                stack.append(num1 * num2)

    print('#{} {}'.format(tc, *stack))
