import sys; sys.stdin = open('4866_input.txt', 'r')

tc = int(input())

for t in range(1, tc+1):
    sentence = input()
    arr = []
    ans = 1

    for i in sentence:
        if i == '(' or i == '{':
            arr.append(i)
        elif i == ')' or i == '}':
            if len(arr) <= 0:
                ans = 0
                print(arr)
                break
            else:
                top = arr.pop()

                if top == '(' and i == '}':
                    ans = 0
                    break
                elif top == '{' and i == ')':
                    ans = 0
                    break
    if len(arr) > 0:
        ans = 0

    print('#{} {}'.format(t, ans))