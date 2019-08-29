# C-Style
S = [0] * 3
top = -1


def push(item):
    global top
    # full-상태에 주의
    top += 1
    S[top] = item


def pop():
    if top == -1: return
    ret = S[top]
    top -= 1
    return ret

S = []
S.append(1)
S.append(2)
S.append(3)

print(S.pop()); print(S.pop())