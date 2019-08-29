arr ='ABC'; N = len(arr)
order = [0] * N             # 원소의 인덱스의 순서를 저장


def perm(k, n, used):
    if k == n:          # 하나의 순열을 생성
        for i in range(n):
            print(arr[order[i]], end=' ')
        print()
        return
    for i in range(n):
        if used & (1 << i): continue
        order[k] = i
        perm(k + 1, n, used |(1 << i))


perm(0, N, 0)               # 0: 선택한수, N: 전체원소수, 0: 선택한 요소들의 집합