order = 'ABC'; N=len(arr)
used = [0] * N                      # 실제 요소들의 순서(index를 기록)

def perm(k, n):
    if k == n:
        for i in range(N):
            print(order[i], end='')
        print()
        return
    used = [False] * N
    for i in range(N):              # 지금까지 선택한 k개의 원소를 확인
        used[order[i]] = True

    for i in range(N):
        if used[i]: continue
        order[k] = i
        perm(k + 1, n)



# for i in range(N):
#     for j in range(N):
#         if i == j:
#         for k in range(N):
#             print(order[i], order[j])
