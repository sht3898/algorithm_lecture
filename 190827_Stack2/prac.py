icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}


arr = '3+(4+5)*6+7'
n = len(arr)
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
        elif token:
            if temp == ')':
                while token[-1] != '(':
                    numbers.append(token.pop())
                token.pop()

            elif icp[temp] > isp[token[-1]]:
                token.append(temp)

            else:
                while token and icp[temp] <= isp[token[-1]]:
                    numbers.append(token.pop())
                token.append(temp)

numbers.append(token[-1])

for j in numbers:
    if j.isdigit():
        stack.append(j)
    else:
        num1, num2 = int(stack.pop()), int(stack.pop())
        if j == '+':
            stack.append(num1 + num2)
        elif j == '*':
            stack.append(num1 * num2)
print(*stack)