# 힙 구현
H = [0] * 100       # 저장소
top = 0             # 자료의 수, 마지막 노드의 인덱스


def push(item):
    global top
    top += 1
    H[top] = item
    c, p = top, top // 2    # 부모, 부모/2
    while p:
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2
        else:
            break
            

def pop():
    global top
    # empty 체크 필요
    ret = H[1]
    H[1] = H[top]
    top -= 1
    p, c = 1, 2
    while c <= top:
        if c + 1 <= top and H[c] > H[c+1]:
            c += 1
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            p = c
            c = p * 2       # 왼쪽 자식
        else:
            break

    return ret


data = [69, 10, 30, 2, 16, 8, 31, 22]
for val in data:
    push(val)

while top:
    print(pop(), end=' ')
