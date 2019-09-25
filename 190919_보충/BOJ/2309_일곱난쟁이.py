import sys; sys.stdin = open('2309_input.txt', 'r')

man = [0] * 9
for i in range(9):
    man[i] = int(input())
check = [0] * 9
arr = []
final = []


def solve(k):
    global final
    if k == 7:
        if sum(arr) == 100:
            final = sorted(arr)
        return
    for i in range(len(man)):
        m = man[i]
        if not check[i]:
            check[i] = 1
            arr.append(m)
            solve(k+1)
            arr.pop()
            check[i] = 0


solve(0)
for i in final:
    print(i)
