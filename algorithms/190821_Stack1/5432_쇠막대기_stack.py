import sys; sys.stdin = open('5432_input.txt', 'r')

T = int(input())

for TC in range(1, T+1):

    arr = input()
    stack = []
    result = 0

    for token in arr:
        if token == '(':
            stack.append(token)
            last = token
        else:
            if last == '(': # 이전 막대기와 비교
                stack.pop()
                result += len(stack)
                last = token
            else:           # 막대기의 끝
                stack.pop()
                result += 1
    print('#{}'.format(TC), end=' ')
    print(result)
    