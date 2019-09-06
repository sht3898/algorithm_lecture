import sys; sys.stdin = open('4873_input.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    arr = list(input())
    n = len(arr)
    stack = []
    for i in range(n):
        if not stack or arr[i] != stack[-1]:
            stack.append(arr[i])
        elif stack and arr[i] == stack[-1]:
            stack.pop()
    print('#{} {}'.format(tc, len(stack)))
