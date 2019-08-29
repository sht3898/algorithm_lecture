# 무한 호출

cnt = 0
bits = [0] * 3
def printHello(i, n):  # i : 함수 호출 트리에서의 높이
    global cnt
    if i == n:
        cnt += 1
        print(bits)
        return
    else: # printHello의 개수^n 만큼 cnt 됨
        bits[i] = 1; printHello(i + 1, n)
        bits[i] = 0; printHello(i + 1, n)

# for i in range(3):
#     print('Hello')

# printHello()


printHello(0, 3)
print('cnt =', cnt)