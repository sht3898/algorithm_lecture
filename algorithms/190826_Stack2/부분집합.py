arr = 'ABC'; N = len(arr)
bits = [0] * N


def subset(k, n):       # k=현재 노드의 높이, n:단말 노드의 높이
    if k == n:          # 모든 선택이 완료, 단말 노드에 도착,
        for i in range(N):
            if bits[i]: print(arr[i], end='')
        print()
        return
    # 선택이 남아있다.
    bits[k] = 1;  subset(k + 1, n)    # 왼쪽
    bits[k] = 0;  subset(k + 1, n)    # 오른쪽


subset(0, N)            # 0 = 어떤 선택도 하지 않았다.
                        # N = 해야할 선택의 수



# for i in range(2):
#     bits[0] = i
#     for j in range(2):
#         bits[1] = j
#         for k in range(2):
#             bits[2] = k
#             print(bits)
