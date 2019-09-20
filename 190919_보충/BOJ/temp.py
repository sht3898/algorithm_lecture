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