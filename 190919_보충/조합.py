# 조합 생성 ex) 3P2 {0, 1, 2}
# N = 3
# for i in range(N):
#     for j in range(N):
#         if i == j: continue
#         print(i, j)

# arr = 'ABCDE'
# N = 5   # {0, 1, 2, 3, 4}
# for i in range(0, N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             print(arr[i], arr[j], arr[k])

arr = 'ABCDE'
N, R = 5, 3 # {0, 1, 2, 3, 4}
choose = []


def comb(k, s):     # 선택할 요소의 시작값
    if k == R:      # 모두 선택
        print(choose)
        return

    for i in range(s, N):
        choose.append(i)
        comb(k + 1, i + 1)
        choose.pop()


comb(0, 0)


for i in range(3):
    for j in range(i + 1, 3):
        print(i, j)
